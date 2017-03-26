# -*- coding: UTF8 -*-

import csv
import subprocess

prefix = "D:\\kovka\\assets\\"

with open('prices.csv', 'rt') as csvfile:
    pricereader = csv.reader(csvfile, delimiter=';')
    for row in pricereader:
        infile = row[0].replace(prefix,"").lower
#        print( row[0])
#        print( row[1])
        print("magick convert -size 600x150 xc:none -font Arial -pointsize 128 -gravity center -stroke black -strokewidth 10 -annotate 0 '" + row[1] +  " руб.' -background none -shadow 100x3+0+0 +repage -stroke none -fill white     -annotate 0 '" + row[1] + " руб.'  " + infile + " +swap -gravity south -geometry +0-3 -composite  " + "../_site/assets/"+infile)
#        subprocess.call("magick convert -size 600x150 xc:none -font Arial -pointsize 128 -gravity center -stroke black -strokewidth 10 -annotate 0 '" + row[1] +  " руб.' -background none -shadow 100x3+0+0 +repage -stroke none -fill white     -annotate 0 '" + row[1] + " руб.'  " + row[0].replace(prefix,"") + " +swap -gravity south -geometry +0-3 -composite  " + "../_site/assets/"+row[0], shell=True)
