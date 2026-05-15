import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QComboBox,
    QVBoxLayout
)

from models.room import Room
from models.apartment import Apartment
from models.house import House

from export.to_doc import save_to_doc


class Window(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Расчёт помещения")
        self.setGeometry(100, 100, 300, 300)

        self.last_area = 0
        self.last_heat = 0

        self.length_input = QLineEdit()
        self.length_input.setPlaceholderText("Длина")

        self.width_input = QLineEdit()
        self.width_input.setPlaceholderText("Ширина")

        self.combo = QComboBox()
        self.combo.addItems(["Комната", "Квартира", "Дом"])

        self.result = QLabel("Результат")

        self.calc_button = QPushButton("Рассчитать")
        self.calc_button.clicked.connect(self.calculate)

        self.doc_button = QPushButton("Сохранить DOC")
        self.doc_button.clicked.connect(self.export_doc)

        layout = QVBoxLayout()

        layout.addWidget(self.length_input)
        layout.addWidget(self.width_input)
        layout.addWidget(self.combo)
        layout.addWidget(self.calc_button)
        layout.addWidget(self.result)
        layout.addWidget(self.doc_button)

        self.setLayout(layout)

    def calculate(self):

        length = float(self.length_input.text())
        width = float(self.width_input.text())

        room_type = self.combo.currentText()

        if room_type == "Комната":
            obj = Room(length, width)

        elif room_type == "Квартира":
            obj = Apartment(length, width)

        else:
            obj = House(length, width)

        area = obj.calc_area()
        heat = obj.calc_heat()

        self.last_area = area
        self.last_heat = heat

        self.result.setText(
            f"Площадь: {area:.2f} м²\n"
            f"Мощность: {heat:.2f} Вт"
        )

    def export_doc(self):

        save_to_doc(self.last_area, self.last_heat)

        self.result.setText("DOC файл сохранён")


app = QApplication(sys.argv)

window = Window()
window.show()

sys.exit(app.exec())