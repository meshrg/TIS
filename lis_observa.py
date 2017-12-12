# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lis_observa.ui'
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

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(400, 300)
        self.lis_obs = QtGui.QListWidget(Dialog)
        self.lis_obs.setGeometry(QtCore.QRect(20, 10, 361, 241))
        self.lis_obs.setObjectName(_fromUtf8("lis_obs"))
        self.PB_A = QtGui.QPushButton(Dialog)
        self.PB_A.setGeometry(QtCore.QRect(190, 260, 85, 27))
        self.PB_A.setObjectName(_fromUtf8("pb_A"))
        self.pb_C = QtGui.QPushButton(Dialog)
        self.pb_C.setGeometry(QtCore.QRect(290, 260, 82, 27))
        self.pb_C.setObjectName(_fromUtf8("pb_C"))

        self.retranslateUi(Dialog)
        self.lis_obs.setCurrentRow(-1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Dialog", None))
        self.PB_A.setText(_translate("Dialog", "Aceptar", None))
        self.pb_C.setText(_translate("Dialog", "Cerrar", None))


class Dialog(QtGui.QDialog, Ui_Dialog):
    def __init__(self, parent=None, f=QtCore.Qt.WindowFlags()):
        QtGui.QDialog.__init__(self, parent, f)

        self.setupUi(self)

