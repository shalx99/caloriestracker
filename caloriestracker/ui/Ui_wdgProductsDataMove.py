# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caloriestracker/ui/wdgProductsDataMove.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgProductsDataMove(object):
    def setupUi(self, wdgProductsDataMove):
        wdgProductsDataMove.setObjectName("wdgProductsDataMove")
        wdgProductsDataMove.setWindowModality(QtCore.Qt.WindowModal)
        wdgProductsDataMove.resize(634, 358)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(wdgProductsDataMove)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lblTitle = QtWidgets.QLabel(wdgProductsDataMove)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lblTitle.setFont(font)
        self.lblTitle.setText("")
        self.lblTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout.addWidget(self.lblTitle)
        self.lblExplanation = QtWidgets.QLabel(wdgProductsDataMove)
        self.lblExplanation.setAlignment(QtCore.Qt.AlignCenter)
        self.lblExplanation.setWordWrap(True)
        self.lblExplanation.setObjectName("lblExplanation")
        self.verticalLayout.addWidget(self.lblExplanation)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.wdg = mqtwObjects(wdgProductsDataMove)
        self.wdg.setObjectName("wdg")
        self.horizontalLayout.addWidget(self.wdg)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.bb = QtWidgets.QDialogButtonBox(wdgProductsDataMove)
        self.bb.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bb.setObjectName("bb")
        self.verticalLayout.addWidget(self.bb)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(wdgProductsDataMove)
        QtCore.QMetaObject.connectSlotsByName(wdgProductsDataMove)

    def retranslateUi(self, wdgProductsDataMove):
        _translate = QtCore.QCoreApplication.translate
        self.lblExplanation.setText(_translate("wdgProductsDataMove", "All product data will be moved from origin product to destiny one. If there are invesments created with origin product, they will be referenced to destiny product.\n"
"If origin is a user product, you can delete afterwards, because it won\'t have any data"))
from caloriestracker.ui.myqtablewidget import mqtwObjects
import caloriestracker.images.caloriestracker_rc
