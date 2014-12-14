import picamera
import shutil
import os

camera = picamera.PiCamera()

camera.capture('image.jpg')

file = open('/home/pi/cis191/marker.txt', 'r+')
x = int(file.readline())

shutil.move("image.jpg", "/home/pi/cis191/sync/Img"+str(x)+".jpg")
file.close()

os.remove("/home/pi/cis191/marker.txt")

file = open('/home/pi/cis191/marker.txt', 'w')
file.write(str(x+1))
file.close()

print "Made Image " + str(x)
