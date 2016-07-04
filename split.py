# script to automatically crop single photo

from __future__ import print_function
from PIL import Image
import os

im = Image.open(input("img: "))
letter = input("letter: ")
columns = int(input("# berry columns: "))
rows = int(input("# berry rows: "))

crop_col = int(im.size[0]/columns)
crop_row = int(im.size[1]/rows)

directory = input("dir: ")
if not os.path.exists(directory):
    os.makedirs(directory)

for i in range(0,columns):
     for j in range(0,rows):
        tmp = im.crop((i*crop_col,j*crop_row,i*crop_col+crop_col,j*crop_row+crop_row))
        tmp.load()
        tmp.save(directory+"/"+letter+'_'+str(i)+str(j)+".jpg")
        
