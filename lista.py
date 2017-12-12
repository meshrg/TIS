from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtCore import QCoreApplication, Qt
from PyQt4.QtGui import QListWidget, QListWidgetItem, QApplication

import time as ti
import sqlite3
import sys
import numpy as np
import ephem as ep
from  lis_observa import *

import os


root_ob = './observa'



citis=[]
lis=[]
#tomando las direccines de cada uno de la ciudades.  
for fileList in os.walk(root_ob):
	fileList=str(fileList)

#convirtiendo los datos de una lista de str.

datos=fileList.split("[]")[1]
for l in datos.split("'"):
	if (".pickle" in l):
		citis.append(l)

#tomamos los nombres
for x in citis:
	lis.append(x.split(".")[0])


lis.sort()
lis.remove("")

l_obs=dict()

class lista(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.ui=Ui_Dialog()
		self.ui.setupUi(self)
		self.add_items()
		self.ui.PB_A.clicked.connect(self.Aceptar_click)
		self.ui.pb_C.clicked.connect(self.close)
		self.setWindowTitle("Lista")
		
	#Codigo para crar la lista.
	def add_items(self):
		for item_text in lis:
			self.ui.lis_obs.addItem(item_text)
			#print(item_text)
			#print(type(item_text))
			#l_obs[item_text]=obs
			

	def Aceptar_click(self):
		it=self.ui.lis_obs.selectedItems()
		x=" "
              #vuele la varibles en una sola lista 
		for i in list(it):
			x= x + (str(i.text()))
			x=x.lstrip()
		return x 







if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = lista()
    #print dir(myapp)
    myapp.show()
    sys.exit(app.exec_())
