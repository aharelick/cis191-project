from PIL import Image
import PIL.ImageOps
from os import listdir

sync_dir = (f for f in listdir("/home/pi/cis191/sync/"))

for f in sync_dir:
    if not "Inv" in f and not "Blur" in f:
        image = Image.open("/home/pi/cis191/sync/" + f)
        inverted_image = PIL.ImageOps.invert(image)
        inverted_image.save("/home/pi/cis191/sync/Inv" + f)
