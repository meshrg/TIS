#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from  download import *
import sys
import urllib2
from bs4 import BeautifulSoup
import requests

import ntplib as ntp
import datetime
from datetime import datetime
import time
#guarda en una carpeta espesifico sa txt
from os import path
import os
import cPickle

url = "http://celestrak.com/NORAD/elements/"
#solo el 


#tiempo 
x = ntp.NTPClient()
c=x.request("mx.pool.ntp.org",version=4,timeout=5)
t=datetime.utcfromtimestamp(c.recv_time)
da=datetime.date(t)

req = requests.get(url)

html = BeautifulSoup(req.text, "lxml")

with open(r"satdic.pickle", "rb") as input_file:
	l_u=cPickle.load(input_file)


#Fecha que muestra la pagina 
for i in html.find_all('h2',{'align':'CENTER'}):
	daCT=i.getText()
	#print i.getText()


l_url=dict()
l_urlts=dict()



class sat_dwload(QtGui.QDialog):
	def __init__(self,Fe,parent=None):
		QtGui.QWidget.__init__(self,parent)
		self.ui=Ui_Form()
		self.da=Fe
		#print self.da 
		self.ui.setupUi(self)
		self.ui.Prog_B.setValue(0)
		self.ui.PB_Ac.clicked.connect(self.des)
		#descarga=urllib2.urlopen(url)
		self.setWindowTitle(u"Actualización de base de datos")

		#headers = descarga.info()
		#self.ui.Prog_B.valueChanged.connect(self.uno)
		#self.fecha()
		
	#def fecha(self):
		#self.fe_p=l_u['fecha']
		#if self.fe_p==da:
			#self.ui.PB_Ac.setEnabled(False)
		#else:
			#self.ui.PB_Ac.setEnabled(True)
		
	def des(self):
		self.pro=0
		self.ui.label.setText("Descargando")
		for i in html.find_all('td',{'align':'CENTER'}):
			self.aum=2.43902439
			for j in i.find_all('a'):
				#print"%s : http://celestrak.com/NORAD/elements/%s" %(j.text, j.get("href").replace(" ", "%20"))
				if j.get("href") == "/webmaster.asp" :
					break
				url3= "http://celestrak.com/NORAD/elements/"+j.get("href").replace(" ", "%20")
				self.ui.txt_out.setText(j.text)
				descarga=urllib2.urlopen(url3)
				l1=descarga.readline()
				tipo=j.get("href")
				ti=tipo.split(".")
				#comprueva si la ruta exite
				car=path.join("sat tle",ti[0])
				if not(os.path.exists(car)):
					os.mkdir(path.join("sat tle",ti[0]))
				numero=00
				while l1:
					nom="sat"+ str(numero)
					l2=descarga.readline()
					l3=descarga.readline()
					fiche=path.join("sat tle",ti[0],nom)
					arch=open(fiche,'w')
					arch.writelines([l1,l2,l3])
					arch.close()
					l_url[l1.rstrip()]=fiche
					l1=descarga.readline()
					numero=numero+1
				l_urlts[j.text]=car
				self.pro=self.pro+self.aum
				self.ui.Prog_B.setValue(self.pro)
		while self.pro<101:
			self.pro+=0.01
			self.ui.Prog_B.setValue(self.pro)
		
			
		l_url["fecha"]=self.da
		#Direciones de los satelites 
		with open(r"satdic.pickle", "wb") as output_file:
			cPickle.dump(l_url, output_file)
		#direciiones de las carpetoas con los satelites
		with open(r"tipsatdic.pickle", "wb") as output_file:
			cPickle.dump(l_urlts, output_file)
		self.ui.label.setText("Descargado")
		self.close()




 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = sat_dwload(da)
    myapp.show()
    app.exec_()





