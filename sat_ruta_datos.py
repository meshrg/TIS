# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sat_ruta_datos.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
import PyQt4.Qwt5 as Qwt
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_W_seg_sat(object):
    def setupUi(self, W_seg_sat):
        W_seg_sat.setObjectName(_fromUtf8("W_seg_sat"))
        W_seg_sat.resize(349, 358)
        self.TW_Sat_paso = QtGui.QTabWidget(W_seg_sat)
        self.TW_Sat_paso.setGeometry(QtCore.QRect(0, 0, 351, 301))
        self.TW_Sat_paso.setObjectName(_fromUtf8("TW_Sat_paso"))
        self.tab_datos = QtGui.QWidget()
        self.tab_datos.setObjectName(_fromUtf8("tab_datos"))
        self.TW_seg_sat = QtGui.QTableWidget(self.tab_datos)
        self.TW_seg_sat.setGeometry(QtCore.QRect(0, 0, 351, 271))
        self.TW_seg_sat.setObjectName(_fromUtf8("TW_seg_sat"))
        self.TW_seg_sat.setColumnCount(0)
        self.TW_seg_sat.setRowCount(0)
        self.TW_Sat_paso.addTab(self.tab_datos, _fromUtf8(""))
        self.tab_A_E = QtGui.QWidget()
        self.tab_A_E.setObjectName(_fromUtf8("tab_A_E"))
        self.QP_AE =Qwt.QwtPlot(self.tab_A_E)
        self.QP_AE.setGeometry(QtCore.QRect(0, 0, 341, 261))
        self.QP_AE.setObjectName(_fromUtf8("QP_AE"))
        self.TW_Sat_paso.addTab(self.tab_A_E, _fromUtf8(""))
        self.tab_polar = QtGui.QWidget()
        self.tab_polar.setObjectName(_fromUtf8("tab_polar"))
        self.QP_P = Qwt.QwtPlot(self.tab_polar)
        self.QP_P.setGeometry(QtCore.QRect(0, 0, 341, 261))
        self.QP_P.setObjectName(_fromUtf8("QP_P"))
        self.TW_Sat_paso.addTab(self.tab_polar, _fromUtf8(""))

        self.retranslateUi(W_seg_sat)
        self.TW_Sat_paso.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(W_seg_sat)

    def retranslateUi(self, W_seg_sat):
        W_seg_sat.setWindowTitle(_translate("W_seg_sat", "Form", None))
        self.TW_Sat_paso.setTabText(self.TW_Sat_paso.indexOf(self.tab_datos), _translate("W_seg_sat", "tabla", None))
        self.TW_Sat_paso.setTabText(self.TW_Sat_paso.indexOf(self.tab_A_E), _translate("W_seg_sat", "Az/El", None))
        self.TW_Sat_paso.setTabText(self.TW_Sat_paso.indexOf(self.tab_polar), _translate("W_seg_sat", "Ruta", None))

#import PyQt4.Qwt5 as Qwt

#from qwt_plot import QwtPlot

class W_seg_sat(QtGui.QWidget, Ui_W_seg_sat):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)
#if __name__ == "__main__":
 #   app = QtGui.QApplication(sys.argv)
  #  myapp = W_seg_sat()
   # myapp.show()
    #app.exec_()
