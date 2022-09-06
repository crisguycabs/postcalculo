# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'colParamChild.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QAbstractTableModel, Qt
from PyQt5.QtWidgets import  QTableWidgetItem

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
        self.label_3.setGeometry(QtCore.QRect(120, 240, 431, 20))
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
        self.label_3.setPalette(palette)
        self.label_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_3.setTextFormat(QtCore.Qt.RichText)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
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
        self.label_3.setText(_translate("ColParamChild", "Este es un mensaje de error"))

    def SetCustom(self,MainProtoV2):
        
        # datos desde el padre
        self.padre=MainProtoV2
        self.data=MainProtoV2.data
        
        self.columna={}
        self.columna["TIPO_DATO_GAMS"]="PARAMETER"
        self.columna["NOMBRE_E_S"]=[]
        self.columna["TIPO_CAMPO"]=[]
        self.columna["NOMBRE_COLUMNA"]=""
        self.columna["FORMULA"]="NA"
        
        # ancho de columnas
        self.tableWidget.setColumnWidth(0, 30)
        self.tableWidget.setColumnWidth(1, 90)
        self.tableWidget.setColumnWidth(2, 80)
        self.tableWidget.setColumnWidth(3, 100)
        self.tableWidget.setColumnWidth(4, 70)
        self.tableWidget.setColumnWidth(5, 30)
        self.tableWidget.setColumnWidth(6, 30)
        self.tableWidget.setColumnWidth(7, 60)
        
        # se llena el combobox
        categoria=self.data.iloc[:,3].unique()
        self.cmbCategoria.addItems(categoria)
        self.cmbCategoria.insertItem(0,"Todas las categorias")
        
        self.LlenarTable(self.data)
                
        # evento de cambio de indice
        self.cmbCategoria.currentIndexChanged.connect(self.CambioSeleccion)
        
        self.cmbCategoria.setCurrentIndex(0)
        
        # evento de limpiar seleccion
        self.btnLimpiar.clicked.connect(self.Limpiar)
        
        # evento de activar el modo formula
        self.chkFormula.stateChanged.connect(self.ActivarFormula)
        
        # evento para revisar las dimensiones al cambiar el checked en la tabla
        self.tableWidget.itemChanged.connect(self.CheckDimensiones)
        
        self.label_3.setText("")
        
    '''
    se activan o desactivan botones en el tablewidget
    '''
    def CheckDimensiones(self):
        # failsafe
        if(self.controlcheck==True):
            return

        # parametros seleccionados
        lista=list()
        self.label_3.setText("")
        for i in range(self.tableWidget.rowCount()):
            item = self.tableWidget.item(i, 0)
            if item.checkState() == QtCore.Qt.Checked:
                # es un parametro o variable?
                temp=self.data.loc[self.data["nombre_dato"]==self.tableWidget.item(i, 1).text()]
                lista.append((self.tableWidget.item(i, 1).text(),self.tableWidget.item(i, 2).text(),temp.iloc[0,0]))
        
        if(len(lista)==1):
            # solo hay un elemento seleccionado, se verifica si hay dimensiones previas
            if(self.padre.dimensiones):
                if(self.padre.dimensiones!=lista[0][1]):
                    self.label_3.setText("Las dimensiones seleccionadas no coinciden con las columnas creadas previamente. Modifique su selección")
        elif(len(lista)>1):
            for i in range(1,len(lista)):
                for j in range(0,len(lista)-1):
                    if(lista[i][1]!=lista[j][1]):
                        self.label_3.setText("Las dimensiones seleccionadas no coinciden. Modifique su selección")
                        return
                    if(self.padre.dimensiones):
                        if(self.padre.dimensiones!=lista[i][1]):
                            self.label_3.setText("Las dimensiones seleccionadas no coinciden con las columnas creadas previamente. Modifique su selección")
                            return
                        if(self.padre.dimensiones!=lista[j][1]):
                            self.label_3.setText("Las dimensiones seleccionadas no coinciden con las columnas creadas previamente. Modifique su selección")
                            return
    
    '''
    se activa el modo formula
    '''
    def ActivarFormula(self):
        self.txtFormula.setEnabled(self.chkFormula.isChecked())
    
    '''
    se limpian los elementos seleccionados en la primera columna
    '''
    def Limpiar(self):
        for row  in range(self.tableWidget.rowCount()):
            self.tableWidget.item(row, 0).setCheckState(QtCore.Qt.Unchecked)
    
    '''
    Evento de cambio de indice del combobox seleccionado
    '''
    def CambioSeleccion(self):
        self.controlcheck=True
        indice=self.cmbCategoria.currentIndex()
        if(indice==0):
            self.LlenarTable(self.data)
        else:
            self.LlenarTable(self.data[self.data["categoria"]==self.cmbCategoria.currentText()])
        self.controlcheck=False
    
    '''
    Se limpia y llena el Qtablewidget segun el dataframe que se pasa como argumento
    '''
    def LlenarTable(self,datos):
        
        self.tableWidget.clearContents()
        
        self.tableWidget.setRowCount(len(datos))
        
        for i in range(len(datos)):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(""))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(datos.iloc[i,1]))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(datos.iloc[i,2]))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(datos.iloc[i,3]))
            self.tableWidget.setItem(i, 4, QTableWidgetItem(""))
            self.tableWidget.setItem(i, 5, QTableWidgetItem(""))
            self.tableWidget.setItem(i, 6, QTableWidgetItem(""))
            self.tableWidget.setItem(i, 7, QTableWidgetItem(""))
            
            chkBoxItem = QTableWidgetItem()
            chkBoxItem.setFlags(QtCore.Qt.ItemIsUserCheckable)
            chkBoxItem.setCheckState(QtCore.Qt.Checked)
            self.tableWidget.setItem(i,4,chkBoxItem)
            
            chkBoxItem5 = QTableWidgetItem()
            chkBoxItem5.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
            chkBoxItem5.setCheckState(QtCore.Qt.Unchecked)
            self.tableWidget.setItem(i,0,chkBoxItem5)
            
            if(datos.iloc[i,0]!="parameter"):
                chkBoxItem2 = QTableWidgetItem()
                chkBoxItem2.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem2.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i,5,chkBoxItem2)
                
                chkBoxItem3 = QTableWidgetItem()
                chkBoxItem3.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem3.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i,6,chkBoxItem3)
                
                chkBoxItem4 = QTableWidgetItem()
                chkBoxItem4.setFlags(QtCore.Qt.ItemIsUserCheckable | QtCore.Qt.ItemIsEnabled)
                chkBoxItem4.setCheckState(QtCore.Qt.Unchecked)
                self.tableWidget.setItem(i,7,chkBoxItem4)

        
# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ColParamChild = QtWidgets.QDialog()
#     ui = Ui_ColParamChild()
#     ui.setupUi(ColParamChild)
#     ColParamChild.show()
#     sys.exit(app.exec_())