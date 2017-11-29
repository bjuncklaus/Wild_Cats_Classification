from PIL import Image
import os

source_dir = 'images/oncas/'
destination_dir = 'images/greyscaled/'

if not os.path.exists(destination_dir):
    os.mkdir(destination_dir)

files = [f for f in os.listdir(source_dir)]

for f in files:
    print('Found image:', f)
    img = Image.open(source_dir + f).convert('L')
    img.save(destination_dir + f)
