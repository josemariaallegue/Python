# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(449, 406)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(449, 406))
        Form.setMaximumSize(QtCore.QSize(449, 406))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(90, 90, 90))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.Window, brush)
        Form.setPalette(palette)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.titleLabel = QtWidgets.QLabel(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.titleLabel.sizePolicy().hasHeightForWidth())
        self.titleLabel.setSizePolicy(sizePolicy)
        self.titleLabel.setMaximumSize(QtCore.QSize(421, 31))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Active, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Inactive, QtGui.QPalette.ColorRole.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.BrushStyle.SolidPattern)
        palette.setBrush(QtGui.QPalette.ColorGroup.Disabled, QtGui.QPalette.ColorRole.WindowText, brush)
        self.titleLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        self.titleLabel.setFont(font)
        self.titleLabel.setTextFormat(QtCore.Qt.TextFormat.PlainText)
        self.titleLabel.setScaledContents(True)
        self.titleLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.titleLabel.setObjectName("titleLabel")
        self.verticalLayout.addWidget(self.titleLabel)
        self.inputFrame = QtWidgets.QFrame(Form)
        self.inputFrame.setMinimumSize(QtCore.QSize(431, 91))
        self.inputFrame.setMaximumSize(QtCore.QSize(431, 91))
        self.inputFrame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.inputFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.inputFrame.setLineWidth(3)
        self.inputFrame.setMidLineWidth(5)
        self.inputFrame.setObjectName("inputFrame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.inputFrame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.inputLayout = QtWidgets.QHBoxLayout()
        self.inputLayout.setObjectName("inputLayout")
        self.number1Edit = QtWidgets.QLineEdit(self.inputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number1Edit.sizePolicy().hasHeightForWidth())
        self.number1Edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.number1Edit.setFont(font)
        self.number1Edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.number1Edit.setObjectName("number1Edit")
        self.inputLayout.addWidget(self.number1Edit)
        self.number2Edit = QtWidgets.QLineEdit(self.inputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number2Edit.sizePolicy().hasHeightForWidth())
        self.number2Edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.number2Edit.setFont(font)
        self.number2Edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.number2Edit.setObjectName("number2Edit")
        self.inputLayout.addWidget(self.number2Edit)
        self.number3Edit = QtWidgets.QLineEdit(self.inputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number3Edit.sizePolicy().hasHeightForWidth())
        self.number3Edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.number3Edit.setFont(font)
        self.number3Edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.number3Edit.setObjectName("number3Edit")
        self.inputLayout.addWidget(self.number3Edit)
        self.number4Edit = QtWidgets.QLineEdit(self.inputFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number4Edit.sizePolicy().hasHeightForWidth())
        self.number4Edit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(30)
        self.number4Edit.setFont(font)
        self.number4Edit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.number4Edit.setObjectName("number4Edit")
        self.inputLayout.addWidget(self.number4Edit)
        self.gridLayout_2.addLayout(self.inputLayout, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.inputFrame)
        self.padFrame = QtWidgets.QFrame(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.padFrame.sizePolicy().hasHeightForWidth())
        self.padFrame.setSizePolicy(sizePolicy)
        self.padFrame.setMaximumSize(QtCore.QSize(431, 251))
        self.padFrame.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.padFrame.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.padFrame.setLineWidth(2)
        self.padFrame.setMidLineWidth(5)
        self.padFrame.setObjectName("padFrame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.padFrame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.numberLayout = QtWidgets.QGridLayout()
        self.numberLayout.setObjectName("numberLayout")
        self.number5Button = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number5Button.sizePolicy().hasHeightForWidth())
        self.number5Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number5Button.setFont(font)
        self.number5Button.setObjectName("number5Button")
        self.numberLayout.addWidget(self.number5Button, 1, 1, 1, 1)
        self.number3Button = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number3Button.sizePolicy().hasHeightForWidth())
        self.number3Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number3Button.setFont(font)
        self.number3Button.setObjectName("number3Button")
        self.numberLayout.addWidget(self.number3Button, 2, 2, 1, 1)
        self.number9Button = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number9Button.sizePolicy().hasHeightForWidth())
        self.number9Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number9Button.setFont(font)
        self.number9Button.setCheckable(False)
        self.number9Button.setObjectName("number9Button")
        self.numberLayout.addWidget(self.number9Button, 0, 2, 1, 1)
        self.numberAButton = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberAButton.sizePolicy().hasHeightForWidth())
        self.numberAButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.numberAButton.setFont(font)
        self.numberAButton.setObjectName("numberAButton")
        self.numberLayout.addWidget(self.numberAButton, 3, 0, 1, 1)
        self.number4Button = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number4Button.sizePolicy().hasHeightForWidth())
        self.number4Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number4Button.setFont(font)
        self.number4Button.setObjectName("number4Button")
        self.numberLayout.addWidget(self.number4Button, 1, 0, 1, 1)
        self.number0Button = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number0Button.sizePolicy().hasHeightForWidth())
        self.number0Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number0Button.setFont(font)
        self.number0Button.setObjectName("number0Button")
        self.numberLayout.addWidget(self.number0Button, 3, 1, 1, 1)
        self.number8Button = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number8Button.sizePolicy().hasHeightForWidth())
        self.number8Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number8Button.setFont(font)
        self.number8Button.setObjectName("number8Button")
        self.numberLayout.addWidget(self.number8Button, 0, 1, 1, 1)
        self.number6Button = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number6Button.sizePolicy().hasHeightForWidth())
        self.number6Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number6Button.setFont(font)
        self.number6Button.setObjectName("number6Button")
        self.numberLayout.addWidget(self.number6Button, 1, 2, 1, 1)
        self.numberBButton = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.numberBButton.sizePolicy().hasHeightForWidth())
        self.numberBButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.numberBButton.setFont(font)
        self.numberBButton.setObjectName("numberBButton")
        self.numberLayout.addWidget(self.numberBButton, 3, 2, 1, 1)
        self.number7Button = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number7Button.sizePolicy().hasHeightForWidth())
        self.number7Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number7Button.setFont(font)
        self.number7Button.setObjectName("number7Button")
        self.numberLayout.addWidget(self.number7Button, 0, 0, 1, 1)
        self.number1Button = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number1Button.sizePolicy().hasHeightForWidth())
        self.number1Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number1Button.setFont(font)
        self.number1Button.setObjectName("number1Button")
        self.numberLayout.addWidget(self.number1Button, 2, 0, 1, 1)
        self.number2Button = QtWidgets.QPushButton(self.padFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.number2Button.sizePolicy().hasHeightForWidth())
        self.number2Button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(28)
        self.number2Button.setFont(font)
        self.number2Button.setObjectName("number2Button")
        self.numberLayout.addWidget(self.number2Button, 2, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.numberLayout)
        self.verticalLayout.addWidget(self.padFrame)

        self.retranslateUi(Form)
        self.numberAButton.clicked.connect(self.number1Edit.clear) # type: ignore
        self.numberAButton.clicked.connect(self.number2Edit.clear) # type: ignore
        self.numberAButton.clicked.connect(self.number3Edit.clear) # type: ignore
        self.numberAButton.clicked.connect(self.number4Edit.clear) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.number1Edit, self.number2Edit)
        Form.setTabOrder(self.number2Edit, self.number3Edit)
        Form.setTabOrder(self.number3Edit, self.number4Edit)
        Form.setTabOrder(self.number4Edit, self.number7Button)
        Form.setTabOrder(self.number7Button, self.number8Button)
        Form.setTabOrder(self.number8Button, self.number9Button)
        Form.setTabOrder(self.number9Button, self.number4Button)
        Form.setTabOrder(self.number4Button, self.number5Button)
        Form.setTabOrder(self.number5Button, self.number6Button)
        Form.setTabOrder(self.number6Button, self.number1Button)
        Form.setTabOrder(self.number1Button, self.number2Button)
        Form.setTabOrder(self.number2Button, self.number3Button)
        Form.setTabOrder(self.number3Button, self.numberAButton)
        Form.setTabOrder(self.numberAButton, self.number0Button)
        Form.setTabOrder(self.number0Button, self.numberBButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "8.1 - Keypad GUI"))
        self.titleLabel.setText(_translate("Form", "Enter a passcode"))
        self.number5Button.setText(_translate("Form", "5"))
        self.number3Button.setText(_translate("Form", "3"))
        self.number9Button.setText(_translate("Form", "9"))
        self.numberAButton.setText(_translate("Form", "*"))
        self.number4Button.setText(_translate("Form", "4"))
        self.number0Button.setText(_translate("Form", "0"))
        self.number8Button.setText(_translate("Form", "8"))
        self.number6Button.setText(_translate("Form", "6"))
        self.numberBButton.setText(_translate("Form", "#"))
        self.number7Button.setText(_translate("Form", "7"))
        self.number1Button.setText(_translate("Form", "1"))
        self.number2Button.setText(_translate("Form", "2"))
