import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QLineEdit,
    QMessageBox
)

from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

from PIL.ImageQt import ImageQt

from meme_generator import MemeGenerator
from exceptions import ImageNotLoadedError, SaveImageError


class MemeApp(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор мемов")
        self.setGeometry(300, 200, 600, 600)

        self.image_path = None
        self.generated_image = None

        self.init_ui()

    def init_ui(self):

        self.layout = QVBoxLayout()

        self.image_label = QLabel("Изображение не загружено")
        self.image_label.setAlignment(Qt.AlignCenter)

        self.top_text = QLineEdit()
        self.top_text.setPlaceholderText("Введите верхний текст")

        self.bottom_text = QLineEdit()
        self.bottom_text.setPlaceholderText("Введите нижний текст")

        self.load_button = QPushButton("Загрузить изображение")
        self.generate_button = QPushButton("Создать мем")
        self.save_button = QPushButton("Сохранить мем")

        self.load_button.clicked.connect(self.load_image)
        self.generate_button.clicked.connect(self.generate_meme)
        self.save_button.clicked.connect(self.save_meme)

        self.layout.addWidget(self.image_label)
        self.layout.addWidget(self.top_text)
        self.layout.addWidget(self.bottom_text)
        self.layout.addWidget(self.load_button)
        self.layout.addWidget(self.generate_button)
        self.layout.addWidget(self.save_button)

        self.setLayout(self.layout)

    def load_image(self):

        file_name, _ = QFileDialog.getOpenFileName(
            self,
            "Выберите изображение",
            "",
            "Images (*.png *.jpg *.jpeg)"
        )

        if file_name:
            self.image_path = file_name

            pixmap = QPixmap(file_name)
            pixmap = pixmap.scaled(
                500,
                400,
                Qt.KeepAspectRatio
            )

            self.image_label.setPixmap(pixmap)

    def generate_meme(self):

        try:

            if not self.image_path:
                raise ImageNotLoadedError(
                    "Сначала загрузите изображение!"
                )

            generator = MemeGenerator(self.image_path)

            self.generated_image = generator.add_text(
                self.top_text.text(),
                self.bottom_text.text()
            )

            qt_image = ImageQt(self.generated_image)

            pixmap = QPixmap.fromImage(qt_image)

            pixmap = pixmap.scaled(
                500,
                400,
                Qt.KeepAspectRatio
            )

            self.image_label.setPixmap(pixmap)

        except ImageNotLoadedError as e:
            QMessageBox.warning(self, "Ошибка", str(e))

        except Exception as e:
            QMessageBox.critical(
                self,
                "Неизвестная ошибка",
                str(e)
            )

    def save_meme(self):

        try:

            if self.generated_image is None:
                raise SaveImageError(
                    "Сначала создайте мем!"
                )

            file_name, _ = QFileDialog.getSaveFileName(
                self,
                "Сохранить мем",
                "",
                "PNG Files (*.png)"
            )

            if file_name:
                self.generated_image.save(file_name)

                QMessageBox.information(
                    self,
                    "Успех",
                    "Мем успешно сохранён!"
                )

        except SaveImageError as e:
            QMessageBox.warning(self, "Ошибка", str(e))

        except Exception as e:
            QMessageBox.critical(
                self,
                "Ошибка сохранения",
                str(e)
            )


if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MemeApp()
    window.show()

    sys.exit(app.exec())