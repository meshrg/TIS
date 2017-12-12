# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sat_dato.ui'
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
        Form.resize(629, 430)
        self.sat_G = QtGui.QListWidget(Form)
        self.sat_G.setGeometry(QtCore.QRect(20, 160, 256, 192))
        self.sat_G.setObjectName(_fromUtf8("sat_G"))
        self.TE_B = QtGui.QTextEdit(Form)
        self.TE_B.setGeometry(QtCore.QRect(90, 40, 151, 31))
        self.TE_B.setObjectName(_fromUtf8("TE_B"))
        self.sat_See = QtGui.QListWidget(Form)
        self.sat_See.setGeometry(QtCore.QRect(360, 160, 256, 192))
        self.sat_See.setObjectName(_fromUtf8("sat_See"))
        self.PB_Save = QtGui.QPushButton(Form)
        self.PB_Save.setGeometry(QtCore.QRect(290, 190, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PB_Save.setFont(font)
        self.PB_Save.setObjectName(_fromUtf8("PB_Save"))
        self.splitter = QtGui.QSplitter(Form)
        self.splitter.setGeometry(QtCore.QRect(400, 390, 170, 27))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName(_fromUtf8("splitter"))
        self.pb_G = QtGui.QPushButton(self.splitter)
        self.pb_G.setObjectName(_fromUtf8("pb_G"))
        self.pb_C = QtGui.QPushButton(self.splitter)
        self.pb_C.setObjectName(_fromUtf8("pb_C"))
        self.PB_clear = QtGui.QPushButton(Form)
        self.PB_clear.setGeometry(QtCore.QRect(290, 260, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.PB_clear.setFont(font)
        self.PB_clear.setObjectName(_fromUtf8("PB_clear"))
        self.CB_Gsat = QtGui.QComboBox(Form)
        self.CB_Gsat.setGeometry(QtCore.QRect(90, 90, 131, 31))
        self.CB_Gsat.setObjectName(_fromUtf8("CB_Gsat"))
        self.S_tex = QtGui.QLabel(Form)
        self.S_tex.setGeometry(QtCore.QRect(60, 130, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_tex.setFont(font)
        self.S_tex.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.S_tex.setObjectName(_fromUtf8("S_tex"))
        self.S_tex_2 = QtGui.QLabel(Form)
        self.S_tex_2.setGeometry(QtCore.QRect(410, 130, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_tex_2.setFont(font)
        self.S_tex_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.S_tex_2.setObjectName(_fromUtf8("S_tex_2"))
        self.S_tex_3 = QtGui.QLabel(Form)
        self.S_tex_3.setGeometry(QtCore.QRect(0, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_tex_3.setFont(font)
        self.S_tex_3.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.S_tex_3.setObjectName(_fromUtf8("S_tex_3"))
        self.S_tex_4 = QtGui.QLabel(Form)
        self.S_tex_4.setGeometry(QtCore.QRect(0, 90, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.S_tex_4.setFont(font)
        self.S_tex_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.S_tex_4.setObjectName(_fromUtf8("S_tex_4"))
        self.PB_fin = QtGui.QPushButton(Form)
        self.PB_fin.setGeometry(QtCore.QRect(270, 90, 111, 27))
        self.PB_fin.setObjectName(_fromUtf8("PB_fin"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.PB_Save.setText(_translate("Form", ">\n"
"", None))
        self.pb_G.setText(_translate("Form", "Guardar", None))
        self.pb_C.setText(_translate("Form", "Cerrar", None))
        self.PB_clear.setText(_translate("Form", "<", None))
        self.S_tex.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Lista de Satélites </span></p></body></html>", None))
        self.S_tex_2.setText(_translate("Form", "<html><head/><body><p align=\"center\">Satélites observados</p></body></html>", None))
        self.S_tex_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">Buscar</p></body></html>", None))
        self.S_tex_4.setText(_translate("Form", "<html><head/><body><p align=\"center\">Grupos</p></body></html>", None))
        self.PB_fin.setText(_translate("Form", "En  linea de vista", None))


class Form(QtGui.QWidget, Ui_Form):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QWidget.__init__(self, parent, f)

        self.setupUi(self)

