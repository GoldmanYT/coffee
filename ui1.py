# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UI/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.8
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.table_widget = QtWidgets.QTableWidget(self.centralwidget)
        self.table_widget.setGeometry(QtCore.QRect(10, 50, 781, 541))
        self.table_widget.setObjectName("table_widget")
        self.table_widget.setColumnCount(7)
        self.table_widget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(6, item)
        self.btn = QtWidgets.QPushButton(self.centralwidget)
        self.btn.setGeometry(QtCore.QRect(10, 10, 781, 31))
        self.btn.setObjectName("btn")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.table_widget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.table_widget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "название сорта"))
        item = self.table_widget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "степень обжарки"))
        item = self.table_widget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "молотый/в зернах"))
        item = self.table_widget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "описание вкуса"))
        item = self.table_widget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "цена"))
        item = self.table_widget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "объем упаковки"))
        self.btn.setText(_translate("MainWindow", "Добавить/редактировать запись"))
