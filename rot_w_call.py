import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from rot_w import *
 
import ephem as ep
import time  as ti

from datetime import datetime
import datetime as dat
import Hamlib
import numpy as np

#def int_num(valor,por):
	#"""
	#valor= el numpero sental 
	#por= le porsentaje numero . 
	#"""
	#n1=valor*por
	#ini=float("{0:.2f}".format(valor-n1))
	#fin=float("{0:.2f}".format(valor+n1))
	#print "#######################"
	#print ini
	#print fin
	#print "#######################"
	#fl=True
	#vec=[ini]
	#p=0
	#while fl:
		#nex=float("{0:.2f}".format(vec[p]+0.01))
		#if nex==fin:
			#fl=False
		#p=p+1
		#print "#############################################"
		#vec.insert(p,nex)
	#return vec



class Rot_ant(QtGui.QDialog):
	def __init__(self,dic_sat,de_time,obser,parent=None):
		QtGui.QWidget.__init__(self, parent)
		self.ui=Ui_Form()
		self.ui.setupUi(self)
		self.setWindowTitle(u"Control de la antena")
		### el rotor al prinsipo esta en comunicacion ###
		self.rot=Hamlib.Rot(Hamlib.ROT_MODEL_EASYCOMM2)
		self.rot.set_conf("serial_speed","19200") 
		self.rot.set_conf("timeout","500")
		self.rot.set_conf("rot_pathname","/dev/ttyACM0") #Nombre de la antena 
		self.rot.open()
		self.dic_sat=dic_sat
		self.ob=obser
		self.ras=False
		#######################################################
		self.LCD=self.ui.W_Ti_data_r
		###### Tomado la lisrta de lo satelites #####
		self.l=list(dic_sat.keys())
		for it_text in self.l:
			self.ui.CB_sat.addItem(it_text)
		
		self.ui.PB_conec.clicked.connect(self.datos)
		self.ui.PB_desco.clicked.connect(self.datos_off)
		self.ui.PB_Set.clicked.connect(self.set_ag)
		self.ui.CB_sat.activated.connect(self.get_sat)
		self.ui.PB_close.clicked.connect(self.clo)
		
		self.ui.PB_conec.setEnabled(False)
		self.t=de_time

		#self.t_re=self.t
		#self.tz=self.t-dat.timedelta(hours=self.h_z)
		self.LCD.setText(str(self.t.strftime("%Y/%m/%d %H:%M:%S")))
		
		self.timer = QtCore.QTimer(self)
		self.timer.timeout.connect(self.sleep)
		self.timer.start(1000)
		
		
	
	def sleep(self):
		self.t=self.t+dat.timedelta(seconds=1)
		#self.tz=self.t1-dat.timedelta(hours=self.h_z)
		#self.LCD_2.setText(str(self.tz.strftime("%Y/%m/%d %H:%M:%S")))
		self.LCD.setText(str(self.t.strftime("%Y/%m/%d %H:%M:%S")))
		[self.r_az,self.r_el]=self.rot.get_position()
		self.ui.L_az.setText(str(self.r_az))
		self.ui.L_el.setText(str(self.r_el))
		if self.ras==True:
			self.ob.date=self.t
			self.sat.compute(self.ob)
			self.g_az=float("{0:.2f}".format(np.rad2deg(self.sat.az)))
			self.g_el=float("{0:.2f}".format(np.rad2deg(self.sat.alt)))
			# evita los valores negartivos }
			## crAR UN INtervalo 
			valor=(self.g_az*0.05)
			self.int_az_min=self.g_az-valor
			self.int_az_max=self.g_az+valor
			if self.g_el<0:
				self.g_el=0
			valor=(self.g_el*0.05)
			###############No borrar #########################4
			self.rot.set_position(self.g_az,self.g_el)
			################################################4
			self.int_el_min=self.g_az-valor
			self.int_el_max=self.g_az+valor
			ci=True
		#Espera de que tome la posicion
			while ci:
				[self.r_az,self.r_el]=self.rot.get_position()
				self.r_az=float("{0:.2f}".format(self.r_az))
				self.r_el=float("{0:.2f}".format(self.r_el))
				if (self.r_az >self.int_az_min) or (self.r_az<self.int_az_max):
					if (self.r_el >self.int_el_min) or (self.r_el <self.int_el_max ):
						ci=False
			self.t=dat.datetime.utcnow()
			
	def get_sat(self):
		self.sat_no=str(self.ui.CB_sat.currentText())
		self.ui.PB_conec.setEnabled(True)
		
	def set_ag(self):
		self.s_az=float("{0:.2f}".format(self.ui.SB_az.value()))
		self.s_el=float("{0:.2f}".format(self.ui.SB_el.value()))
		[self.r_az,self.r_el]=self.rot.get_position()
		self.rot.set_position(self.s_az,self.s_el)
		#Espera de que tome la posicion

	
	def datos(self):
		self.sat=self.dic_sat[self.sat_no]
		self.ui.CB_sat.setEnabled(False)
		self.ui.PB_conec.setEnabled(False)
		self.ras=True
		
	def datos_off(self):
		self.ui.CB_sat.setEnabled(True)
		self.ui.PB_conec.setEnabled(True)
		self.ras=False
		
	def clo(self):
		self.rot.set_position(0,0)
		while True:
			[self.r_az,self.r_el]=self.rot.get_position()
			self.r_az=float("{0:.2f}".format(self.r_az))
			self.r_el=float("{0:.2f}".format(self.r_el))
			if self.r_az ==00:
				if self.r_el==00:
					break
		self.rot.close()
		self.close()
		




if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = Rot_ant()
    myapp.show()
    sys.exit(app.exec_())



