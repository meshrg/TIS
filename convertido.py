from PyQt4.QtCore import *
from PyQt4.QtGui import *
from  lis_observa import *
import sys
#import ntplib as ntp
from lista import lista 
from lista import l_obs
from gcode_ import pygeoDi
from datetime import datetime
from os import path

from add_datos import *

import os
import cPickle

#x = ntp.NTPClient()
#c=x.request("mx.pool.ntp.org",version=4,timeout=5)
#fchea actual en UTC 
#t = datetime.utcfromtimestamp(c.recv_time)

root_ob = 'observa'

lis=[]
citis=[]
#tomando las direccines de cada uno de la ciudades.  
for fileList in os.walk(root_ob):
	fileList=str(fileList)

#manejo de archivos 
#toma los Datos ya exixtentes 
#fi=os.path("Sat_see","Datos_obs")

##cargando el archivo ruta de las carpeta 
#with open(fi+".pickle", "rb") as input_file:
	#D_obs=cPickle.load(input_file)

#convirtiendo los datos de una lista de str.

datos=fileList.split("[]")[1]
for l in datos.split("'"):
	if (".pickle" in l):
		citis.append(l)

#tomamos los nombres
#for x in citis:
	#s=x.split(".")[1]
	#if s=".pickle":
		#lis.append(x.split(".")[0])
	#else:
	#lis.append(x.split(".")[2])
	
print lis
for direct in citis:
	with open(path.join(root_ob,direct), "rb") as input_file:
		Ob_datos=cPickle.load(input_file)
	if "Alt" in Ob_datos:
		Ob_datos["latitud"]=Ob_datos["Alt"]
		del(Ob_datos["Alt"])
	
	with open(path.join(root_ob,direct), "wb") as output_file:
			cPickle.dump(Ob_datos, output_file)
