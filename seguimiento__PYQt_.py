import numpy as np
import ephem as ep
import time  as ti
import datetime 
import math 

import ntplib as ntp
import datetime
import sys
from matplotlib.widgets import MultiCursor
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as  FigureCanvas
from matplotlib.figure import Figure

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from  sat_ruta_datos import *
import PyQt4.Qwt5 as Qwt
#from qwt_plot import QwtPlot

#importando clases y o funciones
from datetime import datetime
from datetime import timedelta
import cPickle


x = ntp.NTPClient()
c=x.request("3.north-america.pool.ntp.org",version=4,timeout=5)

#fchea actual en UTC 
#t = datetime.utcfromtimestamp(c.recv_time)
t2="2016/11/30"

#sacando los sateliters a obsevar 
with open(r"Sat_see/sateli.pickle", "rb") as input_file:
	sat_v=cPickle.load(input_file)

sat_l=list(sat_v.keys())
#sacando el observador 

with open(r"Sat_see/date_obs.pickle", "rb") as input_file:
	D_obs=cPickle.load(input_file)

ob_lis=list(D_obs.keys())

fic_lug=D_obs[ob_lis[2]]


with open(fic_lug, "rb") as input_file:
	l_obs=cPickle.load(input_file)



#lugar de observacion 
obse=ep.Observer()
obse.long=l_obs["logitud"]
obse.lat=l_obs["Alt"]
#use una plicacion
obse.elevation=l_obs["elevacion"]  #en metros 



obse.date=ep.date(t2)   #toma fecha y hora ingresada 
#comparacion de la hora
print('Hora Actual UTC \n %s'% obse.date)

print('Hora Actial TL \n %s'%ep.localtime(ep.now()))

#obveto que sera observado 
#Datos de los satelites 

Sat_s=dict()
for k in sat_l:
	fi=sat_v[k]
	sat=leertxt(fi)
	Sat_s[sat.name]=sat

sat=Sat_s["ISS (ZARYA)"]

seg=obse.next_pass(sat)

print('Rise time(UTC): %s \n Rise time(TL): %s \n Rise azimuth: %s \n \
Maximum altitude time(UTC): %s \n Maximum altitud(TL): %s \n \
Maximum altitude: %s \n Set time(UTC): %s  Set time(TL): %s \n  Set azimuth: %s '\
%(seg[0], ep.localtime(seg[0]),np.rad2deg(seg[1]),seg[2],ep.localtime(seg[2]),\
np.rad2deg(seg[3]),seg[4],ep.localtime(seg[4]),np.rad2deg(seg[5])))

# convetri la fecha en lista para manejar solo un elemento

ini=seg[0].tuple()
fin=seg[4].tuple()

#tipo de vista con el satelite 

ti_h=int(fin[3])-int(ini[3])

ti_m=int(fin[4])-int(ini[4])

ti_s=int(fin[5])-int(ini[5])

# Corregui el erro de los tiempos
 
if ti_s<0:
	ti_m=ti_m-1
	ti_s=60+ti_s

ti_v=[ti_h,ti_m, ti_s]

#print(ti_v);
#print(type(ti_v));

#timpo de incio 
esp=[ini[0],ini[1],ini[2],ini[3],int(ini[4])]

#print(esp)
#print(type(esp))
#print(ep.date(tuple(esp)))
dt=[]

#inicio de la observacion 5 minutos antes 

midnight = ep.date(tuple(esp))
	#print(midnight)
	#print(type(midnight))

#vetro con el tiempo 2 minutos depues 
dt  = [midnight + ep.minute*x + ep.second*y*2 for x in range(0 , ti_m+2) for y in range(0,30)]
#print(dt)
#print(type(dt[10]))

#Calculo de los datos para ala antena 
ejex_ti=[]
sat_alt, sat_az = [], []
for date in dt:
	obse.date = date
	#print ti.time(date)
	sat.compute(obse)
	sat_alt.append(np.rad2deg(sat.alt))
	sat_az.append(np.rad2deg(sat.az))

#intevalo para desicidir que graficar 

#for s in sat_alt:
#	print ("%s\n",s)  

#print np.max(sat_alt)

#fig=plt.figure()
#fig.add_subplot(1, 1, 1) 
#
#plt.plot(sat_az,'b')
#plt.ylabel("Azimut (deg) azul")
#plt.ylim(0,360)
#plt.twinx()

#plt.plot(sat_alt,'r')
#plt.ylabel("Altidud (deg) rojo")
#plt.ylim(0,90)
#plt.ioff()
#plt.show()
## Creado la grafica de azimut y altitud



## Clase para generar la tabla 

class MyTable(QTableWidget):
	def __init__(self, data, *args):
		QTableWidget.__init__(self, *args)
		self.data = data
		self.setmydata()
		self.resizeColumnsToContents()
		self.resizeRowsToContents()
 
	def setmydata(self):
 
		horHeaders = []
		for n, key in enumerate(sorted(self.data.keys())):
			horHeaders.append(key)
			for m, item in enumerate(self.data[key]):
				newitem = QTableWidgetItem(str(item))
				self.setItem(m, n, newitem)
		self.setHorizontalHeaderLabels(horHeaders)




#fil=len(sat_az)

#dt=[ep.date(x) for x in dt]

#col={"teimpo":dt, "Azimut":(sat_az) ,"Altitud":(sat_alt)}

class Datos(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui=Ui_W_seg_sat()
		self.ui.setupUi(self)
		self.setWindowTitle(sat.name)
		self.t_datos()
		self.ui.TW_seg_sat.resizeColumnsToContents()
		self.ui.TW_Sat_paso.removeTab(0)
		
		
	def t_datos(self):
		#generando la primeraparte
		self.ta=MyTable(col,fil,3)
		self.graaz=Lienzo()
		self.ui.TW_Sat_paso.addTab(self.ta,"Teimpos")
		self.ui.TW_Sat_paso.addTab(self.graaz,'Grafica')





#if __name__ == "__main__":
    #app = QtGui.QApplication(sys.argv)
    #myapp = Datos()
    #myapp.show()
    #app.exec_()

##print(midnight)
##print(type(ejex_ti))



##print(type(sat_alt))

##print('\n'.join(map(str,90-np.array(sat_alt))))

##print(90-np.array(sat_alt))

 


#f1=plt.figure
#plt.polar(np.deg2rad(sat_az),(90-np.array(sat_alt)))
#plt.ion() 
#plt.ylim(0,90)
#plt.show()


