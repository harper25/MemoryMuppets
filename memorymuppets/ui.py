import sys
from PySide2 import QtMultimedia
from PySide2.QtCore import QSize, Qt, QTimer, QObject, QUrl, QFile, QFileInfo
from PySide2.QtGui import QBitmap, QIcon, QPixmap, QImage, QColor, qAlpha, QCursor
from PySide2.QtWidgets import QApplication, QLabel, QLineEdit, QMainWindow, QWidget
from PySide2.QtWidgets import QDialog, QPushButton, QVBoxLayout, QGridLayout


class MuppetButton(QPushButton):
    signal = Signal(int)

    def __init__(self, icon, icon_active, number):
        super(MuppetButton, self).__init__()
        self.number = number
        self.icons = [QPixmap(icon), QPixmap(icon_active)]
        self.setIcon(self.icons[0])
        self.setIconSize(QSize(80, 130))
        self.setFixedSize(QSize(80, 80))
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.setStyleSheet("background-color: rgba(255, 255, 255, 30); \
                            border-radius: 12px;")

    def respond(self):
        self.sound.stop()
        self.setIcon(self.icons[1])
        self.sound.play()

    def unset_icon(self):
        self.setIcon(self.icons[0])

    def mousePressEvent(self, event):
        self.signal.emit(self.number)

    def mouseReleaseEvent(self, event):
        self.setIcon(self.icons[0])


    def enterEvent(self, event):
        self.setStyleSheet("background-color: rgba(255, 255, 255, 60); \
                            border-radius: 12px;")

    def leaveEvent(self, event):
        self.setStyleSheet("background-color: rgba(255, 255, 255, 30); \
                            border-radius: 12px;")


    def toggle_icon(self):
        self.icon_number = (self.icon_number + 1) % 2
        self.setIcon(self.icons[self.icon_number])


def build(win):  # # noqa: N803
    win.setFixedSize(624, 468)
    win.setStyleSheet("QMainWindow {background-image: url(:/background)}")

    layout_buttons = QGridLayout()
    win.buttons = []
    for i in range(6):
        win.buttons.append(MuppetButton(f":/b{i+1}", f":/b{i+1}a"))
        # win.buttons[i].sound = QtMultimedia.QSound(f':/memorymuppets/sounds/s{i + 1}.mp3')
        layout_buttons.addWidget(win.buttons[i], 0, i)
        layout_buttons.setColumnMinimumWidth(i, 91)
        path_to_sound = QFileInfo(f"sounds/s{i + 1}.mp3").absoluteFilePath()
        win.buttons[i].sound = QtMultimedia.QMediaPlayer()
        win.buttons[i].sound.setMedia(QUrl.fromLocalFile(path_to_sound))
        win.buttons[i].clicked.connect(win.button_pressed(i))

    # win.buttons[0].sound.setMedia(QUrl.fromLocalFile('E:/python_venv/MemoryMuppets/memorymuppets/s1.mp3'))
    # win.buttons[0].sound.play()

    win.central_widget = QWidget()
    central_layout = QVBoxLayout()
    central_layout.addWidget(win.central_widget)
    win.setCentralWidget(win.central_widget)

    win.buttons_widget = QWidget()
    win.buttons_widget.setLayout(layout_buttons)
    win.buttons_widget.setParent(win.central_widget)
    win.buttons_widget.move(0, 225)
    # layout_buttons.setHorizontalSpacing(25)
    # layout_buttons.setHorizontalSpacing(37)
