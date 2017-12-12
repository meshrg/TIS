# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'add_datos.ui'
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
        Form.resize(541, 413)
        self.label_6 = QtGui.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(9, 239, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.observ_lod = QtGui.QTextEdit(Form)
        self.observ_lod.setGeometry(QtCore.QRect(159, 239, 171, 31))
        self.observ_lod.setObjectName(_fromUtf8("observ_lod"))
        self.pb_lep = QtGui.QPushButton(Form)
        self.pb_lep.setGeometry(QtCore.QRect(360, 140, 151, 27))
        self.pb_lep.setObjectName(_fromUtf8("pb_lep"))
        self.label_5 = QtGui.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(9, 184, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.observ_lad = QtGui.QTextEdit(Form)
        self.observ_lad.setGeometry(QtCore.QRect(159, 184, 171, 31))
        self.observ_lad.setObjectName(_fromUtf8("observ_lad"))
        self.label_7 = QtGui.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(9, 300, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.spinBox = QtGui.QSpinBox(Form)
        self.spinBox.setGeometry(QtCore.QRect(159, 300, 81, 27))
        self.spinBox.setMaximum(999999)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.label_3 = QtGui.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(9, 90, 91, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.observ_des = QtGui.QTextEdit(Form)
        self.observ_des.setGeometry(QtCore.QRect(159, 90, 261, 31))
        self.observ_des.setObjectName(_fromUtf8("observ_des"))
        self.observ_at = QtGui.QTextEdit(Form)
        self.observ_at.setGeometry(QtCore.QRect(159, 43, 211, 31))
        self.observ_at.setObjectName(_fromUtf8("observ_at"))
        self.label_2 = QtGui.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(9, 43, 144, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label = QtGui.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(220, 10, 115, 28))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(9, 135, 81, 17))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.observ_ubi = QtGui.QTextEdit(Form)
        self.observ_ubi.setGeometry(QtCore.QRect(159, 135, 191, 31))
        self.observ_ubi.setObjectName(_fromUtf8("observ_ubi"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(270, 367, 170, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.pb_G = QtGui.QPushButton(self.splitter)
        self.pb_G.setObjectName(_fromUtf8("pb_G"))
        self.pb_C = QtGui.QPushButton(self.splitter)
        self.pb_C.setObjectName(_fromUtf8("pb_C"))
        self.pb_py = QtGui.QPushButton(Form)
        self.pb_py.setGeometry(QtCore.QRect(370, 210, 85, 27))
        self.pb_py.setObjectName(_fromUtf8("pb_py"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label_6.setText(_translate("Form", "<html><head/><body><p>Longitud(°)</p></body></html>", None))
        self.pb_lep.setText(_translate("Form", "Seleccionar ubicación", None))
        self.label_5.setText(_translate("Form", "<html><head/><body><p>Latitud(°)</p></body></html>", None))
        self.label_7.setText(_translate("Form", "<html><head/><body><p>Altitud (m) </p></body></html>", None))
        self.label_3.setText(_translate("Form", "<html><head/><body><p>Descripción</p></body></html>", None))
        self.label_2.setText(_translate("Form", "<html><head/><body><p>Nombre </p></body></html>", None))
        self.label.setText(_translate("Form", "Obsevador", None))
        self.label_4.setText(_translate("Form", "<html><head/><body><p>Ubicación</p></body></html>", None))
        self.pb_G.setText(_translate("Form", "Guardar", None))
        self.pb_C.setText(_translate("Form", "Cerrar", None))
        self.pb_py.setText(_translate("Form", "Ubicarme", None))


class Form(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

