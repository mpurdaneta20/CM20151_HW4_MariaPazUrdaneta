# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

from pylab import*

from mpl_toolkits.basemap import Basemap
import csv



File = open('top_300_rios.csv', 'r+')
csvFile = csv.reader(File)
RIOS=[]
for i in range(150):
    R=csvFile.next()
    RIOS.append(R)
LAT=[]
LON=[]
for row in RIOS:
    LAT.append(float(row[2]))
    LON.append(float(row[1]))



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



