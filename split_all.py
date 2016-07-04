# script to automatically crop all photos in directory

from __future__ import print_function
from PIL import Image
import os

cdir = input("current_dir: ")
files = os.listdir(cdir)

p = []
for i in sorted(files):
    p.append(cdir+'//'+i)

columns = int(input("# berry columns: "))
rows = int(input("# berry rows: "))

directory = input("new_dir: ")
if not os.path.exists(directory):
    os.makedirs(directory)

os.chdir('//home//f-vasconcelos//wv2016//rasp')

for n in range(len(p)):
    im = Image.open(p[n])
    crop_col = int(im.size[0]/columns)
    crop_row = int(im.size[1]/rows)
    m=0
    for i in range(0,columns):
        for j in range(0,rows):
            tmp = im.crop((i*crop_col,j*crop_row,i*crop_col+crop_col,j*crop_row+crop_row))
            tmp.load()
            tmp.save(directory+"/"+str(n+1)+'_'+str(m)+".jpg")
            m += 1
        
