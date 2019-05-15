import sys
from PySide2.QtCore import QSize
from PySide2.QtGui import QBitmap, QIcon, QPixmap, QImage, QColor, qAlpha
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QWidget
from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout


def build(win):  ## noqa: N803
    win.setFixedSize(624, 468)
    win.setStyleSheet("QMainWindow {background-image: url(:/background)}")

    # Bulb Widget
    win.bulbs = []

    win.button = QPushButton()
    icon = QPixmap(":/b1")
    # icon = QPixmap("img/b1.png")
    # transparent_icon = _set_alpha_for_image_background(icon)
    # icon.
    print('ALPHA: ', icon.hasAlpha())
    win.button.setIcon(icon)
    win.button.setIconSize(QSize(81, 123))
    win.button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")

    win.edit = QLineEdit("What's up?")

    # win.button.move(20, 500)
    layout = QVBoxLayout()
    layout.addWidget(win.edit)
    layout.addWidget(win.button)

    win.edit_widget = QWidget()
    win.edit_widget.setLayout(layout)
    win.setCentralWidget(win.edit_widget)
