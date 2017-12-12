# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dowload.ui'
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
        Form.resize(369, 252)
        self.Prog_B = QtGui.QProgressBar(Form)
        self.Prog_B.setGeometry(QtCore.QRect(40, 100, 271, 23))
        self.Prog_B.setProperty("value", 24)
        self.Prog_B.setObjectName(_fromUtf8("Prog_B"))
        self.label = QtGui.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(130, 20, 150, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setObjectName(_fromUtf8("label"))
        self.txt_out = QtGui.QLabel(Form)
        self.txt_out.setGeometry(QtCore.QRect(60, 140, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.txt_out.setFont(font)
        self.txt_out.setObjectName(_fromUtf8("txt_out"))
        self.PB_Ac = QtGui.QPushButton(Form)
        self.PB_Ac.setGeometry(QtCore.QRect(130, 180, 85, 27))
        self.PB_Ac.setObjectName(_fromUtf8("PB_Ac"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "Descarga", None))
        self.txt_out.setText(_translate("Form", "", None))
        self.PB_Ac.setText(_translate("Form", "Actualizar", None))


class Form(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

