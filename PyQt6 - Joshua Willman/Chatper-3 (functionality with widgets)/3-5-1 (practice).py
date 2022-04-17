import sys
from registration import RegistrationWindow
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox


class LoginWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self) -> None:
        self.setGeometry(800, 300, 240, 170)
        self.setWindowTitle("Login GUI")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self) -> None:
        self.loginLabel = QLabel("Login", self)
        self.loginLabel.move(100, 10)

        self.usernameLabel = QLabel("Username:", self)
        self.usernameLabel.move(10, 35)

        self.usernameEdit = QLineEdit(self)
        self.usernameEdit.resize(160, 20)
        self.usernameEdit.move(70, 35)

        self.passwordEdit = QLabel("Password:", self)
        self.passwordEdit.move(10, 60)
        self.passwordEdit = QLineEdit(self)
        self.passwordEdit.resize(160, 20)
        self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)
        self.passwordEdit.move(70, 60)

        self.showCheck = QCheckBox("Show password", self)
        self.showCheck.move(70, 85)
        self.showCheck.toggled.connect(self.showPassword)

        self.loginButton = QPushButton("Login", self)
        self.loginButton.resize(220, 25)
        self.loginButton.move(10, 110)
        self.loginButton.pressed.connect(self.checkLogin)

        self.notMemberLabel = QLabel("Not a member?", self)
        self.notMemberLabel.move(10, 142)

        self.signUpButton = QPushButton("Sign Up", self)
        self.signUpButton.move(95, 140)
        self.signUpButton.clicked.connect(self.signUp)

    def showPassword(self, checked) -> None:
        if(checked):
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.passwordEdit.setEchoMode(QLineEdit.EchoMode.Password)

    def checkLogin(self) -> None:
        users = {}
        try:
            with open(r"Files\users.txt", "r") as file:
                for line in file:
                    user, password = str(line).split(" ")
                    users[user] = str(password).strip("\n")

            if((self.usernameEdit.text(), self.passwordEdit.text()) in users.items()):
                QMessageBox.information(
                    self, "Ingreso correcto", "Se ha ingresado correctamente", QMessageBox.StandardButton.Close)
                self.close()
            else:
                QMessageBox.warning(
                    self, "Icorrecto login", "No se ha podido ingresar con los datos ingresados", QMessageBox.StandardButton.Close)

        except FileNotFoundError:
            QMessageBox.warning(
                self, "Error en carga", "No fue posible cargar el archivo de usuarios", QMessageBox.StandardButton.Close)
            self.close()

    def signUp(self) -> None:
        self.registrationWindow = RegistrationWindow()


def main():
    app = QApplication(sys.argv)
    loginWindow = LoginWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
