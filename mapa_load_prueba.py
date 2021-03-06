#!/usr/bin/python
# -*- coding:latin-1 -*-
#!/usr/bin/python
# -*- coding: UTF-8 -*-


import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import ephem as ep

import datetime 
import math 
import ntplib as ntp


from datetime import datetime
import datetime as dat
import folium
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from bokeh.io import output_file, show,save,vform
from bokeh.models import Select,ColumnDataSource, Circle, DataRange1d, Select, HoverTool,LinearAxis, Range1d, HoverTool
from bokeh.models.widgets import Panel, Tabs, DataTable, DateFormatter, TableColumn,NumberFormatter
from bokeh.layouts import widgetbox

### librerias para el manejo de los archivos 
import cPickle
import pickle
from os import path
import yaml
import os
"""
###############################################################################
################ improtado progmama a utilizar ################################
"""

from Main_W_p1 import *
from plotdaynight import Grafica
from sat_tabla import MyTable
from gra_az_al import QT_url,Gra_azal


"""
################################################################################
####################### funciones extras #$####################################
"""
def see_time(ti_ini,ti_final,H=None,M=None,S=None):
	"""
	Genera los timpos para de una manera "equitativa". mientras esta en linea de vista.
	"""
	if H==None:
		H=0
	
	if M==None:
		M=0

	if S==None:
		S=5

	indice=1
	ti_see=ti_final-ti_ini
	
	if ti_see>dat.timedelta(days=31):
		li=[datetime.strptime(("00 00:00:00"),"%d %H:%M:%S")]
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
		li=[datetime.strptime(("00:00:00"),"%H:%M:%S")]
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

def day_sat(c_obser,c_sat):
	d_ini=dat.datetime.utcnow()
	#d_ini=d_ini.date()+
	##Definido los valores iniciales sin valor 
	final=(d_ini.date()+dat.timedelta(hours=24))
	ti_see=final-d_ini.date()
	midnight = d_ini.date()
	dt=[d_ini.date()]
	indice=1
	li=[datetime.strptime(("00:00:00"),"%H:%M:%S")]
	"""
	Los datos tinen que tenel devido formato y con esta librearias para que funcione bien 
	c_obser=(objeto) el observador . 
	c_sat=(obejto) el satalite a calcular
	d_sat=el diccionarion con el nombre del satelite y los timepos. 
	"""
	H=1
	M=0
	S=00
	gra_dic=dict()
	ti_formato2="%Y-%m-%d %H:%M:%S"
	gra_dic["sat_name"]=c_sat.name
	gra_dic["lug_ob"]=c_obser.name
	
	while midnight < final:
		midnight=midnight+dat.timedelta(hours=H)+dat.timedelta(minutes=M)+dat.timedelta(seconds=S)
		dt.insert(indice,midnight)
		li.insert(indice,li[indice-1]+dat.timedelta(hours=H)+dat.timedelta(minutes=M)+dat.timedelta(seconds=S))
		indice=indice+1
	
	gra_dic["date_time"]=dt
	gra_dic["Escal_time"]=li
	sat_alt, sat_az = [], []
	#sat_speed, sat_dis = [], []
	sat_lati, sat_long = [], []
	Time=[]
	
	for date in dt:
		c_obser.date =ep.date(date)
		c_sat.compute(obse)
		Time.append(str(obse.date))
		sat_alt.append(np.rad2deg(c_sat.alt))
		sat_az.append(np.rad2deg(c_sat.az))
		#sat_speed.append(c_sat.range_velocity)
		#sat_dis.append(c_sat.range)
		sat_long.append(np.rad2deg(c_sat.sublong))
		sat_lati.append(np.rad2deg(c_sat.sublat))
		#gra_dic[""]=
		#gra_dic[""]=
	gra_dic["ant_alt"]=sat_alt
	gra_dic["ant_az"]=sat_az
	gra_dic["longitud"]=sat_long
	gra_dic["latitud"]=sat_lati
	gra_dic["Tiempo"]=Time
	Nom=gra_dic["sat_name"]+"day"
	#print gra_dic
	###  Guardando el archivo en un yaml
	fiche=open(path.join("Sat_datos",Nom),"w")
	fiche.write(yaml.dump(gra_dic))
	fiche.close() 
	return gra_dic

def leertxt_lista(nomdre):
	arch=open(nomdre)
	l1=arch.readline()
	satlis=dict()
	while l1:
		l2=arch.readline()
		l3=arch.readline()
		sat=ep.readtle(l1,l2,l3)
		satlis[sat.name]=sat
		l1=arch.readline()
	arch.close()
	return satlis

def leertxt(nomdre):
	arch=open(nomdre)
	l1=arch.readline()
	while l1:
		l2=arch.readline()
		l3=arch.readline()
		sat=ep.readtle(l1,l2,l3)
		#print sat.name
		l1=arch.readline()
	arch.close()
	return sat


def dat_antena(c_obser,c_sat,d_sat):
	"""
	Los datos tinen que tenel devido formato y con esta librearias para que funcione bien 
	c_obser=(objeto) el observador . 
	c_sat=(obejto) el satalite a calcular
	d_sat=el diccionarion con el nombre del satelite y los timepos. 
	"""
	gra_dic=dict()
	ti_formato2="%Y-%m-%d %H:%M:%S"
	gra_dic["sat_name"]=c_sat.name
	gra_dic["lug_ob"]=c_obser.name
	sat_t_i=datetime.strptime(d_sat["Tiempo Inical"],ti_formato2)
	sat_t_f=datetime.strptime(d_sat["Tiempo Final"],ti_formato2)
	#sat_t_d=datetime.strptime(d_sat["Duracion"],"%H:%M:%S")
	#print sat_t_i
	#print sat_t_f
	
	dt,li=see_time(sat_t_i,sat_t_f)
	
	gra_dic["date_time"]=dt
	gra_dic["Escal_time"]=li
	sat_alt, sat_az = [], []
	#sat_speed, sat_dis = [], []
	sat_lati, sat_long = [], []
	Time=[]
	for date in dt:
		c_obser.date =ep.date(date)
		c_sat.compute(c_obser)
		Time.append(str(c_obser.date))
		sat_alt.append(np.rad2deg(c_sat.alt))
		sat_az.append(np.rad2deg(c_sat.az))
		#sat_speed.append(c_sat.range_velocity)
		#sat_dis.append(c_sat.range)
		sat_long.append(np.rad2deg(c_sat.sublong))
		sat_lati.append(np.rad2deg(c_sat.sublat))
		#gra_dic[""]=
		#gra_dic[""]=
	gra_dic["ant_alt"]=sat_alt
	gra_dic["ant_az"]=sat_az
	#print sat_az
	gra_dic["longitud"]=sat_long
	gra_dic["latitud"]=sat_lati
	gra_dic["Tiempo"]=Time
	Nom=gra_dic["sat_name"]
	###  Guardando el archivo en un yaml
	fiche=open(path.join("Sat_datos",Nom),"w")
	fiche.write(yaml.dump(gra_dic))
	fiche.close() 
	return gra_dic

"""
def seg_map()
mapOBJ = folium.Map(location=[22.4520984, -102.2925], zoom_start=6)

m1=folium.Marker([22.4520984, -102.2925],popup="CIDTE")
m1.add_to(mapOBJ)

mapOBJ.save(outfile='map.html')

#mapOBJ.save(outfile='map2.html')


"""

def ruta_sat(obse,sat_da,red):
	"""
	obser=diccionario 
	sat_da=diccionario
	
	"""
	mapOBJ = folium.Map(location=[(obse["latitud"]),(obse["logitud"]) ], zoom_start=2)

	m1=folium.Marker([float(obse["latitud"]),float(obse["logitud"])],popup=(obse["nombre"]))
	m1.add_to(mapOBJ)
	k_data=(list(sat_da.keys()))
	
	for nu in range(0,len(sat_da["latitud"])):
		pod=folium.Popup(red+" a las "+sat_da["Tiempo"][nu])
		s1=folium.RegularPolygonMarker([sat_da["latitud"][nu],sat_da["longitud"][nu]],
			radius=5,
			popup=pod,
			color='#3186cc',
			fill_color='#3186cc',
			)
		mapOBJ.add_children(s1)
	mapOBJ.save('map.html')

def tiempo_ajuste(obse,sat):
	"""
	obse=objeto 
	sat_da=objeto
	"""
	obse_2=obse
	sat_t=dict()
	n_s=obse_2.next_pass(sat)
	sat_t={"Tiempo Inical":datetime.strptime(str(n_s[0]),ti_formato),"Tiempo Final":datetime.strptime(str(n_s[4]),ti_formato),}
	if sat_t["Tiempo Inical"]>sat_t["Tiempo Final"]:
		obse_2.date=sat_t["Tiempo Inical"]
		n_s=obse_2.next_pass(sat)
		sat_t={"Tiempo Inical":str(datetime.strptime(str(n_s[0]),ti_formato)),"Tiempo Final":str(datetime.strptime(str(n_s[4]),ti_formato))}
	return sat_t
	
"""
##############################################################################
##### Batos inicales #########################################################
##############################################################################
"""
#cargando el archivo ruta de las carpeta
ro_prin="./Sat_see" 



ti_formato="%Y/%m/%d %H:%M:%S"
ti_formato2="%Y-%m-%d %H:%M:%S"
####Formato para restar las horas

#Convetimos los timpos a formatos datetime
#ti_final=datetime.strptime(str(seg[4]),ti_formato)
#ti_ini=datetime.strptime(str(seg[0]),ti_formato) 

"""
################################################################################
####################### excepciones propias  #$####################################
""" 


class mine_w(QMainWindow):
	def __init__(self,parent=None):
		QMainWindow.__init__(self,parent)
		self.ui=Ui_MainWindow()
		self.ui.setupUi(self)
		self.Az_al_gra=True
		
		with open(path.join(ro_prin,"Datos_obs.pickle"), "rb") as input_file:
			D_obs=cPickle.load(input_file)

		ob_lis=list(D_obs.keys())

		fic_lug=D_obs[ob_lis[2]]


		with open(fic_lug, "rb") as input_file:
			self.Ob_datos=cPickle.load(input_file)

#cargando los satelites que ya estan guardados 
		sav_sat=path.join("Sat_see","satelites.pickle")
		with open(sav_sat, "rb") as input_file:
			self.sat_v=cPickle.load(input_file)

		self.sat_l=list(self.sat_v.keys())

#cargando el archivo ruta de las carpeta 
		with open(r"satdic.pickle", "rb") as input_file:
			l_url=cPickle.load(input_file)

#t=dat.datetime.utcnow()
		self.d_sat_f=l_url["fecha"]+dat.timedelta(hours=72)
		
		#th=datetime.now()
		#self.h_z=t.hour-th.hour
		""""
		################################################################
		################################################################
		################################################################
		"""
		########### inicializando reloj ###############################
		self.t=dat.datetime.utcnow()
		
#lugar de observacion 
		self.obse=ep.Observer()
		self.obse.name=self.Ob_datos["nombre"]
		self.obse.long=self.Ob_datos["logitud"]
		self.obse.lat=self.Ob_datos["latitud"]
		#use una plicacion
		self.obse.elevation=self.Ob_datos["elevacion"]  #en metros 
		self.obse.date=self.t 
		  #toma fecha y hora ingresada 
		self.rotac=False
		self.Sat_s=dict()
		
		self.sat_lis=[]
		
		for k in self.sat_l:
			fi=self.sat_v[k]
			sat=leertxt(fi)
			self.Sat_s[sat.name]=sat
			self.sat_lis.append(sat.name)

		self.sat_t_s=dict()
		self.sat_t=dict()
		self.seg=dict()
		self.seg["observador"]=[np.rad2deg(self.obse.lon),np.rad2deg(self.obse.lat)] 
		self.li_ti_in=[]
		self.li_ti_fn=[]
		#print self.sat_lis
		for no in self.sat_lis:
			self.Sat_s[no].compute(self.obse)
			if self.Sat_s[no].transit_time!= None:
				n_s=self.obse.next_pass(self.Sat_s[no])
				if n_s[0]==None:
					self.sat_t={"Tiempo Inical":"No encontrado","Tiempo Final":"No encontrado","Duracion":"notiene"}
				else:
					self.sat_t={"Tiempo Inical":str(datetime.strptime(str(n_s[0]),ti_formato)),"Tiempo Final":str(datetime.strptime(str(n_s[4]),ti_formato)),"Duracion":str(datetime.strptime(str(n_s[4]),ti_formato)-datetime.strptime(str(n_s[0]),ti_formato))}
				self.li_ti_in.append(self.sat_t["Tiempo Inical"])
				self.li_ti_fn.append(self.sat_t["Tiempo Final"])
			else: 
				self.sat_t={"Tiempo Inical":"Geo ","Tiempo Final":"Geo","Duracion":"Simepre"}
			ins=self.sat_t["Duracion"].find("-")
			if ins!=-1:
				self.sat_t["Duracion"]="LV"
			self.sat_t_s[no]=self.sat_t
			
			lon=np.rad2deg(self.Sat_s[no].sublong)
			lat=np.rad2deg(self.Sat_s[no].sublat)
			self.seg[no]=[lon,lat]
		
		self.k_data=sorted(list(self.sat_t_s.keys()))
		#se tiene el satelite mas sercano y ordenando los satelites por fecha 
		self.ti_or_in=sorted(self.li_ti_in)
		self.ti_or_fn=sorted(self.li_ti_fn)
		px_in=datetime.strptime(self.ti_or_in[0],ti_formato2)
		px_fn=datetime.strptime(self.ti_or_fn[0],ti_formato2)
		if px_in<px_fn:
			self.next_t=self.ti_or_in[0]
			for no in self.k_data:
				if self.next_t==self.sat_t_s[no]["Tiempo Inical"]:
					self.red=no
			self.next_t=datetime.strptime(self.sat_t_s[self.red]["Tiempo Inical"],ti_formato2)
		else:
			self.next_t=self.ti_or_fn[0]
			for no in self.k_data:
				if self.next_t==self.sat_t_s[no]["Tiempo Final"]:
					self.red=no
			self.next_t=datetime.strptime(self.sat_t_s[self.red]["Tiempo Final"],ti_formato2)
		
		self.ui.Lab_sat_name.setText(self.red)
		########### reloj bigital ######################################
		#self.LCD_2=self.ui.W_Ti_data_zh
		self.LCD=self.ui.W_Ti_data
		#########3 grafica de los satelites 3###########################
		self.webview = Grafica()
		self.la=QVBoxLayout()
		self.la.addWidget(self.webview)
		self.ui.Map_sat.setLayout(self.la)
		#########3 Tabla de los satelites 3#############################
		self.tabla=MyTable(self.sat_t_s)
		self.tabla.set_datatime()
		self.la_ta=QtGui.QGridLayout() 
		self.la_ta.addWidget(self.tabla)
		self.ui.Sat_tab.setLayout(self.la_ta)
		############Acciones para la ventan ############################
		self.ui.actionObservador.triggered.connect(self.ob_datos)
		self.ui.actionReloj.triggered.connect(self.con_reloj)
		self.ui.actionSatelites.triggered.connect(self.sat_datos)
		self.ui.actionRed.triggered.connect(self.red_actz)
		self.ui.actionControl.triggered.connect(self.at_cont)
		self.ui.actionRed_2.triggered.connect(self.at_cont_red)
		self.tabla.cellClicked.connect(self.sat_dt)
		self.tabla.cellDoubleClicked.connect(self.sat_dt)
		self.ui.PB_nex.clicked.connect(self.Grafica_new)
		self.ui.PB_Ruta.clicked.connect(self.Ruta_sat)
		self.ui.PB_Tabla.clicked.connect(self.tab_new)
		################## iniciando taimer ############################
		self.t1=self.t=self.t
		#self.t_re=self.t
		#self.tz=self.t-dat.timedelta(hours=self.h_z)
		self.LCD.setText(str(self.t.strftime("%Y/%m/%d %H:%M:%S")))
		#self.LCD_2.setText(str(self.tz.strftime("%Y/%m/%d %H:%M:%S")))
		self.tex_lati=str(float("{0:.2f}".format(self.seg[self.red][1])))
		self.tex_long=str(float("{0:.2f}".format(self.seg[self.red][0])))
		self.tex_azi=str(float("{0:.2f}".format(np.rad2deg(self.Sat_s[self.red].az))))
		self.tex_ele=str(float("{0:.2f}".format(np.rad2deg(self.Sat_s[self.red].alt))))
		self.tex_dist=str((self.Sat_s[self.red].range/1000))
		self.ui.Lab_lati.setText(self.tex_lati)
		self.ui.Lab_long.setText(self.tex_long)
		self.ui.Lab_azi.setText(self.tex_azi)
		self.ui.Lab_al.setText(self.tex_ele)
		self.ui.label_11.setText(self.tex_dist)
		self.webview.sat_lu(self.seg,self.red,self.t)
		
		
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.sleep)
		self.timer.start(1000)
		

	def sleep(self):
		self.t1=self.t1+dat.timedelta(seconds=1)
		#self.tz=self.t1-dat.timedelta(hours=self.h_z)
		#self.LCD_2.setText(str(self.tz.strftime("%Y/%m/%d %H:%M:%S")))
		self.LCD.setText(str(self.t1.strftime("%Y/%m/%d %H:%M:%S")))
		
		if (self.t1-self.t)>dat.timedelta(seconds=3):
			self.t=self.t1
			#print  "Tiempo guardado"
			self.rec()
			
		if self.t1>self.next_t:
			self.tabla_rec()
			
		if self.t1.date()>self.d_sat_f:
			self.red_actz()
		#try:
			#self.rot_ant.isVisible()
		
		if self.rotac:
			if not(self.rot_ant.isVisible()):
				del(self.rot_ant)
				self.rotac=False
	
	def rec(self):
		#Cargado la nueva ubicasion 
		self.la.removeWidget(self.webview)
		self.tabla.selectedItems()
		self.webview = Grafica()
		self.obse.date=self.t1
		
		for no in self.sat_lis:
			self.Sat_s[no].compute(self.obse)
			lon=np.rad2deg(self.Sat_s[no].sublong)
			lat=np.rad2deg(self.Sat_s[no].sublat)
			self.seg[no]=[lon,lat]
		
		self.tex_lati=str(float("{0:.2f}".format(self.seg[self.red][1])))
		self.tex_long=str(float("{0:.2f}".format(self.seg[self.red][0])))
		self.tex_azi=str(float("{0:.2f}".format(np.rad2deg(self.Sat_s[self.red].az))))
		self.tex_ele=str(float("{0:.2f}".format(np.rad2deg(self.Sat_s[self.red].alt))))
		self.tex_dist=str((self.Sat_s[self.red].range/1000))
		self.ui.Lab_lati.setText(self.tex_lati)
		self.ui.Lab_long.setText(self.tex_long)
		self.ui.Lab_azi.setText(self.tex_azi)
		self.ui.Lab_al.setText(self.tex_ele)
		self.ui.label_11.setText(self.tex_dist)
		#colocando la grafica 
		self.webview.sat_lu(self.seg,self.red,self.t1)
		self.la.addWidget(self.webview)
		self.ui.Map_sat.setLayout(self.la)
	
	
	def tabla_rec(self):
		self.obse.date=self.t1
		self.li_ti_in=[]
		self.li_ti_fn=[]
		self.la_ta.removeWidget(self.tabla)
		for no in self.sat_lis:
			if self.Sat_s[no].transit_time!= None:
				n_s=self.obse.next_pass(self.Sat_s[no])
				if n_s[0]==None:
					self.sat_t={"Tiempo Inical":"No encontrado","Tiempo Final":"No encontrado","Duracion":"notiene"}
				else:
					self.sat_t={"Tiempo Inical":str(datetime.strptime(str(n_s[0]),ti_formato)),"Tiempo Final":str(datetime.strptime(str(n_s[4]),ti_formato)),"Duracion":str(datetime.strptime(str(n_s[4]),ti_formato)-datetime.strptime(str(n_s[0]),ti_formato))}
				self.li_ti_in.append(self.sat_t["Tiempo Inical"])
				self.li_ti_fn.append(self.sat_t["Tiempo Final"])
			else: 
				self.sat_t={"Tiempo Inical":"Geo ","Tiempo Final":"Geo","Duracion":"Simepre"}
				
			ins=self.sat_t["Duracion"].find("-")
			if ins!=-1:
				self.sat_t["Duracion"]="LV"
			self.sat_t_s[no]=self.sat_t
		
		self.k_data=sorted(list(self.sat_t_s.keys()))
		#se tiene el satelite mas sercano y ordenando los satelites por fecha 
		self.ti_or_in=sorted(self.li_ti_in)
		self.ti_or_fn=sorted(self.li_ti_fn)
		px_in=datetime.strptime(self.ti_or_in[0],ti_formato2)
		px_fn=datetime.strptime(self.ti_or_fn[0],ti_formato2)
		if px_in<px_fn:
			self.next_t=self.ti_or_in[0]
			for no in self.k_data:
				if self.next_t==self.sat_t_s[no]["Tiempo Inical"]:
					self.red=no
			self.next_t=datetime.strptime(self.sat_t_s[self.red]["Tiempo Inical"],ti_formato2)
		else:
			self.next_t=self.ti_or_fn[0]
			for no in self.k_data:
				if self.next_t==self.sat_t_s[no]["Tiempo Final"]:
					self.red=no
			self.next_t=datetime.strptime(self.sat_t_s[self.red]["Tiempo Final"],ti_formato2)

		#agregando la tabla
		self.tabla=MyTable(self.sat_t_s) 
		self.tabla.set_datatime()
		self.la_ta.addWidget(self.tabla)
		self.ui.Sat_tab.setLayout(self.la_ta)
		
		self.t1=dat.datetime.utcnow()
		#self.tz=self.t1-dat.timedelta(hours=self.h_z)
		#self.LCD_2.setText(str(self.tz.strftime("%Y/%m/%d %H:%M:%S")))
		self.LCD.setText(str(self.t1.strftime("%Y/%m/%d %H:%M:%S")))
		
	def sat_dt(self):
		self.it_row=self.tabla.currentRow()
		self.item_ta=self.tabla.item(self.it_row,0)
		self.red=str(self.item_ta.text())
		self.ui.Lab_sat_name.setText(self.red)
		
		if self.Sat_s[self.red].transit_time==None:
			self.ui.PB_Ruta.setEnabled(False)
			self.ui.PB_Tabla.setEnabled(False)
			self.ui.PB_nex.setEnabled(False)
		else:
			self.ui.PB_Ruta.setEnabled(True)
			self.ui.PB_Tabla.setEnabled(True)
			self.ui.PB_nex.setEnabled(True)
			
		#if self.sat_t_s[self.red]["Duracion"]=="LV":
			#self.ui.PB_Ruta.setEnabled(False)
			#self.ui.PB_Tabla.setEnabled(False)
			#self.ui.PB_nex.setEnabled(False)
		#else:
			#self.ui.PB_Ruta.setEnabled(True)
			#self.ui.PB_Tabla.setEnabled(True)
			#self.ui.PB_nex.setEnabled(True)
			
		self.rec()



	""" Codigo para llamar a los demas programas de el menu pricipal """
	def ob_datos(self):
		## improtando los datos de la estacion 
		from add_datos_llama import add_ant
		self.dat_obse=add_ant()
		#Datos del archivo donde se guarada 
		with open(path.join(ro_prin,"Datos_obs.pickle"), "rb") as input_file:
			D_obs=cPickle.load(input_file)
			
		ob_lis=list(D_obs.keys())
		
		fic_lug=D_obs[ob_lis[2]]
		

		#Datos de lugar de observador 
		with open(fic_lug, "rb") as input_file:
			Ob_datos=cPickle.load(input_file)
			
		self.dat_obse.ui.spinBox.setValue(Ob_datos['elevacion'])
		self.dat_obse.ui.observ_lad.setText(Ob_datos["latitud"])
		self.dat_obse.ui.observ_lod.setText(Ob_datos["logitud"])
		self.dat_obse.ui.observ_ubi.setText(Ob_datos["nombre"])
		self.dat_obse.ui.observ_at.setText(D_obs["nom"])
		self.dat_obse.ui.observ_des.setText(D_obs["desc"])
		
		self.la.removeWidget(self.webview)
		self.webview = Grafica()
		
		
		self.la_ta.removeWidget(self.tabla)
		
		self.dat_obse.show()
		self.dat_obse.ui.pb_G.clicked.connect(self.sat_reloa_sat)



	def red_actz(self):
		## importando el programa para actualizar 
		from descarga import sat_dwload 
		self.des=sat_dwload(self.t1.date())
		self.des.show()
		#self.des.ui.PB_Ac.click()
		self.des.ui.PB_Ac.clicked.connect(self.sat_reloa_sat)
	
	def sat_datos(self):
		## importado los taselites 
		from lersat_p import sat_datos
		self.la.removeWidget(self.webview)
		self.webview = Grafica()
		
		
		
		self.la_ta.removeWidget(self.tabla)
		self.li_sat=sat_datos(self.obse)
		self.li_sat.show() 
		self.li_sat.ui.pb_G.clicked.connect(self.sat_reloa_sat)
	
	def con_reloj(self):
		from Reloj_toma import Reloj_set 
		self.timer=Reloj_set()
		self.timer.show()
		self.timer.PB_SNTP.clicked.connect(self.reloj_load)
		self.timer.PB_RM.clicked.connect(self.reloj_load)
	
	def reloj_load(self):
		self.t=self.t1=self.timer.impre_timer()
		self.recalc()
	
	def at_cont(self):
		from rot_w_call import Rot_ant
		self.rot_ant=Rot_ant(self.Sat_s,self.t1,self.obse)
		self.rot_ant.show()
		self.rotac=True
		
	def at_cont_red(self):
		from rot_w_call_red import Rot_ant_red
		self.rot_ant=Rot_ant_red(self.Sat_s,self.t1,self.obse)
		self.rot_ant.show()
		self.rotac=True
		
####### Recargado los datos de los satelites ########################### 
		
	def recalc(self):
		self.la.removeWidget(self.webview)
		self.tabla.selectedItems()
		
		self.webview = Grafica()
		self.obse.date=self.t1
		
		self.LCD.setText(str(self.t1.strftime("%Y/%m/%d %H:%M:%S")))
		
		self.la_ta.removeWidget(self.tabla)
		self.obse.date=self.t 
		  #toma fecha y hora ingresada 

		self.sat_t_s=dict()
		self.sat_t=dict()
		self.seg=dict()
		self.seg["observador"]=[np.rad2deg(self.obse.lon),np.rad2deg(self.obse.lat)] 
		self.li_ti_in=[]
		self.li_ti_fn=[]
		#print self.sat_lis
		for no in self.sat_lis:
			self.Sat_s[no].compute(self.obse)
			if self.Sat_s[no].transit_time!= None:
				n_s=self.obse.next_pass(self.Sat_s[no])
				if n_s[0]==None:
					self.sat_t={"Tiempo Inical":"No encontrado","Tiempo Final":"No encontrado","Duracion":"notiene"}
				else:
					self.sat_t={"Tiempo Inical":str(datetime.strptime(str(n_s[0]),ti_formato)),"Tiempo Final":str(datetime.strptime(str(n_s[4]),ti_formato)),"Duracion":str(datetime.strptime(str(n_s[4]),ti_formato)-datetime.strptime(str(n_s[0]),ti_formato))}
				self.li_ti_in.append(self.sat_t["Tiempo Inical"])
				self.li_ti_fn.append(self.sat_t["Tiempo Final"])
			else: 
				self.sat_t={"Tiempo Inical":"Geo ","Tiempo Final":"Geo","Duracion":"Simepre"}
			
			ins=self.sat_t["Duracion"].find("-")
			if ins!=-1:
				self.sat_t["Duracion"]="LV"
			self.sat_t_s[no]=self.sat_t
			lon=np.rad2deg(self.Sat_s[no].sublong)
			lat=np.rad2deg(self.Sat_s[no].sublat)
			self.seg[no]=[lon,lat]
		
		self.k_data=sorted(list(self.sat_t_s.keys()))
#se tiene el satelite mas sercano y ordenando los satelites por fecha 
		self.ti_or_in=sorted(self.li_ti_in)
		self.ti_or_fn=sorted(self.li_ti_fn)
		px_in=datetime.strptime(self.ti_or_in[0],ti_formato2)
		px_fn=datetime.strptime(self.ti_or_fn[0],ti_formato2)
		if px_in<px_fn:
			self.next_t=self.ti_or_in[0]
			for no in self.k_data:
				if self.next_t==self.sat_t_s[no]["Tiempo Inical"]:
					self.red=no
			self.next_t=datetime.strptime(self.sat_t_s[self.red]["Tiempo Inical"],ti_formato2)
		else:
			self.next_t=self.ti_or_fn[0]
			for no in self.k_data:
				if self.next_t==self.sat_t_s[no]["Tiempo Final"]:
					self.red=no
			self.next_t=datetime.strptime(self.sat_t_s[self.red]["Tiempo Final"],ti_formato2)
			
		#$$$$  nueva tabla y grafica $$$$#
		self.tabla=MyTable(self.sat_t_s) 
		self.tabla.set_datatime()
		self.la_ta.addWidget(self.tabla)
		self.ui.Sat_tab.setLayout(self.la_ta)
		
		self.tabla.cellClicked.connect(self.sat_dt)
		self.tabla.cellDoubleClicked.connect(self.sat_dt)
		
		self.webview.sat_lu(self.seg,self.red,self.t1)
		self.la.addWidget(self.webview)
		self.ui.Map_sat.setLayout(self.la)
		
		
	def sat_reloa_sat(self):
		self.tabla.selectedItems()
		self.t1=dat.datetime.utcnow()
		## insetan los timepos ##
		
		with open(r"satdic.pickle", "rb") as input_file:
			l_url=cPickle.load(input_file)

#t=dat.datetime.utcnow()
		self.d_sat_f=l_url["fecha"]+dat.timedelta(hours=72)
		
		#self.tz=self.t1-dat.timedelta(hours=self.h_z)
		#self.LCD_2.setText(str(self.tz.strftime("%Y/%m/%d %H:%M:%S")))
		self.LCD.setText(str(self.t1.strftime("%Y/%m/%d %H:%M:%S")))

		with open(path.join(ro_prin,"Datos_obs.pickle"), "rb") as input_file:
			D_obs=cPickle.load(input_file)

		ob_lis=list(D_obs.keys())
		
		fic_lug=D_obs[ob_lis[2]]
		print fic_lug
		#Datos de lugar de observador 
		with open(fic_lug, "rb") as input_file:
			self.Ob_datos=cPickle.load(input_file)
			
		#cargando los satelites que ya estan guardados 
		sav_sat=path.join("Sat_see","satelites.pickle")
		
		with open(sav_sat, "rb") as input_file:
			self.sat_v=cPickle.load(input_file)
		
		self.sat_l=list(self.sat_v.keys())

		self.Sat_s=dict()
		self.sat_lis=[]
		
		for k in self.sat_l:
			fi=self.sat_v[k]
			sat=leertxt(fi)
			self.Sat_s[sat.name]=sat
			self.sat_lis.append(sat.name)
		
		self.Az_al_gra=True

		self.sat_t_s=dict()
		self.sat_t=dict()
		self.seg=dict()
		######################### Se retoma toda la informacion ######################
		
		self.obse=ep.Observer()
		self.obse.name=self.Ob_datos["nombre"]
		self.obse.long=self.Ob_datos["logitud"]
		self.obse.lat=self.Ob_datos["latitud"]
		
		#use una plicacion
		self.obse.elevation=self.Ob_datos["elevacion"] 
		self.seg["observador"]=[np.rad2deg(self.obse.lon),np.rad2deg(self.obse.lat)] 
		#print self.seg["observador"]
		self.li_ti_in=[]
		self.li_ti_fn=[]
		for no in self.sat_lis:
			self.Sat_s[no].compute(self.obse)
			if self.Sat_s[no].transit_time!= None:
				n_s=self.obse.next_pass(self.Sat_s[no])
				if n_s[0]==None:
					self.sat_t={"Tiempo Inical":"No encontrado","Tiempo Final":"No encontrado","Duracion":"notiene"}
				else:
					self.sat_t={"Tiempo Inical":str(datetime.strptime(str(n_s[0]),ti_formato)),"Tiempo Final":str(datetime.strptime(str(n_s[4]),ti_formato)),"Duracion":str(datetime.strptime(str(n_s[4]),ti_formato)-datetime.strptime(str(n_s[0]),ti_formato))}
				self.li_ti_in.append(self.sat_t["Tiempo Inical"])
				self.li_ti_fn.append(self.sat_t["Tiempo Final"])
			else: 
				self.sat_t={"Tiempo Inical":"Geo ","Tiempo Final":"Geo","Duracion":"Simepre"}
			
			ins=self.sat_t["Duracion"].find("-")
			if ins!=-1:
				self.sat_t["Duracion"]="LV"
			self.sat_t_s[no]=self.sat_t
			lon=np.rad2deg(self.Sat_s[no].sublong)
			lat=np.rad2deg(self.Sat_s[no].sublat)
			self.seg[no]=[lon,lat]
		self.k_data=sorted(list(self.sat_t_s.keys()))
		#se tiene el satelite mas sercano y ordenando los satelites por fecha 
		self.ti_or_in=sorted(self.li_ti_in)
		self.ti_or_fn=sorted(self.li_ti_fn)
		px_in=datetime.strptime(self.ti_or_in[0],ti_formato2)
		px_fn=datetime.strptime(self.ti_or_fn[0],ti_formato2)
		if px_in<px_fn:
			self.next_t=self.ti_or_in[0]
			for no in self.k_data:
				if self.next_t==self.sat_t_s[no]["Tiempo Inical"]:
					self.red=no
			self.next_t=datetime.strptime(self.sat_t_s[self.red]["Tiempo Inical"],ti_formato2)
		else:
			self.next_t=self.ti_or_fn[0]
			for no in self.k_data:
				if self.next_t==self.sat_t_s[no]["Tiempo Final"]:
					self.red=no
			self.next_t=datetime.strptime(self.sat_t_s[self.red]["Tiempo Final"],ti_formato2)

		
		#$$$$  nueva tabla y grafica $$$$#
		self.tabla=MyTable(self.sat_t_s) 
		self.tabla.set_datatime()
		self.la_ta.addWidget(self.tabla)
		self.ui.Sat_tab.setLayout(self.la_ta)
		
		self.tabla.cellClicked.connect(self.sat_dt)
		self.tabla.cellDoubleClicked.connect(self.sat_dt)
		
		self.webview.sat_lu(self.seg,self.red,self.t1)
		self.la.addWidget(self.webview)
		self.ui.Map_sat.setLayout(self.la)
		
	
	"""Codigo para mostrasr los resultado de un satlite  """
	def Grafica_new(self):
		self.ven_nom="Grafica de los angulos del satelite:"+self.red
		if self.Az_al_gra==True:
			self.red_s=self.red
			if self.sat_t_s[self.red]["Duracion"]=="LV":
				self.sat_t_v=tiempo_ajuste(self.obse,self.Sat_s[self.red])
			else:
				self.sat_t_v=self.sat_t_s[self.red]
			self.dat_azal=dat_antena(self.obse,self.Sat_s[self.red],self.sat_t_v)
			self.red_date=datetime.strptime(self.sat_t_s[self.red]["Tiempo Final"],ti_formato2)
			
			self.plot=Gra_azal(self.dat_azal)
			self.plot.plot()
			self.Az_al_gra=False
		else:
			if self.red_s==self.red:
				if self.red_date<self.t1:
					print 1
					self.dat_azal=dat_antena(self.obse,self.Sat_s[self.red],self.sat_t_s[self.red])
					
					self.plot=Gra_azal(self.dat_azal)
					self.plot.plot()
				else:
					self.plot.plot()
					
			else:
				if self.sat_t_s[self.red]["Duracion"]=="LV":
					self.sat_t_v=tiempo_ajuste(self.obse,self.Sat_s[self.red])
				else:
					self.sat_t_v=self.sat_t_s[self.red]
				self.dat_azal=dat_antena(self.obse,self.Sat_s[self.red],self.sat_t_v)
				
				self.plot=Gra_azal(self.dat_azal)
				self.plot.plot()
			
		self.dic_ur="file:///home/cidte/programas de python/Ejercicio de Python/partes del codigo/az_alt_gra.html"
		
		self.az_la_G=QT_url(self.dic_ur,w=530,h=450,nom=self.ven_nom)
		self.az_la_G.show()

		
	def Ruta_sat(self):
		self.ven_nom="Ruta del satelite:"+self.red
		if self.Az_al_gra==True:
			self.red_s=self.red
			if self.sat_t_s[self.red]["Duracion"]=="LV":
				self.sat_t_v=tiempo_ajuste(self.obse,self.Sat_s[self.red])
			else:
				self.sat_t_v=self.sat_t_s[self.red]
			self.dat_azal=dat_antena(self.obse,self.Sat_s[self.red],self.sat_t_v)
			self.red_date=datetime.strptime(self.sat_t_s[self.red]["Tiempo Final"],ti_formato2)
			
			self.plot_r=ruta_sat(self.Ob_datos,self.dat_azal,self.red)
			self.Az_al_gra=False
		else:
			if self.red_s==self.red:
				if self.red_date<self.t1:
					
					self.dat_azal=dat_antena(self.obse,self.Sat_s[self.red],self.sat_t_s[self.red])
					
					self.plot=ruta_sat(self.Ob_datos,self.dat_azal,self.red)
				else:
					self.plot_r=ruta_sat(self.Ob_datos,self.dat_azal,self.red)
			else:
				if self.sat_t_s[self.red]["Duracion"]=="LV":
					self.sat_t_v=tiempo_ajuste(self.obse,self.Sat_s[self.red])
				else:
					self.sat_t_v=self.sat_t_s[self.red]
				self.dat_azal=dat_antena(self.obse,self.Sat_s[self.red],self.sat_t_v)
				self.t1=dat.datetime.utcnow() 
				self.plot_r=ruta_sat(self.Ob_datos,self.dat_azal,self.red)
			
		
		self.dic_ur="file:///home/cidte/programas de python/Ejercicio de Python/partes del codigo/map.html"
		
		self.az_la_R=QT_url(self.dic_ur,w=1200,h=500,nom=self.ven_nom)
		self.az_la_R.show()
	
	def tab_new(self):
		self.ven_nom="Tabla de los angulos del satelite:"+self.red
		if self.Az_al_gra==True:
			self.red_s=self.red
			if self.sat_t_s[self.red]["Duracion"]=="LV":
				self.sat_t_v=tiempo_ajuste(self.obse,self.Sat_s[self.red])
			else:
				self.sat_t_v=self.sat_t_s[self.red]
			self.dat_azal=dat_antena(self.obse,self.Sat_s[self.red],self.sat_t_v)
			self.red_date=datetime.strptime(self.sat_t_s[self.red]["Tiempo Final"],ti_formato2)
			
			self.Az_al_gra=False
			self.plot=Gra_azal(self.dat_azal)
			self.plot.tabular()
		else:
			if self.red_s==self.red:
				if self.red_date<self.t1:
					
					self.dat_azal=dat_antena(self.obse,self.Sat_s[self.red],self.sat_t_s[self.red])
					self.t1=dat.datetime.utcnow()
					self.plot=Gra_azal(self.dat_azal)
					self.plot.tabular()
				else:
					self.plot.tabular()
			
			else:
				if self.sat_t_s[self.red]["Duracion"]=="LV":
					self.sat_t_v=tiempo_ajuste(self.obse,self.Sat_s[self.red])
				else:
					self.sat_t_v=self.sat_t_s[self.red]
				self.dat_azal=dat_antena(self.obse,self.Sat_s[self.red],self.sat_t_v)
				
				self.plot=Gra_azal(self.dat_azal)
				self.plot.tabular()
			
		
		self.dic_ur="file:///home/cidte/programas de python/Ejercicio de Python/partes del codigo/data_table.html"
		
		self.az_la_T=QT_url(self.dic_ur,w=530,h=450,nom=self.ven_nom)
		self.az_la_T.show()




app = QtGui.QApplication(sys.argv)
minWin=mine_w()
minWin.show()
app.exec_()


