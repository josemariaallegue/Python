import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QAction


class EmptyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Main Window Template")
        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.show()

    def setUpMainWindow(self):
        pass

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.quitAct = QAction("Quit")
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.triggered.connect(self.close)

    def createMenu(self):
        """Create the application's menu bar."""
        self.menuBar().setNativeMenuBar(False)
        # Create file menu and add actions
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quitAct)


def main():
    app = QApplication(sys.argv)
    window = EmptyWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
