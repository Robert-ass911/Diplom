# Form implementation generated from reading ui file 'app\forms\ui\categories.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_CategoriesWindow(object):
    def setupUi(self, CategoriesWindow):
        CategoriesWindow.setObjectName("CategoriesWindow")
        CategoriesWindow.resize(325, 226)
        self.centralwidget = QtWidgets.QWidget(parent=CategoriesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.name_line = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.name_line.setObjectName("name_line")
        self.horizontalLayout.addWidget(self.name_line)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.create_btn = QtWidgets.QPushButton(parent=self.centralwidget)
        self.create_btn.setObjectName("create_btn")
        self.horizontalLayout_2.addWidget(self.create_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.tableWidget = QtWidgets.QTableWidget(parent=self.centralwidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout.addWidget(self.tableWidget)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        CategoriesWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(CategoriesWindow)
        QtCore.QMetaObject.connectSlotsByName(CategoriesWindow)

    def retranslateUi(self, CategoriesWindow):
        _translate = QtCore.QCoreApplication.translate
        CategoriesWindow.setWindowTitle(_translate("CategoriesWindow", "MainWindow"))
        self.label.setText(_translate("CategoriesWindow", "Имя:"))
        self.create_btn.setText(_translate("CategoriesWindow", "Создать"))
