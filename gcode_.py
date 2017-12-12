#localizando con Geocoder
import sys
from pygeocoder import Geocoder
from PyQt4 import QtCore, QtGui
from pygeo import *
#lugar =" Ramon Lopez Velarde 801, Centro, Universitaria, 98000 Zacatecas,Zacatecas, Mexico"

#print lugar





class pygeoDi(QtGui.QDialog):
	def __init__(self,parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.ui.PB_A.clicked.connect(self.cargar_datos)
		self.ui.PB_C.clicked.connect(self.close)
		
	def cargar_datos(self):
		self.pa=str(self.ui.LE_pais.toPlainText())
		self.es=str(self.ui.LE_Es.toPlainText())
		self.ci=str(self.ui.LE_Ciu.toPlainText())
		self.cal=str(self.ui.LE_calle.toPlainText())
		self.cp=str(self.ui.LE_CP.toPlainText())
		self.address = Geocoder.geocode(self.cal+self.cp+self.ci+self.es+self.pa)
		#print self.address.valid_address
		#print self.address.coordinates
		lug=self.address.coordinates
		#print type(lug)
		#print lug[1]
		return lug

if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = pygeoDi()
    myapp.show()
    sys.exit(app.exec_())
