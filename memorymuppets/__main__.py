import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QBitmap, QIcon, QPixmap, QImage, QColor, qAlpha, QCursor
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QWidget
from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout

import memorymuppets.resources  # noqa
from memorymuppets import ui
from random import randint


class MainWindow(QMainWindow):
    def __init__(self, name):
        super(MainWindow, self).__init__()

        self.setWindowTitle(name)
        ui.build(self)

        self.sequence = [randint(0, 5)]
        print(self.sequence)
        self.buttons_active = False

    def button_pressed(self, i):
        def button_response():
            print('Button number: ', i)
            if self.buttons_active:
                self.buttons[i].toggle_icon()
                if self.buttons[i].icon_number:
                    self.buttons[i].sound.play()
        return button_response

    def toggle_buttons_cursor(self):
        if self.buttons_active:
            self.setCursor(QCursor(Qt.PointingHandCursor))
        else:
            self.setCursor(QCursor(Qt.PointingHandCursor))


if __name__ == "__main__":
    appname = "Muppet Memory Game!"
    app = QApplication([])
    app.setApplicationName(appname)
    app.setWindowIcon(QIcon(":app"))
    win = MainWindow(appname)
    win.show()
    sys.exit(app.exec_())
