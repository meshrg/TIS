#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from Reloj import *

from datetime import datetime
import datetime as dat
import ntplib as ntp


class Reloj_set(QWidget, Ui_Form):
	def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
		QtGui.QWidget.__init__(self, parent, f)
		self.setupUi(self)
		self.PB_SNTP.clicked.connect(self.NTP_ser)
		self.PB_RM.clicked.connect(self.Ma_reloj)
		self.ti_formato="yyyy/MM/dd hh:mm:ss"
		self.setWindowTitle(u"Hora del observador")
		
		
	def NTP_ser(self):
		self.x = ntp.NTPClient()
		try:
			self.c=self.x.request("mx.pool.ntp.org",version=4,timeout=5)
			self.t = datetime.utcfromtimestamp(self.c.recv_time)
			self.impre_timer
			self.close()
		except:
			 self.btn_Error_clicked()
			
		#self.c=self.x.request("mx.pool.ntp.org",version=4,timeout=5)
		#fchea actual en UTC 
		
		
		
	def Ma_reloj(self):
		ti_formato="%Y/%m/%d %H:%M:%S"
		self.t_in=self.DTE_1.dateTime()
		self.t1=str(self.t_in.toString(self.ti_formato))
		self.t=datetime.strptime(self.t1,ti_formato)
		self.impre_timer
		self.close()
		
	def btn_Error_clicked(self):
		QtGui.QMessageBox.information(self, "Informacion", u"""Error de conexión""",
		QtGui.QMessageBox.Ok)
		
	def impre_timer(self):
		return self.t



if __name__ == "__main__":
	app = QApplication(sys.argv)
	window = Reloj_set()
	window.show()
	sys.exit(app.exec_())


