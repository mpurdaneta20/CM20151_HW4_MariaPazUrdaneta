# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

#PUNTO 2B
from pylab import *

from mpl_toolkits.basemap import Basemap
import csv
import pandas
from pandas import *

File = open('top_300_rios.csv', 'r+')
csvFile = csv.reader(File)
RIOS=[]
for i in range(150):
    R=csvFile.next()
    RIOS.append(R)

RIOS=pandas.read_csv('top_300_rios.csv', sep=' ',header=None, usecols=[1,2])

LON=[]
for item in RIOS[1]:
    LON.append(float(item))
#print LON

LAT=[]
for item in RIOS[2]:
    LAT.append(float(item))
#print LAT

map = Basemap(projection='kav7',lon_0=180)
# plot linea costera, meridianos y paralelos
map.drawcoastlines()
map.drawparallels(np.arange(-90,90,30),labels=[1,0,0,0])
map.drawmeridians(np.arange(map.lonmin,map.lonmax+30,60),labels=[0,0,0,1])
lons = LON
lats = LAT
x,y = map(lons, lats)
map.plot(x, y, 'bo', markersize=4)
show()

