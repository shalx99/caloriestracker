# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caloriestracker/ui/wdgMeals.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgMeals(object):
    def setupUi(self, wdgMeals):
        wdgMeals.setObjectName("wdgMeals")
        wdgMeals.resize(1012, 669)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(wdgMeals)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl = QtWidgets.QLabel(wdgMeals)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout_2.addWidget(self.lbl)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.calendar = QtWidgets.QCalendarWidget(wdgMeals)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.calendar.sizePolicy().hasHeightForWidth())
        self.calendar.setSizePolicy(sizePolicy)
        self.calendar.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.calendar.setObjectName("calendar")
        self.horizontalLayout.addWidget(self.calendar)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.tab = QtWidgets.QTabWidget(wdgMeals)
        self.tab.setObjectName("tab")
        self.tab_8 = QtWidgets.QWidget()
        self.tab_8.setObjectName("tab_8")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab_8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tblMeals = mqtwObjects(self.tab_8)
        self.tblMeals.setObjectName("tblMeals")
        self.verticalLayout.addWidget(self.tblMeals)
        self.lblFound = QtWidgets.QLabel(self.tab_8)
        self.lblFound.setObjectName("lblFound")
        self.verticalLayout.addWidget(self.lblFound)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/caloriestracker/meals.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_8, icon, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.wdgPieMeals = VCPie(self.tab_2)
        self.wdgPieMeals.setObjectName("wdgPieMeals")
        self.horizontalLayout_5.addWidget(self.wdgPieMeals)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/caloriestracker/pie.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_2, icon1, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_3)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.wdgPieFoodtypes = VCPie(self.tab_3)
        self.wdgPieFoodtypes.setObjectName("wdgPieFoodtypes")
        self.horizontalLayout_4.addWidget(self.wdgPieFoodtypes)
        self.tab.addTab(self.tab_3, icon1, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_4)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.wdgTS = VCTemporalSeries(self.tab_4)
        self.wdgTS.setObjectName("wdgTS")
        self.horizontalLayout_6.addWidget(self.wdgTS)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/caloriestracker/investment.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_4, icon2, "")
        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.wdgPieFulfillment = VCPie(self.tab_5)
        self.wdgPieFulfillment.setObjectName("wdgPieFulfillment")
        self.horizontalLayout_7.addWidget(self.wdgPieFulfillment)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/caloriestracker/button_ok.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tab.addTab(self.tab_5, icon3, "")
        self.verticalLayout_2.addWidget(self.tab)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.actionMealNew = QtWidgets.QAction(wdgMeals)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/caloriestracker/add.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMealNew.setIcon(icon4)
        self.actionMealNew.setObjectName("actionMealNew")
        self.actionMealDelete = QtWidgets.QAction(wdgMeals)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/caloriestracker/list-remove.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMealDelete.setIcon(icon5)
        self.actionMealDelete.setObjectName("actionMealDelete")
        self.actionMealEdit = QtWidgets.QAction(wdgMeals)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/caloriestracker/document-edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMealEdit.setIcon(icon6)
        self.actionMealEdit.setObjectName("actionMealEdit")
        self.actionProductEdit = QtWidgets.QAction(wdgMeals)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/caloriestracker/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionProductEdit.setIcon(icon7)
        self.actionProductEdit.setObjectName("actionProductEdit")
        self.actionMealDeleteDay = QtWidgets.QAction(wdgMeals)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/caloriestracker/button_cancel.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMealDeleteDay.setIcon(icon8)
        self.actionMealDeleteDay.setObjectName("actionMealDeleteDay")
        self.actionMealCopy = QtWidgets.QAction(wdgMeals)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/caloriestracker/copy.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMealCopy.setIcon(icon9)
        self.actionMealCopy.setObjectName("actionMealCopy")
        self.actionMealPaste = QtWidgets.QAction(wdgMeals)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/caloriestracker/paste.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionMealPaste.setIcon(icon10)
        self.actionMealPaste.setObjectName("actionMealPaste")

        self.retranslateUi(wdgMeals)
        self.tab.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(wdgMeals)

    def retranslateUi(self, wdgMeals):
        _translate = QtCore.QCoreApplication.translate
        self.lbl.setText(_translate("wdgMeals", "Your meals"))
        self.lblFound.setText(_translate("wdgMeals", "Registers found"))
        self.tab.setTabText(self.tab.indexOf(self.tab_8), _translate("wdgMeals", "Meals"))
        self.tab.setTabText(self.tab.indexOf(self.tab_2), _translate("wdgMeals", "Meals chart"))
        self.tab.setTabText(self.tab.indexOf(self.tab_3), _translate("wdgMeals", "Food types chart"))
        self.tab.setTabText(self.tab.indexOf(self.tab_4), _translate("wdgMeals", "Daily evolution"))
        self.tab.setTabText(self.tab.indexOf(self.tab_5), _translate("wdgMeals", "Daily fulfillment"))
        self.actionMealNew.setText(_translate("wdgMeals", "New meal"))
        self.actionMealNew.setToolTip(_translate("wdgMeals", "New meal"))
        self.actionMealDelete.setText(_translate("wdgMeals", "Delete meal"))
        self.actionMealDelete.setToolTip(_translate("wdgMeals", "Delete meal"))
        self.actionMealEdit.setText(_translate("wdgMeals", "Edit meal"))
        self.actionMealEdit.setToolTip(_translate("wdgMeals", "Edit meal"))
        self.actionProductEdit.setText(_translate("wdgMeals", "Edit product"))
        self.actionProductEdit.setToolTip(_translate("wdgMeals", "Edit product"))
        self.actionMealDeleteDay.setText(_translate("wdgMeals", "Delete selected date meals"))
        self.actionMealDeleteDay.setToolTip(_translate("wdgMeals", "Delete selected date meals"))
        self.actionMealCopy.setText(_translate("wdgMeals", "Copy meal"))
        self.actionMealCopy.setToolTip(_translate("wdgMeals", "Copy meal"))
        self.actionMealPaste.setText(_translate("wdgMeals", "Paste meal"))
        self.actionMealPaste.setToolTip(_translate("wdgMeals", "Paste meal"))
from caloriestracker.ui.myqcharts import VCPie, VCTemporalSeries
from caloriestracker.ui.myqtablewidget import mqtwObjects
import caloriestracker.images.caloriestracker_rc
