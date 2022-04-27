import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QSpinBox, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.initializeUi()

    def initializeUi(self):
        self.setMinimumSize(300, 50)
        self.setWindowTitle("Nested Layout Example")
        self.setUpMainWindow()
        self.show()

    def setUpMainWindow(self):
        self.selectLabel = QLabel("Select 2 items for lunch and their prices.")
        self.selectLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        foods = ("egg", "turkey sandwich", "ham sandwich",
                 "cheese", "hummus", "yogurt", "apple", "banana",
                 "orange", "waffle", "carrots", "bread", "pasta",
                 "crackers", "pretzels", "coffee", "soda", "water")
        self.food1Combo = QComboBox()
        self.food1Combo.addItems(foods)
        self.food2Combo = QComboBox()
        self.food2Combo.addItems(foods)

        self.price1Spin = QSpinBox()
        self.price1Spin.setRange(0, 100)
        self.price1Spin.setPrefix("$")
        self.price1Spin.valueChanged.connect(self.sumPrices)
        self.price2Spin = QSpinBox()
        self.price2Spin.setRange(0, 100)
        self.price2Spin.setPrefix("$")
        self.price2Spin.valueChanged.connect(self.sumPrices)

        h1Box = QHBoxLayout()
        h1Box.addWidget(self.food1Combo)
        h1Box.addWidget(self.price1Spin)
        h2Box = QHBoxLayout()
        h2Box.addWidget(self.food2Combo)
        h2Box.addWidget(self.price2Spin)

        self.totalLabel = QLabel("Total spent:")
        self.totalLabel.setAlignment(Qt.AlignmentFlag.AlignRight)

        mainBox = QVBoxLayout()
        mainBox.addWidget(self.selectLabel)
        mainBox.addLayout(h1Box)
        mainBox.addLayout(h2Box)
        mainBox.addWidget(self.totalLabel)

        self.setLayout(mainBox)

    def sumPrices(self):
        self.totalLabel.setText(
            "Total value: $" + str(self.price1Spin.value() + self.price2Spin.value()))


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
