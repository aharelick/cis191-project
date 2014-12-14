# Include the config settings
import config
# Import other stuff
from os import listdir
from os.path import isfile, join
import os
from PIL import Image
# Include the Dropbox SDK
import dropbox

# do we want to sync the file (image)
def restrictions(f):
	return True

# grab token from file
token_file = open(os.path.join('/home/pi/cis191/', '.token'), 'rb')
access_token = token_file.read()
token_file.close()

# create client with token
client = dropbox.client.DropboxClient(access_token)

# create list of files in dropbox folder (the [1:] is to take away the slash in the name)
folder_metadata = client.metadata('/')
dropbox_dir_gen = (content['path'][1:] for content in folder_metadata['contents'] if not content['is_dir'])
dropbox_dir = list(dropbox_dir_gen)

# create list of files in local dir with restrictions
local_dir_gen = (f for f in listdir(config.REL_SYNC_DIR) if restrictions(join(config.REL_SYNC_DIR,f)))
local_dir = list(local_dir_gen)

# create list of files to upload bases on OVERRIDE settings
to_upload = []
if not config.OVERRIDE:
	to_upload = (f for f in local_dir if f not in dropbox_dir)
else:
	to_upload = local_dir

for name in to_upload:
	upload = open(join(config.REL_SYNC_DIR, name), 'rb')
	try:
	    response = client.put_file(name, upload, True)
	    print "uploaded", name
	except (KeyboardInterrupt, SystemExit):
	    raise
	except:
		print "There was an error uploading the file, perhaps your internet is down or you need to reauth."
		exit()
