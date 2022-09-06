# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acercadeChild.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Acercade(object):
    def setupUi(self, Acercade):
        Acercade.setObjectName("Acercade")
        Acercade.resize(450, 235)
        Acercade.setAutoFillBackground(False)
        self.buttonBox = QtWidgets.QDialogButtonBox(Acercade)
        self.buttonBox.setGeometry(QtCore.QRect(100, 200, 341, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Acercade)
        self.label.setGeometry(QtCore.QRect(10, 10, 311, 171))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Acercade)
        self.label_2.setGeometry(QtCore.QRect(250, 10, 191, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ecopetrol.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Acercade)
        self.label_3.setGeometry(QtCore.QRect(240, 90, 201, 101))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("tip.jpg"))
        self.label_3.setScaledContents(False)
        self.label_3.setObjectName("label_3")
        self.buttonBox.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.label_2.raise_()

        self.retranslateUi(Acercade)
        self.buttonBox.accepted.connect(Acercade.accept)
        self.buttonBox.rejected.connect(Acercade.reject)
        QtCore.QMetaObject.connectSlotsByName(Acercade)

    def retranslateUi(self, Acercade):
        _translate = QtCore.QCoreApplication.translate
        Acercade.setWindowTitle(_translate("Acercade", "Acerca de..."))
        self.label.setText(_translate("Acercade", "<html><head/><body><p><span style=\" font-style:italic;\">Diseñado por </span></p><p>Ph.D. (c) Crisostomo A. Barajas-Solano, TIP Colombia</p><p>M.Sc. Jorge Diaz, TIP Colombia</p><p>M.Sc. Luz Angela Bohorquez, TIP Colombia</p><p><br/><span style=\" font-style:italic;\">Bajo la dirección de</span></p><p>Ph.D. (c) Ariel Uribe, Ecopetrol S.A.</p><p>Ing. Luz Marina Rozo, TIP Colombia</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Acercade = QtWidgets.QDialog()
    ui = Ui_Acercade()
    ui.setupUi(Acercade)
    Acercade.show()
    sys.exit(app.exec_())

