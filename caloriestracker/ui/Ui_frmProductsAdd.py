# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caloriestracker/ui/frmProductsAdd.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_frmProductsAdd(object):
    def setupUi(self, frmProductsAdd):
        frmProductsAdd.setObjectName("frmProductsAdd")
        frmProductsAdd.setWindowModality(QtCore.Qt.WindowModal)
        frmProductsAdd.resize(600, 491)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/caloriestracker/books.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        frmProductsAdd.setWindowIcon(icon)
        frmProductsAdd.setModal(True)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(frmProductsAdd)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl = QtWidgets.QLabel(frmProductsAdd)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.lbl.setFont(font)
        self.lbl.setStyleSheet("color: rgb(0, 128, 0);")
        self.lbl.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl.setObjectName("lbl")
        self.verticalLayout_3.addWidget(self.lbl)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.label_15 = QtWidgets.QLabel(frmProductsAdd)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout_14.addWidget(self.label_15)
        self.txtName = QtWidgets.QLineEdit(frmProductsAdd)
        self.txtName.setObjectName("txtName")
        self.horizontalLayout_14.addWidget(self.txtName)
        self.verticalLayout_3.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(frmProductsAdd)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.cmbCompanies = QtWidgets.QComboBox(frmProductsAdd)
        self.cmbCompanies.setEditable(True)
        self.cmbCompanies.setObjectName("cmbCompanies")
        self.horizontalLayout_3.addWidget(self.cmbCompanies)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.groupBox = QtWidgets.QGroupBox(frmProductsAdd)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_5.addWidget(self.label_6)
        self.spnCalories = myQDoubleSpinBox(self.groupBox)
        self.spnCalories.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnCalories.setMaximum(1000000.0)
        self.spnCalories.setObjectName("spnCalories")
        self.horizontalLayout_5.addWidget(self.spnCalories)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.spnAmount = myQDoubleSpinBox(self.groupBox)
        self.spnAmount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnAmount.setMinimum(1.0)
        self.spnAmount.setMaximum(1000000.0)
        self.spnAmount.setProperty("value", 100.0)
        self.spnAmount.setObjectName("spnAmount")
        self.horizontalLayout.addWidget(self.spnAmount)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.spnCarbohydrate = myQDoubleSpinBox(self.groupBox)
        self.spnCarbohydrate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnCarbohydrate.setMaximum(1000000.0)
        self.spnCarbohydrate.setObjectName("spnCarbohydrate")
        self.horizontalLayout_2.addWidget(self.spnCarbohydrate)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_7.addWidget(self.label_8)
        self.spnProtein = myQDoubleSpinBox(self.groupBox)
        self.spnProtein.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnProtein.setMaximum(1000000.0)
        self.spnProtein.setObjectName("spnProtein")
        self.horizontalLayout_7.addWidget(self.spnProtein)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_6.addWidget(self.label_7)
        self.spnFat = myQDoubleSpinBox(self.groupBox)
        self.spnFat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnFat.setMaximum(1000000.0)
        self.spnFat.setObjectName("spnFat")
        self.horizontalLayout_6.addWidget(self.spnFat)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.spnFiber = myQDoubleSpinBox(self.groupBox)
        self.spnFiber.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnFiber.setMaximum(1000000.0)
        self.spnFiber.setObjectName("spnFiber")
        self.horizontalLayout_4.addWidget(self.spnFiber)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_15.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(frmProductsAdd)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_8.addWidget(self.label_9)
        self.spnSalt = myQDoubleSpinBox(self.groupBox_2)
        self.spnSalt.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnSalt.setMaximum(1000000.0)
        self.spnSalt.setObjectName("spnSalt")
        self.horizontalLayout_8.addWidget(self.spnSalt)
        self.verticalLayout_2.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_2)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_9.addWidget(self.label_10)
        self.spnCholesterol = myQDoubleSpinBox(self.groupBox_2)
        self.spnCholesterol.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnCholesterol.setMaximum(1000000.0)
        self.spnCholesterol.setObjectName("spnCholesterol")
        self.horizontalLayout_9.addWidget(self.spnCholesterol)
        self.verticalLayout_2.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox_2)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_10.addWidget(self.label_11)
        self.spnSodium = myQDoubleSpinBox(self.groupBox_2)
        self.spnSodium.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnSodium.setMaximum(1000000.0)
        self.spnSodium.setObjectName("spnSodium")
        self.horizontalLayout_10.addWidget(self.spnSodium)
        self.verticalLayout_2.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox_2)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_11.addWidget(self.label_12)
        self.spnPotassium = myQDoubleSpinBox(self.groupBox_2)
        self.spnPotassium.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnPotassium.setMaximum(1000000.0)
        self.spnPotassium.setObjectName("spnPotassium")
        self.horizontalLayout_11.addWidget(self.spnPotassium)
        self.verticalLayout_2.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox_2)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_12.addWidget(self.label_13)
        self.spnSugar = myQDoubleSpinBox(self.groupBox_2)
        self.spnSugar.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnSugar.setMaximum(1000000.0)
        self.spnSugar.setObjectName("spnSugar")
        self.horizontalLayout_12.addWidget(self.spnSugar)
        self.verticalLayout_2.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox_2)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_13.addWidget(self.label_14)
        self.spnSaturatedFat = myQDoubleSpinBox(self.groupBox_2)
        self.spnSaturatedFat.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.spnSaturatedFat.setMaximum(1000000.0)
        self.spnSaturatedFat.setObjectName("spnSaturatedFat")
        self.horizontalLayout_13.addWidget(self.spnSaturatedFat)
        self.verticalLayout_2.addLayout(self.horizontalLayout_13)
        self.horizontalLayout_15.addWidget(self.groupBox_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.bb = QtWidgets.QDialogButtonBox(frmProductsAdd)
        self.bb.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.bb.setObjectName("bb")
        self.verticalLayout_3.addWidget(self.bb)
        self.horizontalLayout_16.addLayout(self.verticalLayout_3)

        self.retranslateUi(frmProductsAdd)
        QtCore.QMetaObject.connectSlotsByName(frmProductsAdd)

    def retranslateUi(self, frmProductsAdd):
        _translate = QtCore.QCoreApplication.translate
        frmProductsAdd.setWindowTitle(_translate("frmProductsAdd", "Managing products"))
        self.label_15.setText(_translate("frmProductsAdd", "Name of the product"))
        self.label_2.setText(_translate("frmProductsAdd", "Select a company"))
        self.groupBox.setTitle(_translate("frmProductsAdd", "Basic components information"))
        self.label_6.setText(_translate("frmProductsAdd", "Calories"))
        self.spnCalories.setSuffix(_translate("frmProductsAdd", " g"))
        self.label_3.setText(_translate("frmProductsAdd", "Amount"))
        self.spnAmount.setSuffix(_translate("frmProductsAdd", " g"))
        self.label_4.setText(_translate("frmProductsAdd", "Carbohidrates"))
        self.spnCarbohydrate.setSuffix(_translate("frmProductsAdd", " g"))
        self.label_8.setText(_translate("frmProductsAdd", "Protein"))
        self.spnProtein.setSuffix(_translate("frmProductsAdd", " g"))
        self.label_7.setText(_translate("frmProductsAdd", "Fat"))
        self.spnFat.setSuffix(_translate("frmProductsAdd", " g"))
        self.label_5.setText(_translate("frmProductsAdd", "Fiber"))
        self.spnFiber.setSuffix(_translate("frmProductsAdd", " g"))
        self.groupBox_2.setTitle(_translate("frmProductsAdd", "Additional information"))
        self.label_9.setText(_translate("frmProductsAdd", "Salt"))
        self.spnSalt.setSuffix(_translate("frmProductsAdd", " g"))
        self.label_10.setText(_translate("frmProductsAdd", "Cholesterol"))
        self.spnCholesterol.setSuffix(_translate("frmProductsAdd", " mg"))
        self.label_11.setText(_translate("frmProductsAdd", "Sodium"))
        self.spnSodium.setSuffix(_translate("frmProductsAdd", " mg"))
        self.label_12.setText(_translate("frmProductsAdd", "Potassium"))
        self.spnPotassium.setSuffix(_translate("frmProductsAdd", " mg"))
        self.label_13.setText(_translate("frmProductsAdd", "Sugars"))
        self.spnSugar.setSuffix(_translate("frmProductsAdd", " g"))
        self.label_14.setText(_translate("frmProductsAdd", "Saturated fat"))
        self.spnSaturatedFat.setSuffix(_translate("frmProductsAdd", " g"))
from caloriestracker.ui.myqdoublespinbox import myQDoubleSpinBox
import caloriestracker.images.caloriestracker_rc
