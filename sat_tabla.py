import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np
import ephem as ep
import time  as ti
import datetime 
import math 
import ntplib as ntp

#import pylab as plt
from datetime import datetime
import datetime as dat



#def leertxt(nomdre):
	#arch=open(nomdre)
	#l1=arch.readline()
	#satlis=dict()
	#while l1:
		#l2=arch.readline()
		#l3=arch.readline()
		#sat=ep.readtle(l1,l2,l3)
		#satlis[sat.name]=sat
		#l1=arch.readline()
	#arch.close()
	#return satlis

###############################################################################
###### Batos inicales #########################################################
###############################################################################

##punto de obsecacion 
#zac=ep.Observer()
#zac.long=ep.degrees("-102.2925")
#zac.lat=ep.degrees("22.4520984")
##use una plicacion
#zac.elevation=2239  #en metros 

##Timpo y feca 
##x = ntp.NTPClient()
##c=x.request("mx.pool.ntp.org",version=1,timeout=5)
##t=datetime.utcfromtimestamp(c.orig_time)


#Sat=leertxt("vario_sat.txt")

#sat_lis=[]

#for k in Sat.keys():
	#sat_lis.append(k)

#ti_formato="%Y/%m/%d %H:%M:%S"
#####Formato para restar las horas

##Convetimos los timpos a formatos datetime
##ti_final=datetime.strptime(str(seg[4]),ti_formato)
##ti_ini=datetime.strptime(str(seg[0]),ti_formato) 


##ISS.compute(zac)
##3lon=np.rad2deg(ISS.sublong)
##lat=np.rad2deg(ISS.sublat)
#sat_t=dict()
#sat_t_s=dict()
##seg=dict()
##seg["observador"]=[-102.2925,22.4520984]

#for no in sat_lis:
	#print Sat[no]
	#Sat[no].compute(zac)
	#if Sat[no].transit_time!=None:
		#n_s=zac.next_pass(Sat[no])
		#if n_s[0]==None:
			#sat_t={"Tiempo Inical":"No encontrado","Tiempo Final":"No encontrado","Duracion":"notiene"}
		#else:
			#sat_t={"Tiempo Inical":str(datetime.strptime(str(n_s[0]),ti_formato)),"Tiempo Final":str(datetime.strptime(str(n_s[4]),ti_formato)),"Duracion":str(datetime.strptime(str(n_s[4]),ti_formato)-datetime.strptime(str(n_s[0]),ti_formato))}
	#else: 
		#sat_t={"Tiempo Inical":"Geo ","Tiempo Final":"Geo","Duracion":"Simepre"}
		#sat_t_s[no]=sat_t



class MyTable(QTableWidget):
	def __init__(self, data, *args):
		QTableWidget.__init__(self, *args)
		self.data = data
		self.resize(360,215)
		self.k_data=list(self.data.keys())
		self.fila=len(self.k_data)
		self.set_datatime()
		self.setmydata()
		self.resizeColumnsToContents()
		self.resizeRowsToContents()
		
 
	def set_datatime(self): 
		self.setColumnWidth(0,101)
		self.setColumnWidth(1,136)
		self.setColumnWidth(2,136)
		self.setColumnWidth(3,71)
		self.k_2=["Tiempo Inical","Tiempo Final",'Duracion']
		for n,key in enumerate(self.k_data):
			self.sa=self.data[key]
			newitem = QTableWidgetItem(key)
			self.setItem(n, 0, newitem)
			for item in self.k_2:
				newitem = QTableWidgetItem(self.sa[item])
				if item =="Tiempo Inical":
					self.setItem(n, 1, newitem)
				elif item == "Duracion":
					self.setItem(n, 3, newitem)
				else:
					self.setItem(n, 2, newitem)
					
		self.k_2.insert(0,"Satelite")
		self.setHorizontalHeaderLabels(self.k_2)
		self.setRowCount(self.fila)
		self.setColumnCount(4)
		
		
	def setmydata(self):
		horHeaders = []
		for n, key in enumerate(sorted(self.data.keys())):
			horHeaders.append(key)
			for m, item in enumerate(self.data[key]):
				newitem = QTableWidgetItem(str(item))
				self.setItem(m, n, newitem)
		self.setHorizontalHeaderLabels(horHeaders)
		self.setRowCount(self.fila)




if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = MyTable(sat_t_s)
	window.set_datatime()
	window.show()
	#print dir(window)
	sys.exit(app.exec_())

