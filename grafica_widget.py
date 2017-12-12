#preva de la grafica con el widget 
#ISS 

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PyQt4.QtWebKit import QWebView
from PyQt4 import QtCore
from PyQt4 import QtGui

import sys
import numpy as np
import ephem as ep
import time  as ti
import datetime 
import math 
import ntplib as ntp

#import pylab as plt
from datetime import datetime
import datetime as dat
#liberia de los graficos
from bokeh.plotting import figure


from bokeh.io import output_file, show,save,vform
from bokeh.models import Select,ColumnDataSource, Circle, DataRange1d, Select, HoverTool,LinearAxis, Range1d, HoverTool
from bokeh.models.widgets import Panel, Tabs, DataTable, DateFormatter, TableColumn,NumberFormatter,TimeEditor
from bokeh.layouts import widgetbox

import yaml 
from os import path


######################################################################
##### Batos inicales #################################################
######################################################################

#punto de obsecacion 
zac=ep.Observer()
zac.long=ep.degrees("-102.2925")
zac.lat=ep.degrees("22.4520984")
#use una plicacion
zac.elevation=2239  #en metros 

#Timpo y feca 
x = ntp.NTPClient()
c=x.request("mx.pool.ntp.org",version=4,timeout=5)
t=datetime.utcfromtimestamp(c.recv_time)

#Satelites a observar 
zac.date=t     #toma la fecha y hora actual 
ISS = ep.readtle("ISS (ZARYA)",             
"1 25544U 98067A   17028.69377315  .00005276  00000-0  86681-4 0  9992",
"2 25544  51.6440  13.7099 0007722 130.1081 228.0714 15.54189634 40052")

#class tiempos(objecto):

	#def __init__(self,h_i=None,h_f=None,H=None,M=None,S=None):
		
		#if h_i==type("2332"):
			#self.h_i==datetime.strptime(h_i,"1%Y/%m/%d %H:%M:%S")
		#else:
			#self.h_i=h_i
		
		#if h_f==type("1221"):
			#self.h_f==datetime.strptime(h_f,"1%Y/%m/%d %H:%M:%S")
		#else:
			#self.h_f=h_f
		
		#if H==None:
			#self.H=0
		#else: 
			#self.H=H
		
		#if M==None:
			#slef.M=1
		#else:
			#self.M=M
		
		#if S==None:
			#self.S=30
		#else:
			#self.S=S
	
	
	
	#def day_sat(self,hora_ini=self.h_i,H=self.H,M=self.M,S=self.S):
		#"""
		#Datos para todo el dia desde el punto de inicio del dia 
		#"""
		#self.ini=hora_ini.date()
		#self.fin=self.ini+dat.timedelta(hours=24)
		#li=[datetime.strptime(("00:00:00"),"%H:%M:%S")]
		#midnight = self.ini
		#dt=[ti_ini]
		#while midnight < self.fin:
			#midnight=midnight+dat.timedelta(minutes=M)+dat.timedelta(seconds=S)
			#li.insert(indice,li[indice-1]+dat.timedelta(minutes=M)+dat.timedelta(seconds=S))
			#dt.insert(indice,midnight)
			#indice=indice+1
		#return dt,li


def see_time(h_i,h_f,H=None,M=None,S=None):
	"""
	Genera los timpos para de una manera "equitativa". mientras esta en linea de vista.
	"""
	if type(h_i)==type("2332"):
		h_i==datetime.strptime(h_i,"1%Y/%m/%d %H:%M:%S")
		
	if type(h_f)==type("1221"):
		h_f==datetime.strptime(h_f,"1%Y/%m/%d %H:%M:%S")
	
	if H==None:
		H=0
	
	if M==None:
		M=0
	if S==None:
		S=30

	ti_see=ti_final-ti_ini
	indice=1
	
	if ti_see>dat.timedelta(days=31):
		li=[datetime.strptime(("00 00:00:00"),"%d %H%M:%S")]
		midnight = ti_ini
		dt=[ti_ini]
		while midnight < ti_final:
			midnight=midnight+dat.timedelta(hours=H)
			dt.insert(indice,midnight)
			li.insert(indice,li[indice-1]+dat.timedelta(hours=H))
			indice=indice+1
		return dt,li

	elif ti_see>dat.timedelta(days=1):
		li=[datetime.strptime(("00:00:00"),"%H:%M:%S")]
		midnight = ti_ini
		dt=[ti_ini]
		while midnight < ti_final:
			midnight=midnight+dat.timedelta(hours=H)+dat.timedelta(minutes=M)
			li.insert(indice,li[indice-1]+dat.timedelta(hours=H)+dat.timedelta(minutes=M))
			dt.insert(indice,midnight)
			indice=indice+1
		return dt,li
	elif ti_see>dat.timedelta(hours=1):
		li=[datetime.strptime(("00:00:00"),"%H%M:%S")]
		midnight = ti_ini
		dt=[ti_ini]
		while midnight < ti_final:
			midnight=midnight+dat.timedelta(minutes=M)+dat.timedelta(seconds=S)
			dt.insert(indice,midnight)
			li.insert(indice,li[indice-1]+dat.timedelta(minutes=M)+dat.timedelta(seconds=S))
			indice=indice+1
		return dt,li

	elif ti_see>dat.timedelta(minutes=1):
		li=[datetime.strptime(("00:00"),"%M:%S")]
		midnight = ti_ini
		dt=[ti_ini]
		while midnight < ti_final:
			midnight=midnight+dat.timedelta(minutes=M)+dat.timedelta(seconds=S)
			li.insert(indice,li[indice-1]+dat.timedelta(minutes=M)+dat.timedelta(seconds=S))
			dt.insert(indice,midnight)
			indice=indice+1
		return dt,li



######################################################################
##### Calculo de los datos para la obsrcacion ########################
######################################################################

#gra_dic=dict()
#print "Timpo del observador"
#print zac.date

#gra_dic["sat_name"]=ISS.name
#gra_dic["lug_ob"]="zacatecas"

#print "tiempo de los datos del satelite"
#print ISS._epoch

##Selecion de el minimo tiempo posibel.
#while True:
	#seg=zac.next_pass(ISS)

	#print "siguiente paso por el obsevador"
	#print('Rise time: %s \n Rise azimuth: %s \n Maximum altitude time: %s \
		#\n Maximum altitude: %s \n Set time: %s \n  Set azimuth: %s '\
		#%(seg[0],np.rad2deg(seg[1]),seg[2],np.rad2deg(seg[3]),seg[4],np.rad2deg(seg[5])))

### convetri la fecha en lista para manejar solo un elemento
	#ini=seg[0].tuple()
	#fin=seg[4].tuple()
##zac.date= "2017/1/24 01:38:00"
##ISS.compute(zac)
##print ISS.alt

##tipo de vista con el satelite
######Forato del next_pass
	#ti_formato="%Y/%m/%d %H:%M:%S"
#####Formato para restar las horas

##Convetimos los timpos a formatos datetime
	#ti_final=datetime.strptime(str(seg[4]),ti_formato)
	#ti_ini=datetime.strptime(str(seg[0]),ti_formato) 

##print datetime.strptime(str(ini),ti_formato)

	#print ti_ini

	#print ti_final

	#ti_see=ti_final-ti_ini
	#print ti_see
	#if ti_see>dat.timedelta(minutes=6):
		#break
	#zac.date=ti_final+dat.timedelta(seconds=60)


###############################################################################
###### Calculo de los puntos a obsevar ########################################
###############################################################################


#print ti_see
###Timepo de vista 
##midnight = ti_ini
##dt=[ti_ini]

##indice=1
##li=[datetime.strptime(("00, 00"),"%M, %S")]

#dt,li=see_time(ti_ini,ti_final,S=30)
##print dt
#gra_dic["date_time"]=dt
#gra_dic["Escal_time"]=li

##while midnight < ti_final:
	##midnight=midnight+dat.timedelta(minutes=0)+dat.timedelta(seconds=1)
	##dt.insert(indice,midnight)
	##li.insert(indice,li[indice-1]+dat.timedelta(minutes=0)+dat.timedelta(seconds=1))
	##indice=indice+1

###print(midnight)
##for x in dt:
	##print(ep.date(x))

##Tablas de los datos 
#sat_alt, sat_az = [], []
#sat_speed, sat_dis = [], []
#sat_lati, sat_long = [], []
#Time=[]
#for date in dt:
	#zac.date =ep.date(date)
	#ISS.compute(zac)
	#Time.append(str(zac.date))
	#sat_alt.append(np.rad2deg(ISS.alt))
	#sat_az.append(np.rad2deg(ISS.az))
	#sat_speed.append(ISS.range_velocity)
	#sat_dis.append(ISS.range)
	#sat_long.append(np.rad2deg(ISS.sublong))
	#sat_lati.append(np.rad2deg(ISS.sublat))

#gra_dic["ant_alt"]=sat_alt
#gra_dic["ant_az"]=sat_az
#gra_dic["longitud"]=sat_long
#gra_dic["latitud"]=sat_lati
#gra_dic["Tiempo"]=Time

#Nom=gra_dic["sat_name"]

#fiche=open(path.join("Sat_datos",Nom),"w")
#fiche.write(yaml.dump(gra_dic))
#fiche.close()

##Diciconaro con los datos 

##print "velosidad"
##print np.array(sat_speed)
##print "Distacia con el observador"
##print np.array(sat_dis)
##print "Azimut"
##print np.array(sat_az)
##print "altitud"
##print np.array(sat_alt)



###############################################################################
###### Graficando los datos ###################################################
###############################################################################

rut="Sat_datos"
with open(path.join(rut,"ISS (ZARYA)")) as ymlfile:
	gra_dic_2=yaml.load(ymlfile)

#print gra_dic_2


Source=ColumnDataSource(
	data=dict(
		x=gra_dic_2["Escal_time"],
		al=gra_dic_2["ant_alt"],
		az=gra_dic_2["ant_az"],
		lon=gra_dic_2["longitud"],
		lati=gra_dic_2["latitud"],
		t=gra_dic_2["Tiempo"]
		)
	)


hover1 = HoverTool(
		tooltips=[
			("Grados", "$y"),
			("Timpo", "@t"),
		]
	)

hover2 = HoverTool(
		tooltips=[
			("Grados", "$y"),
			("Timpo", "@t"),
		]
	)
	



#show(curdoc) 

#creamos el nuevo plot 
p = figure(
	tools="save,pan",
	y_range=Range1d(start=0,end=90), title="grafica de angulo de azimut y altitud",x_axis_type="datetime",
	x_axis_label='timepo', y_axis_label='altitud')



left = figure(title="Altitud", tools=[hover1,"crosshair"], width=450 , height=450,
	y_range=Range1d(start=0,end=90), x_axis_type="datetime", x_axis_label='Tiempo')

left.line(x="x",y="al",source=Source, color="red")
tab2 = Panel(child=left, title="Altitud")

#show(left)
#save(left,"altitud_gra.html",validate=True)

# create another new plot and add a renderer
right = figure(title="Azimut",tools=[hover2,"crosshair"],  width=450 , height=450,
	y_range=Range1d(start=0,end=360),x_axis_type="datetime",x_axis_label='Tiempo')
	
right.line(x="x",y="az", source=Source,color="blue")
tab1 = Panel(child=right, title="Azimut")


tabs = Tabs(tabs=[ tab1, tab2 ])

#show(tabs)

save(tabs,"az_alt_gra.html",validate=True)




DF_ag=NumberFormatter(format="0.00")
columns = [
		TableColumn(field="t", title="Tiempo"),
		#TableColumn(field="downloads", title="Downloads"),
		TableColumn(field="al",title="Altidu (Grados)",formatter=DF_ag,sortable=True),
		TableColumn(field="az",title="Azimut (Grados)",formatter=DF_ag,sortable=True)
	]

data_table = DataTable(source=Source, columns=columns ,width=450, height=450)
save(data_table,"data_table.html",validate=True)





#angu_lat = figure(title="Latitud", tools=["crosshair"], width=450 , height=450,
	#y_range=Range1d(start=(-90),end=90), x_axis_type="datetime", x_axis_label='Tiempo')

#left.line(x="x",y="lati",source=source, color="black")
#tab3 = Panel(child=angu_lat, title="Latitud")

##show(angu_lat)
##save(angu_lat,"Latitud_gra",validate=True)

## create another new plot and add a renderer
#angu_long = figure(title="Longitud",tools=["crosshair"],  width=450 , height=450,
	#y_range=Range1d(start=(-180),end=180),x_axis_type="datetime",x_axis_label='Tiempo')
	
#right.line(x="x",y="lon", source=source,color="black")
#tab4 = Panel(child=angu_long, title="Longitud")

## put the subplots in a gridplot

##show(angu_long)
##save(angu_long,"longitud_gra",validate=True)

#tabs2 = Tabs(tabs=[ tab3, tab4 ])

#show(tabs2)

class Gafica_ruta(QDialog):
	def __init__(self,parent=None):
		QWidget.__init__(self, parent)
		self.resize(530,540)
		self.webview =QWebView()
		self.webview.load(QUrl("file:///home/cidte/programas de python/Ejercicio de Python/partes del codigo/data_table.html"))
		self.la=QVBoxLayout()
		self.la.addWidget(self.webview)
		self.setLayout(self.la)

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Gafica_ruta()
    myapp.show()
    sys.exit(app.exec_())

