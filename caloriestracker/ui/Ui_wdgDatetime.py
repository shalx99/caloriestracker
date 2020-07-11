# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'caloriestracker/ui/wdgDatetime.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wdgDatetime(object):
    def setupUi(self, wdgDatetime):
        wdgDatetime.setObjectName("wdgDatetime")
        wdgDatetime.resize(508, 296)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(wdgDatetime.sizePolicy().hasHeightForWidth())
        wdgDatetime.setSizePolicy(sizePolicy)
        self.horizontalLayout = QtWidgets.QHBoxLayout(wdgDatetime)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.grp = QtWidgets.QGroupBox(wdgDatetime)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.grp.sizePolicy().hasHeightForWidth())
        self.grp.setSizePolicy(sizePolicy)
        self.grp.setObjectName("grp")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.grp)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.teDate = QtWidgets.QCalendarWidget(self.grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teDate.sizePolicy().hasHeightForWidth())
        self.teDate.setSizePolicy(sizePolicy)
        self.teDate.setFirstDayOfWeek(QtCore.Qt.Monday)
        self.teDate.setVerticalHeaderFormat(QtWidgets.QCalendarWidget.NoVerticalHeader)
        self.teDate.setObjectName("teDate")
        self.horizontalLayout_2.addWidget(self.teDate)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.teTime = QtWidgets.QTimeEdit(self.grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teTime.sizePolicy().hasHeightForWidth())
        self.teTime.setSizePolicy(sizePolicy)
        self.teTime.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.teTime.setObjectName("teTime")
        self.verticalLayout.addWidget(self.teTime)
        self.teMicroseconds = QtWidgets.QSpinBox(self.grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.teMicroseconds.sizePolicy().hasHeightForWidth())
        self.teMicroseconds.setSizePolicy(sizePolicy)
        self.teMicroseconds.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.teMicroseconds.setMaximum(999999)
        self.teMicroseconds.setObjectName("teMicroseconds")
        self.verticalLayout.addWidget(self.teMicroseconds)
        self.cmbZone = QtWidgets.QComboBox(self.grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmbZone.sizePolicy().hasHeightForWidth())
        self.cmbZone.setSizePolicy(sizePolicy)
        self.cmbZone.setEditable(True)
        self.cmbZone.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.cmbZone.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.cmbZone.setObjectName("cmbZone")
        self.verticalLayout.addWidget(self.cmbZone)
        self.line = QtWidgets.QFrame(self.grp)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.cmdNow = QtWidgets.QPushButton(self.grp)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmdNow.sizePolicy().hasHeightForWidth())
        self.cmdNow.setSizePolicy(sizePolicy)
        self.cmdNow.setObjectName("cmdNow")
        self.verticalLayout.addWidget(self.cmdNow)
        self.lineNone = QtWidgets.QFrame(self.grp)
        self.lineNone.setFrameShape(QtWidgets.QFrame.HLine)
        self.lineNone.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.lineNone.setObjectName("lineNone")
        self.verticalLayout.addWidget(self.lineNone)
        self.chkNone = QtWidgets.QCheckBox(self.grp)
        self.chkNone.setObjectName("chkNone")
        self.verticalLayout.addWidget(self.chkNone)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        self.horizontalLayout.addWidget(self.grp)

        self.retranslateUi(wdgDatetime)
        QtCore.QMetaObject.connectSlotsByName(wdgDatetime)

    def retranslateUi(self, wdgDatetime):
        _translate = QtCore.QCoreApplication.translate
        self.grp.setTitle(_translate("wdgDatetime", "Select a datetime"))
        self.teTime.setToolTip(_translate("wdgDatetime", "Select a time"))
        self.teTime.setDisplayFormat(_translate("wdgDatetime", "HH:mm:ss"))
        self.teMicroseconds.setToolTip(_translate("wdgDatetime", "Select microseconds"))
        self.cmdNow.setToolTip(_translate("wdgDatetime", "Set current time"))
        self.cmdNow.setText(_translate("wdgDatetime", "Now"))
        self.chkNone.setText(_translate("wdgDatetime", "Sets a null value"))
