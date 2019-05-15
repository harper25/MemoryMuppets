import sys
from PySide2.QtCore import QSize
from PySide2.QtGui import QBitmap, QIcon, QPixmap, QImage, QColor, qAlpha
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QWidget
from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout

import memorymuppets.resources  # noqa


class MainWindow(QMainWindow):
    def __init__(self, name):
        super(MainWindow, self).__init__()

        self.setWindowTitle(name)
        self.setFixedSize(624, 468)
        self.setStyleSheet("QMainWindow {background-image: url(:/background)}")


        # Bulb Widget
        self.bulbs = []

        self.button = QPushButton()
        icon = QPixmap(":/b1")
        # icon = QPixmap("img/b1.png")
        # transparent_icon = _set_alpha_for_image_background(icon)
        # icon.
        print('ALPHA: ', icon.hasAlpha())
        self.button.setIcon(icon)
        self.button.setIconSize(QSize(81, 123))
        self.button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")


        self.edit = QLineEdit("What's up?")


        # self.button.move(20, 500)
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button)

        self.edit_widget = QWidget()
        self.edit_widget.setLayout(layout)
        self.setCentralWidget(self.edit_widget)



        # # edit widget
        # self.edit = QLineEdit("What's up?")
        # self.button = QPushButton("Print to stdout")
        # # self.button.move(20, 500)
        # layout = QVBoxLayout()
        # layout.addWidget(self.edit)
        # layout.addWidget(self.button)

        # self.edit_widget = QWidget()
        # self.edit_widget.setLayout(layout)
        # self.setCentralWidget(self.edit_widget)

        # signals
        self.button.clicked.connect(self.greetings)


    def greetings(self):
        text = self.edit.text()
        print('Contents of QLineEdit widget: {}'.format(text))
        self.button.setIcon(QPixmap(":/b1a"))



if __name__ == "__main__":
    appname = "Muppet Memory Game!"
    app = QApplication([])
    app.setApplicationName(appname)
    app.setWindowIcon(QIcon(":app"))
    win = MainWindow(appname)
    win.show()
    sys.exit(app.exec_())
