# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colParamChild.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ColParamChild(object):
    def setupUi(self, ColParamChild):
        ColParamChild.setObjectName("ColParamChild")
        ColParamChild.resize(565, 375)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ecp.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ColParamChild.setWindowIcon(icon)
        self.btnBox = QtWidgets.QDialogButtonBox(ColParamChild)
        self.btnBox.setEnabled(True)
        self.btnBox.setGeometry(QtCore.QRect(215, 340, 340, 32))
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnBox.setObjectName("btnBox")
        self.tableWidget = QtWidgets.QTableWidget(ColParamChild)
        self.tableWidget.setGeometry(QtCore.QRect(10, 40, 545, 190))
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.label = QtWidgets.QLabel(ColParamChild)
        self.label.setGeometry(QtCore.QRect(340, 10, 81, 16))
        self.label.setObjectName("label")
        self.cmbCategoria = QtWidgets.QComboBox(ColParamChild)
        self.cmbCategoria.setGeometry(QtCore.QRect(400, 10, 155, 22))
        self.cmbCategoria.setObjectName("cmbCategoria")
        self.label_2 = QtWidgets.QLabel(ColParamChild)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 101, 16))
        self.label_2.setObjectName("label_2")
        self.txtNombreColumna = QtWidgets.QLineEdit(ColParamChild)
        self.txtNombreColumna.setGeometry(QtCore.QRect(100, 10, 113, 20))
        self.txtNombreColumna.setObjectName("txtNombreColumna")
        self.btnLimpiar = QtWidgets.QPushButton(ColParamChild)
        self.btnLimpiar.setGeometry(QtCore.QRect(10, 240, 101, 23))
        self.btnLimpiar.setObjectName("btnLimpiar")
        self.chkFormula = QtWidgets.QCheckBox(ColParamChild)
        self.chkFormula.setGeometry(QtCore.QRect(10, 270, 101, 17))
        self.chkFormula.setObjectName("chkFormula")
        self.txtFormula = QtWidgets.QTextEdit(ColParamChild)
        self.txtFormula.setEnabled(False)
        self.txtFormula.setGeometry(QtCore.QRect(10, 295, 545, 41))
        self.txtFormula.setObjectName("txtFormula")
        self.label_3 = QtWidgets.QLabel(ColParamChild)
        self.label_3.setGeometry(QtCore.QRect(120, 240, 431, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.label_3.setPalette(palette)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")

        self.retranslateUi(ColParamChild)
        self.btnBox.accepted.connect(ColParamChild.accept)
        self.btnBox.rejected.connect(ColParamChild.reject)
        QtCore.QMetaObject.connectSlotsByName(ColParamChild)

    def retranslateUi(self, ColParamChild):
        _translate = QtCore.QCoreApplication.translate
        ColParamChild.setWindowTitle(_translate("ColParamChild", "Columna parametro"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ColParamChild", "Nombre E/S"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ColParamChild", "Dimensiones"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("ColParamChild", "Categoria"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("ColParamChild", "value/level"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("ColParamChild", "up"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("ColParamChild", "lo"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("ColParamChild", "marginal"))
        self.label.setText(_translate("ColParamChild", "Filtrar por:"))
        self.label_2.setText(_translate("ColParamChild", "Nombre columna:"))
        self.btnLimpiar.setText(_translate("ColParamChild", "Limpiar seleccion"))
        self.chkFormula.setText(_translate("ColParamChild", "Agregar formula"))
        self.label_3.setText(_translate("ColParamChild", "<html><head/><body><p>Este es un mensaje de errorEste es un mensaje de errorEste es un mensaje de errorEste es un mensaje de errorEste es un mensaje de errorEste es un mensaje de errorEste es un mensaje de errorEste es un mensaje de errorEste es un mensaje de errorEste es un mensaje de errorEste es un mensaje de errorEste es un mensaje de error</p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ColParamChild = QtWidgets.QDialog()
    ui = Ui_ColParamChild()
    ui.setupUi(ColParamChild)
    ColParamChild.show()
    sys.exit(app.exec_())
