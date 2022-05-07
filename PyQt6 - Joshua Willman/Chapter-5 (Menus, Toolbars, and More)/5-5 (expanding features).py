import sys
from PyQt6.QtWidgets import (
    QApplication, QMainWindow, QTextEdit, QStatusBar, QToolBar, QDockWidget, QCheckBox, QVBoxLayout, QWidget)
from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtCore import QSize, Qt


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        """Set up the application's GUI."""
        self.setMinimumSize(450, 350)
        self.setWindowTitle("Main Window Template")
        self.setUpMainWindow()
        self.createActions()
        self.createMenu()
        self.createToolBar()
        self.createDock()
        self.statusBar().showMessage("Welcome!")
        self.show()

    def setUpMainWindow(self):
        """Create and arrange widgets in the main window."""
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.setStatusBar(QStatusBar())

    def createActions(self):
        """Create the application's menu actions."""
        # Create actions for File menu
        self.quit_act = QAction("&Quit")
        self.quit_act.setShortcut("Ctrl+Q")
        self.quit_act.setIcon(QIcon(r"Images\exit.png"))
        self.quit_act.triggered.connect(self.close)
        self.quit_act.setStatusTip("Quit program")

        self.fullScreenAct = QAction("Fullscreen", checkable=True)
        self.fullScreenAct.setStatusTip("Switch to full screen mode")
        self.fullScreenAct.triggered.connect(self.switchToFullScreen)

    def createMenu(self):
        """Create the application's menu bar."""
        self.menuBar().setNativeMenuBar(False)

        # Create file menu and add actions
        file_menu = self.menuBar().addMenu("File")
        file_menu.addAction(self.quit_act)

        viewMenu = self.menuBar().addMenu("View")
        appearanceSubMenu = viewMenu.addMenu("Appearance")
        appearanceSubMenu.addAction(self.fullScreenAct)

    def createToolBar(self):
        toolbar = QToolBar("Main Toolbar")
        toolbar.setIconSize(QSize(16, 16))
        self.addToolBar(toolbar)

        toolbar.addAction(self.quit_act)

    def createDock(self):
        dock = QDockWidget()
        dock.setWindowTitle("Formatting")
        dock.setAllowedAreas(Qt.DockWidgetArea.LeftDockWidgetArea)

        auto_bullet_cb = QCheckBox("Auto Bullet List")
        auto_bullet_cb.toggled.connect(self.changeTextEditSettings)

        # Create layout for dock widget
        dock_v_box = QVBoxLayout()
        dock_v_box.addWidget(auto_bullet_cb)
        dock_v_box.addStretch(1)

        # Create a QWidget that acts as a container to
        # hold other widgets
        dock_container = QWidget()
        dock_container.setLayout(dock_v_box)

        # Set the main widget for the dock widget
        dock.setWidget(dock_container)

        self.addDockWidget(Qt.DockWidgetArea.LeftDockWidgetArea, dock)

    def switchToFullScreen(self):
        if(self.isFullScreen()):
            self.showNormal()
        else:
            self.showFullScreen()

    def changeTextEditSettings(self, checked):
        """Change formatting features for QTextEdit."""
        if checked:
            self.textEdit.setAutoFormatting(
                QTextEdit.AutoFormattingFlag.AutoBulletList)
        else:
            self.textEdit.setAutoFormatting(
                QTextEdit.AutoFormattingFlag.AutoNone)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
