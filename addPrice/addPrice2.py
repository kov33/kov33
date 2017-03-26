# -*- coding: UTF8 -*-

import csv
import os
import errno
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

prefix = "D:\\kovka\\assets\\"

dest = "D:\\kovka\\_site\\assets\\"

infile_prefix = "..\\resize\\"

with open('prices.csv', 'rt') as csvfile:
    pricereader = csv.reader(csvfile, delimiter=';')
    for row in pricereader:
        infile = row[0].replace(prefix,"").lower()
        img = Image.open(infile_prefix+infile)
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("BOOKOS.ttf", 32) #ARIALUNI
# draw.text((x, y),"Sample Text",(r,g,b))

        w,h = img.size
        text = row[1] + " руб."
        tw,th = draw.textsize(text, font)
        draw.text( (w/2-tw/2, h-42 ),text,(0,0,0),font=font, anchor="c" )
        draw.text( (w/2-1-tw/2, h-42-1 ),text,(0,0,255),font=font, anchor="c" )

        destFile = dest+infile
        head, tail = os.path.split(destFile)
        try:
          os.makedirs(head)
        except :  # Python >2.5
          pass

        img.save(destFile)