import sys
from PySide2.QtCore import QSize, Qt
from PySide2.QtGui import QBitmap, QIcon, QPixmap, QImage, QColor, qAlpha, QCursor
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QWidget
from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout, QGridLayout


def build(win):  ## noqa: N803
    win.setFixedSize(624, 468)
    win.setStyleSheet("QMainWindow {background-image: url(:/background)}")

    # Bulb Widget
    win.bulbs = []

    win.button = QPushButton()
    icon = QPixmap(":/b1")

    # print('ALPHA: ', icon.hasAlpha())
    win.button.setIcon(icon)
    win.button.setIconSize(QSize(81, 123))
    win.button.setFixedSize(QSize(81, 123))
    win.button.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
    win.button.setCursor(QCursor(Qt.PointingHandCursor))

    # win.button.move(20, 500)
    layout = QGridLayout()

    layout.addWidget(win.button, 0, 5)

    win.buttons_widget = QWidget()
    win.buttons_widget.setLayout(layout)
    win.setCentralWidget(win.buttons_widget)
