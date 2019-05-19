from PySide2 import QtMultimedia
from PySide2.QtCore import QSize, Qt, QUrl, QFileInfo, Signal
from PySide2.QtGui import QPixmap, QCursor
from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QPushButton, QVBoxLayout, QGridLayout


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


class PlayButton(QPushButton):
    def __init__(self):
        super(PlayButton, self).__init__("PLAY!")
        self.setFixedSize(QSize(400, 80))
        self.setCursor(QCursor(Qt.PointingHandCursor))
        self.defaultStyle = "background-color: rgba(255, 255, 255, 100); \
                             border-radius: 12px; \
                             font-size: 32px; \
                             color: #1C4B98; \
                             "
        self.setStyleSheet(self.defaultStyle)
        self.hoverStyle = self.defaultStyle.replace("rgba(255, 255, 255, 100)",
                                                    "rgba(255, 255, 255, 140)")
        self.active = True

    def enterEvent(self, event):
        self.setStyleSheet(self.hoverStyle)

    def leaveEvent(self, event):
        self.setStyleSheet(self.defaultStyle)


def build(win):
    win.setFixedSize(624, 468)
    win.setStyleSheet("QMainWindow {background-image: url(:/background)}")

    layout_buttons = QGridLayout()
    # layout_buttons.setHorizontalSpacing(25)  # win 25, mac 37
    win.muppets = []
    for i in range(6):
        win.muppets.append(MuppetButton(f":/b{i+1}", f":/b{i+1}a", i))
        layout_buttons.addWidget(win.muppets[i], 0, i)
        # layout_buttons.setColumnMinimumWidth(i, 91)  # win 91, mac 98
        win.muppets[i].sound = QtMultimedia.QMediaPlayer()
        win.muppets[i].sound.setMedia(QUrl(f"qrc:/s{i+1}"))
        win.muppets[i].signal.connect(win.muppet_pressed(i))

    # central widget
    win.central_widget = QWidget()
    central_layout = QVBoxLayout()
    central_layout.addWidget(win.central_widget)
    win.setCentralWidget(win.central_widget)

    # muppets widget
    win.buttons_widget = QWidget()
    win.buttons_widget.setFixedSize(QSize(624, 130))
    win.buttons_widget.setLayout(layout_buttons)
    win.buttons_widget.setParent(win.central_widget)
    win.buttons_widget.move(0, 225)

    # play button widget
    layout_play = QVBoxLayout()
    win.play_button = PlayButton()
    win.play_button.clicked.connect(win.play_button_pressed)
    layout_play.addWidget(win.play_button)
    win.play_widget = QWidget()
    win.play_widget.setLayout(layout_play)
    win.play_widget.setParent(win.central_widget)
    win.play_widget.move(112, 348)

    # sounds start & failure
    win.start = QtMultimedia.QMediaPlayer()
    win.start.setMedia(QUrl('qrc:/start'))
    win.end = QtMultimedia.QMediaPlayer()
    win.end.setMedia(QUrl('qrc:/end'))

    win.muppets[0].sound.play()
