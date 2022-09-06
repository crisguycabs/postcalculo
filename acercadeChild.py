# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'acercadeChild.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
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
        self.label_2.setGeometry(QtCore.QRect(250, 70, 191, 71))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("ecopetrol.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Acercade)
        self.buttonBox.accepted.connect(Acercade.accept)
        self.buttonBox.rejected.connect(Acercade.reject)
        QtCore.QMetaObject.connectSlotsByName(Acercade)

    def retranslateUi(self, Acercade):
        _translate = QtCore.QCoreApplication.translate
        Acercade.setWindowTitle(_translate("Acercade", "Acerca de..."))
        self.label.setText(_translate("Acercade", "<html><head/><body><p><span style=\" font-family:\'Humanst521 BT\',\'sans-serif\'; font-size:11pt; font-weight:600;\">Centro de Innovación y Tecnología Instituto Colombiano del Petróleo ICP</span></p><p><span style=\" font-weight:600;\">Grupo de Análisis de Sistemas Energéticos</span></p><p><span style=\" font-weight:600;\">Contacto</span>: ariel.uribe@ecopetrol.com.co </p><p><span style=\" font-weight:600;\">Desarrollado por TIP LTDA: </span></p><p>Ph.D.(c) Cristomo A Barajas Solano </p><p>Msc.(c) Jorge E Diaz </p><p>Ing. Luz A Bohorquez Ballesteros </p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Acercade = QtWidgets.QDialog()
    ui = Ui_Acercade()
    ui.setupUi(Acercade)
    Acercade.show()
    sys.exit(app.exec_())
