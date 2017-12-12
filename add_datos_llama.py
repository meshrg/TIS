#!/usr/bin/python
# -*- coding: utf-8 -*-

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
for x in citis:
	lis.append(x.split(".")[0])

#ventana prinvipal 
class add_ant(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.ui.pb_lep.clicked.connect(self.lista_click)
		self.ui.pb_G.clicked.connect(self.guardar_click)
		self.ui.pb_C.clicked.connect(self.close)
		self.ui.pb_py.clicked.connect(self.ubica)
		self.setWindowTitle(u"Captura de datos del observador")
		
	def lista_click(self):
		self.l=lista()
		self.l.show()
		self.l.ui.PB_A.clicked.connect(self.cargar)
		self.l.ui.lis_obs.itemDoubleClicked.connect(self.cargar)
		
	def ubica(self):
		self.u=pygeoDi()
		self.u.show()
		self.u.ui.PB_A.clicked.connect(self.cargar_ll_2)
		
	def guardar_click(self):
		#Datos del observador 
		l_obs=dict()
		self.obs= str(self.ui.observ_at.toPlainText())
		
		self.dec= str(self.ui.observ_des.toPlainText())
		
		self.ub = str(self.ui.observ_ubi.toPlainText())
		
		self.lat = str(self.ui.observ_lad.toPlainText())
		
		self.lon = str(self.ui.observ_lod.toPlainText())
		
		self.alt=self.ui.spinBox.value()
		#convetimo el obsevador un dicionario
		
		l_obs["elevacion"]=self.alt  #en metros
		l_obs['latitud']=self.lat
		l_obs["logitud"]=self.lon
		l_obs["nombre"]=self.ub
		
		fichero=path.join("observa",l_obs["nombre"])
		if not(l_obs["nombre"] in lis):
			fichero=path.join("observa",l_obs["nombre"])
		#Guardando el obsevador 
			with open(fichero + ".pickle", "wb") as output_file:
				cPickle.dump(l_obs, output_file)
			
		D_obs={'nom':self.obs, 'desc':self.dec ,'lug':fichero+ ".pickle"}
		fiche=path.join("Sat_see","Datos_obs")
		#r"Sat_see/Datos_obs.pickle"
		with open(fiche + ".pickle", "wb") as output_file:
			cPickle.dump(D_obs, output_file)
		
		
		self.close()
		return D_obs #regresa los datos del observador 
		
	def cargar(self):
		self.po=self.l.Aceptar_click()
		self.l.close() #Cierra la ventana de lista. 
		#Carga los datos de la ubicacion.
		with open(path.join("observa",(self.po+".pickle")),"rb") as input_file:
			l_obs=cPickle.load(input_file)
		
		self.ui.observ_ubi.setText(self.po)
		self.ui.observ_lad.setText(l_obs['latitud'])
		self.ui.spinBox.setValue(l_obs['elevacion'])
		self.ui.observ_lod.setText(l_obs['logitud'])
		
	def cargar_ll_2(self):
		self.ut=self.u.cargar_datos()
		self.u.close() 
		self.ui.observ_lad.setText(str(self.ut[0]))
		self.ui.observ_lod.setText(str(self.ut[1]))



 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = add_ant()
    myapp.show()
    sys.exit(app.exec_())


