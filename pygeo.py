# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pygeo.ui'
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
        Form.resize(307, 351)
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(21, 41, 24, 17))
        self.label.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label.setObjectName(_fromUtf8("label"))
        self.PB_A = QtGui.QPushButton(Form)
        self.PB_A.setGeometry(QtCore.QRect(150, 300, 85, 27))
        self.PB_A.setObjectName(_fromUtf8("PB_A"))
        self.PB_C = QtGui.QPushButton(Form)
        self.PB_C.setGeometry(QtCore.QRect(40, 300, 85, 27))
        self.PB_C.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.PB_C.setObjectName(_fromUtf8("PB_C"))
        self.LE_pais = QtGui.QTextEdit(Form)
        self.LE_pais.setGeometry(QtCore.QRect(140, 40, 104, 31))
        self.LE_pais.setObjectName(_fromUtf8("LE_pais"))
        self.LE_Es = QtGui.QTextEdit(Form)
        self.LE_Es.setGeometry(QtCore.QRect(140, 90, 104, 31))
        self.LE_Es.setObjectName(_fromUtf8("LE_Es"))
        self.LE_Ciu = QtGui.QTextEdit(Form)
        self.LE_Ciu.setGeometry(QtCore.QRect(140, 140, 104, 31))
        self.LE_Ciu.setObjectName(_fromUtf8("LE_Ciu"))
        self.LE_calle = QtGui.QTextEdit(Form)
        self.LE_calle.setGeometry(QtCore.QRect(140, 190, 104, 31))
        self.LE_calle.setObjectName(_fromUtf8("LE_calle"))
        self.LE_CP = QtGui.QTextEdit(Form)
        self.LE_CP.setGeometry(QtCore.QRect(140, 240, 104, 31))
        self.LE_CP.setObjectName(_fromUtf8("LE_CP"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(21, 151, 41, 17))
        self.label_3.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(21, 101, 40, 17))
        self.label_2.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(21, 201, 29, 17))
        self.label_4.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(21, 251, 79, 17))
        self.label_5.setLocale(QtCore.QLocale(QtCore.QLocale.Spanish, QtCore.QLocale.Mexico))
        self.label_5.setObjectName(_fromUtf8("label_5"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "País", None))
        self.PB_A.setText(_translate("Form", "Aceptar", None))
        self.PB_C.setText(_translate("Form", "Cerrar ", None))
        self.label_3.setText(_translate("Form", "Ciudad", None))
        self.label_2.setText(_translate("Form", "Estado", None))
        self.label_4.setText(_translate("Form", "Calle", None))
        self.label_5.setText(_translate("Form", "Codigo postal", None))


class Form(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

