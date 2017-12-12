# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Reloj.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(400, 300)
        self.PB_SNTP = QtGui.QPushButton(Form)
        self.PB_SNTP.setGeometry(QtCore.QRect(80, 70, 201, 27))
        self.PB_SNTP.setObjectName(_fromUtf8("PB_SNTP"))
        self.S_tex_2 = QtGui.QLabel(Form)
        self.S_tex_2.setGeometry(QtCore.QRect(60, 10, 261, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_tex_2.setFont(font)
        self.S_tex_2.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.S_tex_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.S_tex_2.setObjectName(_fromUtf8("S_tex_2"))
        self.S_tex_5 = QtGui.QLabel(Form)
        self.S_tex_5.setGeometry(QtCore.QRect(100, 120, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_tex_5.setFont(font)
        self.S_tex_5.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.S_tex_5.setObjectName(_fromUtf8("S_tex_5"))
        self.PB_RM = QtGui.QPushButton(Form)
        self.PB_RM.setGeometry(QtCore.QRect(240, 170, 91, 27))
        self.PB_RM.setObjectName(_fromUtf8("PB_RM"))
        self.DTE_1 = QtGui.QDateTimeEdit(Form)
        self.DTE_1.setGeometry(QtCore.QRect(30, 170, 194, 27))
        self.DTE_1.setDate(QtCore.QDate(2017, 4, 1))
        self.DTE_1.setTime(QtCore.QTime(12, 0, 0))
        self.DTE_1.setMaximumDate(QtCore.QDate(2999, 5, 7))
        self.DTE_1.setMinimumDate(QtCore.QDate(2017, 1, 1))
        self.DTE_1.setMaximumTime(QtCore.QTime(14, 59, 59))
        self.DTE_1.setTimeSpec(QtCore.Qt.UTC)
        self.DTE_1.setObjectName(_fromUtf8("DTE_1"))
        self.S_tex_6 = QtGui.QLabel(Form)
        self.S_tex_6.setGeometry(QtCore.QRect(10, 210, 371, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_tex_6.setFont(font)
        self.S_tex_6.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.S_tex_6.setObjectName(_fromUtf8("S_tex_6"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.PB_SNTP.setText(_translate("Form", "Conexion a un servidor NTP", None))
        self.S_tex_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">Reloj del programa </p></body></html>", None))
        self.S_tex_5.setText(_translate("Form", "<html><head/><body><p align=\"center\">Manual</p></body></html>", None))
        self.PB_RM.setText(_translate("Form", "Tomar tiempo", None))
        self.DTE_1.setDisplayFormat(_translate("Form", "yyyy/MM/dd hh:mm:ss ", None))
        self.S_tex_6.setText(_translate("Form", "<html><head/><body><p align=\"center\">La fecha y hora tiene que estar en formato UTC</p></body></html>", None))


class Form(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

