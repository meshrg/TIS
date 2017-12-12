#!/usr/bin/python
# -*- coding: utf-8 -*-

#preva de la grafica con el widget 
#ISS 
import ephem as ep
import time  as ti
import datetime 
import math 

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from PyQt4.QtWebKit import QWebView
#import pylab as plt
from datetime import datetime
import datetime as dat

#liberia de los graficos
#from bokeh.plotting import figure
#from bokeh.models import LinearAxis, Range1d,HoverTool
from bokeh.plotting import figure


#from bokeh.io import output_file, show,save
from bokeh.models import (Select,ColumnDataSource,DataRange1d, Select, HoverTool,LinearAxis, Range1d)
from bokeh.models.widgets import Panel, Tabs

from bokeh.io import output_file, show,save
from bokeh.models import Select,ColumnDataSource, Circle, DataRange1d, Select, HoverTool,LinearAxis, Range1d, HoverTool
from bokeh.models.widgets import Panel, Tabs, DataTable, DateFormatter, TableColumn,NumberFormatter
from bokeh.layouts import widgetbox

import yaml 
from os import path
import os
import os.path


class Gra_azal():
	def __init__(self,archivo):
		rut="Sat_datos"
		gra_dic=archivo
		self.raiz=os.getcwd()
		self.sa="htm"
		self.source=ColumnDataSource(
			data=dict(
				x=gra_dic["Escal_time"],
				al=gra_dic["ant_alt"],
				az=gra_dic["ant_az"],
				lon=gra_dic["longitud"],
				lati=gra_dic["latitud"],
				t=gra_dic["Tiempo"]
				)
			)

#show(curdoc) 

	def plot(self):
		os.chdir(self.sa)
		hover1 = HoverTool(
				tooltips=[
					("Grados", "$y"),
					("Tiempo", "@t"),
				]
			)

		hover2 = HoverTool(
				tooltips=[
					("Grados", "$y"),
					("Tiempo", "@t"),
				]
			)
		p = figure(
			tools="save,pan",
			y_range=Range1d(start=0,end=90), x_axis_type="datetime",
			x_axis_label='tiempo', y_axis_label='altitud')

		left = figure(title="Elevación", tools=[hover1,"crosshair"], width=410 , height=390,
			y_range=Range1d(start=0,end=90), x_axis_type="datetime", x_axis_label='Tiempo')

		left.line(x="x",y="al",source=self.source, color="red")
		tab2 = Panel(child=left, title="Elevación")

#show(left)
#save(left,"altitud_gra.html",validate=True)

		# create another new plot and add a renderer
		right = figure(title="Azimut",tools=[hover2,"crosshair"],  width=410 , height=390,
			y_range=Range1d(start=0,end=360),x_axis_type="datetime",x_axis_label='Tiempo')
	
		right.line(x="x",y="az", source=self.source,color="blue")
		tab1 = Panel(child=right, title="Azimut")

# put the subplots in a gridplot

#show(right)
#save(right,"azimut_gra.html",validate=True)

		tabs = Tabs(tabs=[ tab1, tab2 ])

		save(tabs,"az_alt_gra.html",validate=True)
		os.chdir(self.raiz)
	
	def tabular(self):
		os.chdir(self.sa)
		DF_ag=NumberFormatter(format="0.00")
		columns = [
				TableColumn(field="t", title="Tiempo"),
				TableColumn(field="al",title="Elevación (Grados)",formatter=DF_ag,sortable=True),
				TableColumn(field="az",title="Azimut (Grados)",formatter=DF_ag,sortable=True)
			]

		data_table = DataTable(source=self.source, columns=columns ,width=450, height=450)
		save(data_table,"data_table.html",validate=True)
		os.chdir(self.raiz)



class QT_url(QDialog):
	def __init__(self,direc,w,h,nom,parent=None):
		QWidget.__init__(self, parent)
		self.resize(w,h)
		#print nom
		self.setWindowTitle(nom)
		self.webview = QWebView()
		self.webview.load(QUrl(direc))
		self.la=QVBoxLayout()
		self.la.addWidget(self.webview)
		self.setLayout(self.la)


#class Gafica_angulo_save(QDialog):
#	def __init__(self,parent=None):
#		QWidget.__init__(self, parent)
#		self.webview = QWebView()
#		self.webview.load(QUrl("file:///home/cidte/programas de python/Ejercicio de Python/partes del codigo/az_alt_gra.html"))
#		self.la=QVBoxLayout()
#		self.la.addWidget(self.webview)
#		self.setLayout(self.la)
		

#if __name__ == "__main__":
	#app = QApplication(sys.argv)
	#print direc
	#myapp =QT_url("file://"+direc,w=1200,h=500,nom="Preuva")
	#myapp.show()
	#sys.exit(app.exec_())

