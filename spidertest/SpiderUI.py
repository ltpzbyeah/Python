# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpiderUI.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(884, 645)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.searchButton = QtWidgets.QPushButton(Form)
        self.searchButton.setObjectName("searchButton")
        self.horizontalLayout.addWidget(self.searchButton)
        self.resetButton = QtWidgets.QPushButton(Form)
        self.resetButton.setObjectName("resetButton")
        self.horizontalLayout.addWidget(self.resetButton)
        self.horizontalLayout.setStretch(0, 7)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_Video = QtWidgets.QWidget()
        self.page_Video.setObjectName("page_Video")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.page_Video)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.tableWidget_Video = QtWidgets.QTableWidget(self.page_Video)
        self.tableWidget_Video.setRowCount(20)
        self.tableWidget_Video.setColumnCount(4)
        self.tableWidget_Video.setObjectName("tableWidget_Video")
        self.horizontalLayout_3.addWidget(self.tableWidget_Video)
        self.stackedWidget.addWidget(self.page_Video)
        self.page_Music = QtWidgets.QWidget()
        self.page_Music.setObjectName("page_Music")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.page_Music)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.tableWidget_Music = QtWidgets.QTableWidget(self.page_Music)
        self.tableWidget_Music.setRowCount(20)
        self.tableWidget_Music.setColumnCount(4)
        self.tableWidget_Music.setObjectName("tableWidget_Music")
        self.horizontalLayout_4.addWidget(self.tableWidget_Music)
        self.stackedWidget.addWidget(self.page_Music)
        self.page_Search = QtWidgets.QWidget()
        self.page_Search.setObjectName("page_Search")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.page_Search)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.stackedWidget.addWidget(self.page_Search)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.progressBar = QtWidgets.QProgressBar(Form)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout.addWidget(self.progressBar)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "视频"))
        self.comboBox.setItemText(1, _translate("Form", "音乐"))
        self.comboBox.setItemText(2, _translate("Form", "百科"))
        self.searchButton.setText(_translate("Form", "搜索"))
        self.resetButton.setText(_translate("Form", "重置"))


