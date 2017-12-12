#!/usr/bin/python
# -*- coding: UTF-8 -*-


import ephem as ep

import time as ti
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from  lis_observa import *

import sys
from PyQt4 import QtGui, QtCore
import os 
from os import path
from datetime import datetime
import datetime as dat
import numpy as np

import cPickle
import pickle
from sat_dato import *


#improtado los satelites 
"""funcion encargada  leer un arcivo .txt y nos devuelve un dicionaros 
con objetos que representan los satelites.
"""
ro_prin="./Sat_see" 


def leertxt(nomdre):
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
		# observador 

def leer_sat(nomdre):
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


with open(path.join(ro_prin,"Datos_obs.pickle"), "rb") as input_file:
	D_obs=cPickle.load(input_file)

ob_lis=list(D_obs.keys())

fic_lug=D_obs[ob_lis[2]]


with open(fic_lug, "rb") as input_file:
	Ob_datos=cPickle.load(input_file)



""""
################################################################
################################################################
################################################################
"""

########### inicializando reloj ###############################
#lugar de observacion 
obse=ep.Observer()
obse.name=Ob_datos["nombre"]
obse.long=Ob_datos["logitud"]
obse.lat=Ob_datos["latitud"]
#use una plicacion
obse.elevation=Ob_datos["elevacion"]  #en metros 
obse.date=dat.datetime.utcnow()


#for k in lis_tipos.keys():
	#print("clave={0}".format(k))
#print lis_tipos


sat_v=dict()
#classe que define la vneta pricipal 
class sat_datos(QtGui.QDialog):
	def __init__(self,obser,parent=None):
		QtGui.QWidget.__init__(self, parent)
		
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		#cargando los satelites que ya estan guardados 
		self.sav_sat=path.join("Sat_see","satelites.pickle")
		with open(self.sav_sat, "rb") as input_file:
			sat_vg=cPickle.load(input_file)

		#cargando el archivo ruta de las carpeta 
		with open(r"satdic.pickle", "rb") as input_file:
			self.l_url=cPickle.load(input_file)
	
		with open(r"tipsatdic.pickle", "rb") as input_file:
			l_urlts=cPickle.load(input_file)
		
		self.lis2=list(sat_vg.keys())
		self.ob=obser
		#claves de todos los satelites
		gru=[]
		for k in self.l_url.keys():
			#print("clave={0}".format(k))
			#print l_url[k]
			#Direcion de todos los satlites
			gru.append(k)
		
		gru.remove('fecha')
		
		#Diccionario con diccionario  con los satelites en forma de objetos de los objetos  
		l_sat=dict()
		self.oj_sat=dict()
		#para tomar los archivos de la carpeta 
		for l in gru:
			#fi=path.join("sa txt",l)
			fi=self.l_url.get(l)
			sat=leertxt(fi)
			sat_2=leer_sat(fi)
			l_sat[l]=sat
			self.oj_sat[l]=sat_2#todos los satelites 
		
		#lista de todos los satlite
		self.l_sat_all=list(l_sat.keys())
		
		#lista de los tipo de satlites 
		self.l_tipos=list(l_urlts.keys())
		
		#print tip_lis
		#print(lis)
		#print(type(lis))
		
		#Agrupando los satelites en una clasificacion 
		self.lis_tipos=dict()
		l=[]
		l2=0
		for k2 in self.l_tipos:
			tipo=l_urlts.get(k2)
			#print tipo 
			#pala=tipo.split("/")
			for k1 in gru:
				satl=self.l_url.get(k1)
				#print satl
				if tipo in satl:
					l.append(k1)
					
			self.lis_tipos[k2]=l
			l=[]
				

		self.ui.CB_Gsat.addItem("Todos")
		self.add_items()
		self.setWindowTitle(u"Selección de satélite")
		self.ui.pb_C.clicked.connect(self.close)
		self.ui.pb_G.clicked.connect(self.save_sat)
		self.ui.PB_Save.clicked.connect(self.m_sat)
		self.ui.PB_clear.clicked.connect(self.b_s)
		self.ui.CB_Gsat.activated.connect(self.lis)
		self.ui.TE_B.cursorPositionChanged.connect(self.bus)
		self.ui.PB_fin.clicked.connect(self.sat_see)
		
		
	def add_items(self):
		for item_text in self.l_sat_all:
			if not(item_text in self.lis2):
				self.ui.sat_G.addItem(item_text)
		
		for it_text in self.l_tipos:
			self.ui.CB_Gsat.addItem(it_text)
		for item_t in self.lis2:
			self.ui.sat_See.addItem(item_t)
		
	
	def m_sat(self):
		#Optiene el nombre de la lista lo borra y lo 
		#coloca en la segundalista.
		self.ir=self.ui.sat_G.currentRow()
		self.mi=self.ui.sat_G.takeItem(self.ir)
		self.ui.sat_See.addItem(self.mi)
		
	def b_s(self):
		self.ir=self.ui.sat_See.currentRow()
		self.mi=self.ui.sat_See.takeItem(self.ir)
		self.ui.sat_G.addItem(self.mi)
		
		
	def sat_see(self):
		nsee_sat=[]
		sel2=[]
		#Buscanod satelites en linea de vista 
		for nom in self.l_sat_all:
			self.oj_sat[nom].compute(self.ob)
			if self.oj_sat[nom].transit_time==None:
				sel2.append("uno")
				#print nom
			el=np.rad2deg(self.oj_sat[nom].alt)
			#print el
			if el>0:
				nsee_sat.append(nom)
				
		#print len(nsee_sat)
		#print len(sel2)
		for l in range(self.ui.sat_G.count()):
			self.ui.sat_G.setItemHidden(self.ui.sat_G.item(l),True)
		#Montrado la lista 
		for s  in nsee_sat:
			for en in range(self.ui.sat_G.count()):
				self.it=self.ui.sat_G.item(en)
				if str(self.it.text()) == s:
					self.it.setHidden(False)
		
	def lis(self):
		self.no=self.ui.CB_Gsat.currentText()
		#hocutar los valores 
		for l in range(self.ui.sat_G.count()):
			self.ui.sat_G.setItemHidden(self.ui.sat_G.item(l),True)
			#mostrando los necesarios 
		if self.no.__str__()=="todos":
			for l in range(self.ui.sat_G.count()):
				self.ui.sat_G.setItemHidden(self.ui.sat_G.item(l),False)
		else:
			self.loc=self.lis_tipos.get(self.no.__str__())
			#Monstramos lista de los tipos de satelites 
			for s  in self.loc:
				for en in range(self.ui.sat_G.count()):
					self.it=self.ui.sat_G.item(en)
					if str(self.it.text()) == s:
						self.it.setHidden(False)
		self.ui.TE_B.cursorPositionChanged.connect(self.bus)
		
	def bus(self):
		self.bus=self.ui.TE_B.toPlainText()
		#hocultar los valores 
		for l in range(self.ui.sat_G.count()):
			self.ui.sat_G.setItemHidden(self.ui.sat_G.item(l),True)
		#mostrar los valores 
		if self.bus=="":
			for l in range(self.ui.sat_G.count()):
				self.ui.sat_G.setItemHidden(self.ui.sat_G.item(l),False)
		else:
			self.loc=self.ui.sat_G.findItems(self.bus,QtCore.Qt.MatchStartsWith)
			for s  in self.loc:
				self.ui.sat_G.addItem(s)
				self.ui.sat_G.setItemHidden(s,False)
		
	def save_sat(self):
		sat_v=dict()
		sat_G=[]
		for l in range (self.ui.sat_See.count()):
			self.it=self.ui.sat_See.item(l)
			#pasamos str y guadandolos en una lista 
			self.x=str(self.it.text())
			sat_G.append(self.x)
			#Guardndo las direciones de los archivos en un dicionario 
		for k1 in sat_G:
			sat_v[k1]=self.l_url.get(k1)
			#guardado el dicionario
		with open(self.sav_sat, "wb") as output_file:
			cPickle.dump(sat_v, output_file)
			
		self.close()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = sat_datos(obse)
    myapp.show()
    app.exec_()


#print(sat)
#print(ep.degrees(obs.lat))
