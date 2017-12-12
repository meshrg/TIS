#!/usr/bin/python
# -*- coding: utf-8 -*-

#import numpy as np
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
#import ephem as ep
#import time  as ti
#import datetime 
#import math 
#import ntplib as ntp
#from datetime import datetime
#import datetime as dat

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas

from matplotlib.figure import Figure



########################################################################
##### Datos inicales ###################################################
########################################################################

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *


class Grafica(FigureCanvas):
	def __init__(self,parent=None,dpi=100):
		QWidget.__init__(self, parent)
		self.figure =Figure(dpi=110)
		FigureCanvas.__init__(self, self.figure)
		self.setParent(parent)
		self.axes = self.figure.add_subplot(111)
		self.sat_lu

	def sat_lu(self,seg,red,t):
		
		self.map = Basemap(projection='mill',lat_0=0,lon_0=0.,ax= self.axes)
		### paralelos 
		self.map.drawparallels(np.arange(-90,90,15),labels=[1,1,0,0])
		## meridianos 
		self.map.drawmeridians(np.arange(-180,180,40),labels=[0,0,1,1])
		self.map.drawmapboundary(fill_color='aqua')
		self.map.fillcontinents(color='coral',lake_color='aqua')
		
		x, y =self.map(seg["observador"][0],seg["observador"][1])
		self.map.plot(x,y, marker="x",color="r")
		gru=[]
		for k in seg.keys():
			gru.append(k)
		gru.remove('observador')
		for l in gru:
			x, y =self.map(seg[l][0],seg[l][1])
			if l == red:
				self.map.plot(x,y, marker="d",color="r")
			else:
				self.map.plot(x,y, marker="d",color="b")
		CS=self.map.nightshade(t)









if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Grafica()
	window.sat_lu(seg,sat_lis[2],t)
	window.show()
	#print dir(window)
	sys.exit(app.exec_())



