"""Listing 8-11 to Listing 8-15
Written by Joshua Willman
Featured in "Beginning PyQt - A Hands-on Approach to GUI Programming, 2nd Ed."
"""

# Import necessary modules
import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QMessageBox)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIntValidator
from keyPadGui import Ui_keyPad

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_keyPad()
        self.ui.setupUi(self)

        self.initializeUI()
        self.show()

    def initializeUI(self):
        """Set up the application's GUI."""
        # Update other line_edit features
        self.ui.number1Edit.setMaxLength(1) # Set the max number of characters allowed
        self.ui.number1Edit.setValidator(QIntValidator(0, 9)) # User can only enter ints from 0-9
        self.ui.number1Edit.setFocusPolicy(Qt.FocusPolicy.NoFocus) # Widget does not except focus

        self.ui.number2Edit.setMaxLength(1) 
        self.ui.number2Edit.setValidator(QIntValidator(0, 9)) 
        self.ui.number2Edit.setFocusPolicy(Qt.FocusPolicy.NoFocus) 

        self.ui.number3Edit.setMaxLength(1) 
        self.ui.number3Edit.setValidator(QIntValidator(0, 9)) 
        self.ui.number3Edit.setFocusPolicy(Qt.FocusPolicy.NoFocus) 

        self.ui.number4Edit.setMaxLength(1) 
        self.ui.number4Edit.setValidator(QIntValidator(0, 9)) 
        self.ui.number4Edit.setFocusPolicy(Qt.FocusPolicy.NoFocus) 

        # 4-digit passcode
        self.passcode = 8618
        
        # Add signal/slot connections for buttons
        self.ui.number0Button.clicked.connect(lambda: self.numberClicked(self.ui.number0Button.text()))
        self.ui.number1Button.clicked.connect(lambda: self.numberClicked(self.ui.number1Button.text()))
        self.ui.number2Button.clicked.connect(lambda: self.numberClicked(self.ui.number2Button.text()))
        self.ui.number3Button.clicked.connect(lambda: self.numberClicked(self.ui.number3Button.text()))
        self.ui.number4Button.clicked.connect(lambda: self.numberClicked(self.ui.number4Button.text()))
        self.ui.number5Button.clicked.connect(lambda: self.numberClicked(self.ui.number5Button.text()))
        self.ui.number6Button.clicked.connect(lambda: self.numberClicked(self.ui.number6Button.text()))
        self.ui.number7Button.clicked.connect(lambda: self.numberClicked(self.ui.number7Button.text()))
        self.ui.number8Button.clicked.connect(lambda: self.numberClicked(self.ui.number8Button.text()))
        self.ui.number9Button.clicked.connect(lambda: self.numberClicked(self.ui.number9Button.text()))

        self.ui.numberBButton.clicked.connect(self.checkPasscode)

    def numberClicked(self, text_value):
        """When a button with a digit is pressed, check if 
        the text for QLineEdit widgets are empty. If empty, 
        set the focus to the correct widget and enter text value."""
        if self.ui.number1Edit.text() == "":
            self.ui.number1Edit.setFocus()
            self.ui.number1Edit.setText(text_value)
            self.ui.number1Edit.repaint()
        elif (self.ui.number1Edit.text() != "") and (self.ui.number2Edit.text() == ""):
            self.ui.number2Edit.setFocus()
            self.ui.number2Edit.setText(text_value)
            self.ui.number2Edit.repaint()
        elif (self.ui.number1Edit.text() != "") and (self.ui.number2Edit.text() != "") \
            and (self.ui.number3Edit.text() == ""):
            self.ui.number3Edit.setFocus()
            self.ui.number3Edit.setText(text_value)
            self.ui.number3Edit.repaint()
        elif (self.ui.number1Edit.text() != "") and (self.ui.number2Edit.text() != "") \
            and (self.ui.number3Edit.text() != "") and (self.ui.number4Edit.text() == ""):
            self.ui.number4Edit.setFocus()
            self.ui.number4Edit.setText(text_value)
            self.ui.number4Edit.repaint()
        
    def checkPasscode(self):
        """Concatenate the text values from the 4 QLineEdit widgets,
        and check to see if the passcode entered by user matches 
        existing passcode."""
        entered_passcode = self.ui.number1Edit.text() + self.ui.number2Edit.text() + \
            self.ui.number3Edit.text() +  self.ui.number4Edit.text()
        if len(entered_passcode) == 4 and int(entered_passcode) == self.passcode:
            QMessageBox.information(self, "Valid Passcode!", "Valid Passcode!", 
                QMessageBox.StandardButton.Ok)
            self.close()
        else:
            QMessageBox.warning(self, "Error Message", "Invalid Passcode.", 
                QMessageBox.StandardButton.Close)
            self.ui.number1Edit.clear()
            self.ui.number2Edit.clear()
            self.ui.number3Edit.clear()
            self.ui.number4Edit.clear()
            self.ui.number1Edit.setFocus()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Keypad = MainWindow()
    sys.exit(app.exec())