from PIL import Image
from resizeimage import resizeimage
import os

dir = 'images/'
files = [f for f in os.listdir(dir)] # check extension if necessary

for f in files:
	print(f)
	fd_img = open(dir + f, 'r+b')
	img = Image.open(fd_img)
	img = resizeimage.resize_thumbnail(img, [100, 100])
	img.save(dir + f + '-thumbnail', img.format)
	fd_img.close()