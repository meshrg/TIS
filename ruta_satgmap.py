import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import ephem as ep
import time  as ti
import datetime 
import math 
import ntplib as ntp

#import pylab as plt
from datetime import datetime
import datetime as dat
import folium
from folium import Map, FeatureGroup, Marker, LayerControl


#punto de obsecacion 
lat=(22.4520984)
lon=-102.2925
zac=ep.Observer()
zac.long=ep.degrees(lon)
zac.lat=ep.degrees(lat)
#use una plicacion
zac.elevation=2239  #en metros 

#Timpo y feca 
x = ntp.NTPClient()
c=x.request("mx.pool.ntp.org",version=1,timeout=5)
t=datetime.utcfromtimestamp(c.orig_time)



#Satelites a observar 
zac.date=t     #toma la fecha y hora actual 
ISS = ep.readtle('ISS (ZARYA)',             
'1 25544U 98067A   17053.52178456  .00003000  00000-0  52044-4 0  9996',
'2 25544  51.6415 249.9050 0006460 218.3606 198.6745 15.54414638 43924')

ISS.compute(zac)

lon=np.rad2deg(ISS.sublong)
lat=np.rad2deg(ISS.sublat)

mapOBJ=Map(location=[lat, lon], zoom_start=3,
           tiles='Stamen Terrain')
m1=folium.Marker([22.4520984,-102.2925],popup="CIDTE")
m1.add_to(mapOBJ)

s1=folium.RegularPolygonMarker([np.rad2deg(ISS.sublat), np.rad2deg(ISS.sublong)],
                    radius=5,
                    popup=ISS.name,
                    color='#3186cc',
                    fill_color='#3186cc',
                   )
mapOBJ.add_children(s1)

mapOBJ.save('map.html')

midnight = zac.date(tuple(esp))

print(midnight)
print(type(midnight))

#vetro con el tiempo 2 minutos depues 

print(dt)
print(type(dt[10]))

#Calculo de los datos para ala antena
 
dt,li=day_sat(datetime(2017,02,21),datetime(2017,02,22),M=0,S=30)

ejex_ti=[]
sat_lat_lon=[]
for date in dt:
	zac.date = date
	print ti.time(date)
	ISS.compute(zac)
	sat_lat_lon.append([np.rad2deg(ISS.sublat),np.rad2deg(ISS.sublong)])


line=folium.PolyLine(sat_lat_lon, color="red", weight=2.5, opacity=1).add_to(mapOBJ)


class Gafica_ruta_save(QDialog):
	def __init__(self,parent=None):
		QWidget.__init__(self, parent)
		self.webview = QWebView()
		self.webview.load(QUrl("file:///home/cidte/programas de python/Ejercicio de Python/partes del codigo/map.html"))
		self.la=QVBoxLayout()
		self.la.addWidget(self.webview)
		self.setLayout(self.la)
