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

csvfile = open('Rios.csv', 'wb')
csvwriter = csv.writer(csvfile)
for item in data:
    csvwriter.writerow(item)
csvfile.close()

import pandas
from pandas import *
df=pandas.read_csv('Rios.csv', sep=',',header=None)
#La columna 1 indica la razon en m2.
df=df.sort(columns=0,ascending=False)

RIOS=df[0:299]
#print RIOS

RIOS.to_csv("top_300_rios.csv", sep=' ', header=False, index=False, mode='w')

os.system("rm RIOS.txt")
os.system("rm Rios.csv")

