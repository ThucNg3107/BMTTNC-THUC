# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/rsa.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1117, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(500, 30, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 150, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(570, 150, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 290, 111, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(580, 290, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.txt_plaintext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_plaintext.setGeometry(QtCore.QRect(140, 150, 371, 87))
        self.txt_plaintext.setObjectName("txt_plaintext")
        self.txt_signature = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_signature.setGeometry(QtCore.QRect(690, 300, 391, 87))
        self.txt_signature.setObjectName("txt_signature")
        self.txt_ciphertext = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_ciphertext.setGeometry(QtCore.QRect(140, 300, 371, 87))
        self.txt_ciphertext.setObjectName("txt_ciphertext")
        self.txt_infomation = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.txt_infomation.setGeometry(QtCore.QRect(690, 150, 391, 87))
        self.txt_infomation.setObjectName("txt_infomation")
        self.btn_encrypt = QtWidgets.QToolButton(self.centralwidget)
        self.btn_encrypt.setGeometry(QtCore.QRect(190, 420, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_encrypt.setFont(font)
        self.btn_encrypt.setObjectName("btn_encrypt")
        self.btn_decrypt = QtWidgets.QToolButton(self.centralwidget)
        self.btn_decrypt.setGeometry(QtCore.QRect(350, 420, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_decrypt.setFont(font)
        self.btn_decrypt.setObjectName("btn_decrypt")
        self.btn_sign = QtWidgets.QToolButton(self.centralwidget)
        self.btn_sign.setGeometry(QtCore.QRect(760, 420, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_sign.setFont(font)
        self.btn_sign.setObjectName("btn_sign")
        self.btn_verify = QtWidgets.QToolButton(self.centralwidget)
        self.btn_verify.setGeometry(QtCore.QRect(940, 420, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.btn_verify.setFont(font)
        self.btn_verify.setObjectName("btn_verify")
        self.btn_generatekeys = QtWidgets.QToolButton(self.centralwidget)
        self.btn_generatekeys.setGeometry(QtCore.QRect(690, 80, 111, 41))
        self.btn_generatekeys.setObjectName("btn_generatekeys")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1117, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "RSA CIPHER"))
        self.label_2.setText(_translate("MainWindow", "Plain Text:"))
        self.label_3.setText(_translate("MainWindow", "Information:"))
        self.label_4.setText(_translate("MainWindow", "Cipher Text:"))
        self.label_5.setText(_translate("MainWindow", "Signature:"))
        self.btn_encrypt.setText(_translate("MainWindow", "Encrypt"))
        self.btn_decrypt.setText(_translate("MainWindow", "Decrypt"))
        self.btn_sign.setText(_translate("MainWindow", "Sign"))
        self.btn_verify.setText(_translate("MainWindow", "Verify"))
        self.btn_generatekeys.setText(_translate("MainWindow", "Generate Keys"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
