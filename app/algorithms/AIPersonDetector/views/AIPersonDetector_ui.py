# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\charl\source\repos\crgrove\adiat_ai\resources/views/algorithms/AIPersonDetector.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AIPersonDetector(object):
    def setupUi(self, AIPersonDetector):
        AIPersonDetector.setObjectName("AIPersonDetector")
        AIPersonDetector.resize(674, 70)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(AIPersonDetector)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.confidenceLabel = QtWidgets.QLabel(AIPersonDetector)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.confidenceLabel.setFont(font)
        self.confidenceLabel.setObjectName("confidenceLabel")
        self.horizontalLayout.addWidget(self.confidenceLabel)
        self.confidenceSlider = QtWidgets.QSlider(AIPersonDetector)
        self.confidenceSlider.setMinimum(-1)
        self.confidenceSlider.setMaximum(100)
        self.confidenceSlider.setPageStep(1)
        self.confidenceSlider.setProperty("value", 50)
        self.confidenceSlider.setOrientation(QtCore.Qt.Horizontal)
        self.confidenceSlider.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.confidenceSlider.setTickInterval(1)
        self.confidenceSlider.setObjectName("confidenceSlider")
        self.horizontalLayout.addWidget(self.confidenceSlider)
        self.confidenceValueLabel = QtWidgets.QLabel(AIPersonDetector)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.confidenceValueLabel.setFont(font)
        self.confidenceValueLabel.setObjectName("confidenceValueLabel")
        self.horizontalLayout.addWidget(self.confidenceValueLabel)
        self.verticalLayout_4.addLayout(self.horizontalLayout)
        self.GPULabel = QtWidgets.QLabel(AIPersonDetector)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.GPULabel.setFont(font)
        self.GPULabel.setObjectName("GPULabel")
        self.verticalLayout_4.addWidget(self.GPULabel)

        self.retranslateUi(AIPersonDetector)
        QtCore.QMetaObject.connectSlotsByName(AIPersonDetector)

    def retranslateUi(self, AIPersonDetector):
        _translate = QtCore.QCoreApplication.translate
        AIPersonDetector.setWindowTitle(_translate("AIPersonDetector", "Form"))
        self.confidenceLabel.setText(_translate("AIPersonDetector", "Confidence Threshold"))
        self.confidenceValueLabel.setText(_translate("AIPersonDetector", "50"))
        self.GPULabel.setText(_translate("AIPersonDetector", "GPU Label"))
from . import resources_rc
