# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colQueryChild.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ColQueryChild(object):
    def setupUi(self, ColQueryChild):
        ColQueryChild.setObjectName("ColQueryChild")
        ColQueryChild.resize(400, 256)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("ecp.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        ColQueryChild.setWindowIcon(icon)
        self.btnBox = QtWidgets.QDialogButtonBox(ColQueryChild)
        self.btnBox.setGeometry(QtCore.QRect(50, 220, 341, 32))
        self.btnBox.setOrientation(QtCore.Qt.Horizontal)
        self.btnBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.btnBox.setObjectName("btnBox")
        self.txtNombre = QtWidgets.QLineEdit(ColQueryChild)
        self.txtNombre.setEnabled(True)
        self.txtNombre.setGeometry(QtCore.QRect(100, 10, 113, 20))
        self.txtNombre.setReadOnly(False)
        self.txtNombre.setObjectName("txtNombre")
        self.label_3 = QtWidgets.QLabel(ColQueryChild)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 91, 16))
        self.label_3.setObjectName("label_3")
        self.txtSql = QtWidgets.QTextEdit(ColQueryChild)
        self.txtSql.setGeometry(QtCore.QRect(10, 65, 381, 121))
        self.txtSql.setObjectName("txtSql")
        self.txtDimensiones = QtWidgets.QLineEdit(ColQueryChild)
        self.txtDimensiones.setEnabled(True)
        self.txtDimensiones.setGeometry(QtCore.QRect(100, 35, 113, 20))
        self.txtDimensiones.setReadOnly(False)
        self.txtDimensiones.setObjectName("txtDimensiones")
        self.label_4 = QtWidgets.QLabel(ColQueryChild)
        self.label_4.setGeometry(QtCore.QRect(10, 35, 91, 16))
        self.label_4.setObjectName("label_4")
        self.lblDimensiones = QtWidgets.QLabel(ColQueryChild)
        self.lblDimensiones.setGeometry(QtCore.QRect(9, 190, 381, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        self.lblDimensiones.setPalette(palette)
        self.lblDimensiones.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.lblDimensiones.setTextFormat(QtCore.Qt.RichText)
        self.lblDimensiones.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTop|QtCore.Qt.AlignTrailing)
        self.lblDimensiones.setObjectName("lblDimensiones")

        self.retranslateUi(ColQueryChild)
        self.btnBox.rejected.connect(ColQueryChild.reject)
        self.btnBox.accepted.connect(ColQueryChild.accept)
        QtCore.QMetaObject.connectSlotsByName(ColQueryChild)

    def retranslateUi(self, ColQueryChild):
        _translate = QtCore.QCoreApplication.translate
        ColQueryChild.setWindowTitle(_translate("ColQueryChild", "Columna query"))
        self.txtNombre.setPlaceholderText(_translate("ColQueryChild", "Por asignar..."))
        self.label_3.setText(_translate("ColQueryChild", "Nombre columna: "))
        self.txtDimensiones.setPlaceholderText(_translate("ColQueryChild", "Por asignar..."))
        self.label_4.setText(_translate("ColQueryChild", "Dimensiones: "))
        self.lblDimensiones.setText(_translate("ColQueryChild", "Este es un mensaje de error"))

    def SetCustom(self,MainProtoV2):
        
        # datos desde el padre
        self.padre=MainProtoV2
        self.data=MainProtoV2.data
        
        self.columna={}
        self.columna["TIPO_DATO_GAMS"]="QUERY"
        self.columna["NOMBRE_E_S"]=[]
        self.columna["TIPO_CAMPO"]=[]
        self.columna["NOMBRE_COLUMNA"]=""
        self.columna["FORMULA"]=""
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ColQueryChild = QtWidgets.QDialog()
    ui = Ui_ColQueryChild()
    ui.setupUi(ColQueryChild)
    ColQueryChild.show()
    sys.exit(app.exec_())

