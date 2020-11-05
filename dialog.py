# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dialog.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(493, 146)
        Dialog.setStyleSheet("background-color: black")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 65, 471, 66))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(36)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("font: 36pt \"Consolas\";\n"
"color: white;\n"
"background-color: black; border: none;\n"
"border-bottom: 1px solid white;\n"
"border-right: 1px solid white;")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 471, 51))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("color: white;\n"
"background-color: black; border: none;\n"
"border-bottom: 1px solid white;\n"
"border-right: 1px solid white;")
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        Dialog.setWhatsThis(_translate("Dialog", "<html><head/><body><p>Должно работать</p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "Решить"))
