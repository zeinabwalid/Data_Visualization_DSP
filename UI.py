# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui2.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1321, 742)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.comboBoxMap = QtWidgets.QComboBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comboBoxMap.setFont(font)
        self.comboBoxMap.setObjectName("comboBoxMap")
        self.comboBoxMap.addItem("")
        self.comboBoxMap.addItem("")
        self.comboBoxMap.addItem("")
        self.verticalLayout.addWidget(self.comboBoxMap)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.comboBox_lengthBar = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_lengthBar.sizePolicy().hasHeightForWidth())
        self.comboBox_lengthBar.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_lengthBar.setFont(font)
        self.comboBox_lengthBar.setObjectName("comboBox_lengthBar")
        self.comboBox_lengthBar.addItem("")
        self.comboBox_lengthBar.addItem("")
        self.comboBox_lengthBar.addItem("")
        self.comboBox_lengthBar.addItem("")
        self.verticalLayout.addWidget(self.comboBox_lengthBar)
        self.comboBox_SortBars = QtWidgets.QComboBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_SortBars.sizePolicy().hasHeightForWidth())
        self.comboBox_SortBars.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_SortBars.setFont(font)
        self.comboBox_SortBars.setObjectName("comboBox_SortBars")
        self.comboBox_SortBars.addItem("")
        self.comboBox_SortBars.addItem("")
        self.comboBox_SortBars.addItem("")
        self.comboBox_SortBars.addItem("")
        self.verticalLayout.addWidget(self.comboBox_SortBars)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.export4 = QtWidgets.QPushButton(self.centralwidget)
        self.export4.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("age.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export4.setIcon(icon)
        self.export4.setIconSize(QtCore.QSize(50, 40))
        self.export4.setObjectName("export4")
        self.horizontalLayout_2.addWidget(self.export4)
        self.export3 = QtWidgets.QPushButton(self.centralwidget)
        self.export3.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("bar.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export3.setIcon(icon1)
        self.export3.setIconSize(QtCore.QSize(40, 40))
        self.export3.setObjectName("export3")
        self.horizontalLayout_2.addWidget(self.export3)
        self.export1 = QtWidgets.QPushButton(self.centralwidget)
        self.export1.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.export1.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("bubb.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export1.setIcon(icon2)
        self.export1.setIconSize(QtCore.QSize(50, 40))
        self.export1.setObjectName("export1")
        self.horizontalLayout_2.addWidget(self.export1)
        self.export2 = QtWidgets.QPushButton(self.centralwidget)
        self.export2.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("maap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.export2.setIcon(icon3)
        self.export2.setIconSize(QtCore.QSize(40, 40))
        self.export2.setObjectName("export2")
        self.horizontalLayout_2.addWidget(self.export2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(308, 378, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
        self.widget = QtWebEngineWidgets.QWebEngineView(self.centralwidget)
        self.widget.setObjectName("widget")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.widget)
        self.verticalLayout_3.addLayout(self.formLayout)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.comboBox_SortBars.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Visualization"))
        self.label_2.setText(_translate("MainWindow", "COVID19 Data Visualization"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Visualization Options:"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Animated Bubble Graph."))
        self.comboBox.setItemText(2, _translate("MainWindow", "Animated Map Graph."))
        self.comboBox.setItemText(3, _translate("MainWindow", "Animated Sorted Chart. "))
        self.comboBox.setItemText(4, _translate("MainWindow", "Relation Between Age and # of Cases using Bubble Graph."))
        self.label_3.setText(_translate("MainWindow", "For Animated Maps"))
        self.comboBoxMap.setItemText(0, _translate("MainWindow", "Color of Map indicates:"))
        self.comboBoxMap.setItemText(1, _translate("MainWindow", "Number of Cases in Countries"))
        self.comboBoxMap.setItemText(2, _translate("MainWindow", "Number of Deaths in Countries"))
        self.label.setText(_translate("MainWindow", "For Animated Sorted Chart"))
        self.comboBox_lengthBar.setItemText(0, _translate("MainWindow", "Length of Bars represents:"))
        self.comboBox_lengthBar.setItemText(1, _translate("MainWindow", "Number of Cases."))
        self.comboBox_lengthBar.setItemText(2, _translate("MainWindow", "Number of Deaths."))
        self.comboBox_lengthBar.setItemText(3, _translate("MainWindow", "Both # of Cases and # of Deaths ."))
        self.comboBox_SortBars.setCurrentText(_translate("MainWindow", "Bars sorted by:"))
        self.comboBox_SortBars.setItemText(0, _translate("MainWindow", "Bars sorted by:"))
        self.comboBox_SortBars.setItemText(1, _translate("MainWindow", "Number of Cases."))
        self.comboBox_SortBars.setItemText(2, _translate("MainWindow", "Number of Deaths."))
        self.comboBox_SortBars.setItemText(3, _translate("MainWindow", "Both # of Cases and # of Deaths."))
        self.label_4.setText(_translate("MainWindow", "Export:"))
from PyQt5 import QtWebEngineWidgets


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
