
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
import ephem as ep
import datetime as dat

#Creamos el satelite 

#l1=raw_input("Linea 1 de formtato TLE\n")
#l2=raw_input("Linea 2 de formtato TLE\n")
#l3=raw_input("Linea 3 de formtato TLE\n")



# se crea el satelite
l1="ISS (ZARYA)"
l2="1 25544U 98067A   17317.62840120  .00004117  00000-0  69389-4 0  9994"
l3="2 25544  51.6432  13.3344 0004461 113.6331  45.1344 15.54138509 84996"
 
ISS=ep.readtle(l1,l2,l3)

#creamos elobsevadro 

#lati=raw_input("\n\n Ingresa el valor de latitud \n")
#longi=raw_input("Ingresa el valor de longitud\n")


obse=ep.Observer()
obse.lat=(ep.degrees("22.4520984"))
obse.long=(ep.degrees("-102.2925"))
obse.elevation=2239  #en metros 
obse.date=ep.now() #toma la hora de la pc 

#t_s=raw_input("\nIngrese la fecha y tiempo en formato UTS \n ")
#ti_formato="%Y/%m/%d %H:%M:%S"

#t1=datetime.strptime(t_s,ti_formato)
#obse.date=t1

################################

ISS.compute(obse)

print (np.rad2deg(ISS.sublat))
print (np.rad2deg(ISS.sublong))
#creamos el mapa 

map=Basemap(projection="ortho",lat_0=np.rad2deg(ISS.sublat),lon_0=np.rad2deg(ISS.sublong))

map.drawmapboundary(fill_color='aqua')
map.fillcontinents(color='coral',lake_color='aqua')
map.drawcoastlines()

x, y = map(np.rad2deg(ISS.sublong), np.rad2deg(ISS.sublat))

map.plot(x, y, marker='D',color='b')

plt.show()

