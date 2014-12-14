from PIL import Image
import PIL.ImageOps
from os import listdir
from PIL import ImageFilter

sync_dir = (f for f in listdir("/home/pi/cis191/sync/"))

for f in sync_dir:
	if not "Blur" in f and not "Inv" in f:
		image = Image.open("/home/pi/cis191/sync/" + f)
		blur_im = image.filter(ImageFilter.BLUR)
		blur_im.save("/home/pi/cis191/sync/Blur" + f)
