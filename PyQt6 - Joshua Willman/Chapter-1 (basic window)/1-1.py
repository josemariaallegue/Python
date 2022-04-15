# importaciones necesarias
import sys
from PyQt6.QtWidgets import QApplication, QWidget

# metodo a travez de clase
# siempre deriva de QMainWindow, QWidget, or QDialog


class EmptyWindow(QWidget):

    # en el init se hace un super del init
    # se corre la funciona inicializadora
    def __init__(self):
        """ Constructor for Empty Window Class """
        super().__init__()
        self.initializeUI()

    # funcion inicializadora donde se establecen, entre
    # otras cosas, la dimension de la ventana y el titulo
    # se corre show para mostrar la ventana
    def initializeUI(self):
        """Set up the application."""
        self.setGeometry(200, 100, 400, 300)
        self.setWindowTitle("Empty Window in PyQt")
        self.show()  # Display the window on the screen


def main():

    # app se encarga del main event loop
    app = QApplication(sys.argv)
    # se crea un objeto de la ventana
    window = EmptyWindow()
    # sys se encarga del cierre y app de la ejecucion
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
