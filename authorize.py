# Include the config settings
import config
# Import other stuff
import webbrowser
# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = config.APP_KEY
app_secret = config.APP_SECRET

flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

# Have the user sign in and authorize this token
authorize_url = flow.start()
webbrowser.open(authorize_url)

code = raw_input("Enter the authorization code here: ").strip()

# This will fail if the user enters an invalid authorization code
access_token, user_id = flow.finish(code)
out = open('.token', 'wb')
out.write(access_token)
out.close()
