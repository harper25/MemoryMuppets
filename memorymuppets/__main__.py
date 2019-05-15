import sys
from PySide2.QtCore import QSize
from PySide2.QtGui import QBitmap, QIcon, QPixmap, QImage, QColor, qAlpha
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QWidget
from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout

import memorymuppets.resources  # noqa
from memorymuppets import ui


class MainWindow(QMainWindow):
    def __init__(self, name):
        super(MainWindow, self).__init__()

        self.setWindowTitle(name)
        ui.build(self)

    def greetings(self, number):
        def button_response():
            print('Button number: ', number)
            self.buttons[number].toggle_icon()
        return button_response


if __name__ == "__main__":
    appname = "Muppet Memory Game!"
    app = QApplication([])
    app.setApplicationName(appname)
    app.setWindowIcon(QIcon(":app"))
    win = MainWindow(appname)
    win.show()
    sys.exit(app.exec_())
