# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>


#PUNTO 2A
import urllib
import os
from os import system
import csv
import numpy as np


urllib.urlretrieve("http://www.cgd.ucar.edu/cas/catalog/surface/dai-runoff/coastal-stns-byVol-updated-oct2007.txt","RIOS.txt")


os.system("sed -i 's/,//g' RIOS.txt")
os.system("sed '621d' RIOS.txt")


data=np.genfromtxt('RIOS.txt',dtype=None,skiprows=1,usecols=(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13))


RIOS=data[0:299]


csvfile = open('top_300_rios.csv', 'wb')
csvwriter = csv.writer(csvfile)
for item in RIOS:
    csvwriter.writerow(item)
csvfile.close()


os.system("rm RIOS.txt")



