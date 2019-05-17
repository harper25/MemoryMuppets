import sys
from PySide2.QtCore import Qt, QTimer
from PySide2.QtGui import QCursor, QIcon, QFontDatabase
from PySide2.QtWidgets import QApplication, QMainWindow

import memorymuppets.resources  # noqa
from memorymuppets import ui
from random import randint


class MainWindow(QMainWindow):
    def __init__(self, name):
        super(MainWindow, self).__init__()

        # user interface
        self.setWindowTitle(name)
        ui.build(self)

        # game variables
        self.muppets_active = True
        self.game = False
        self.sequence = []
        self.counter_ok = -1
        self.counter_sequence = -2
        self.timer = QTimer()
        self.timer.timeout.connect(self.play_sequence)

    def toggle_buttons_cursor(self):
        if self.muppets_active:
            self.setCursor(QCursor(Qt.PointingHandCursor))
        else:
            self.setCursor(QCursor(Qt.ArrowCursor))

    def tick(self):
        self.timer.stop()
        # self.timer.start(1000)
        # self.timer.timeout.connect(self.tick)
        # self.timer.start(1000)

    def muppet_pressed(self, i):
        def button_response():
            print('Button number: ', i)
            if self.game and self.muppets_active:
                self.check_sequence(i)
            elif self.muppets_active:
                self.muppets[i].respond()
        return button_response

    def play_button_pressed(self):
        if not self.game:
            self.game = True
            self.sequence = []
            self.timer.start(100)

    def play_sequence(self):
        self.counter_sequence += 1
        print(self.counter_sequence)
        if self.counter_sequence == -1:
            self.muppets_active = False
            self.play_button.setCursor(QCursor(Qt.ArrowCursor))
            self.play_button.setText("Now, remember...")
            self.timer.start(1000)
        elif self.counter_sequence == 0:
            self.sequence.append(randint(0, 5))
            muppet = self.sequence[self.counter_sequence]
            self.muppets[muppet].respond()
        elif self.counter_sequence < len(self.sequence):
            previous_muppet = self.sequence[self.counter_sequence - 1]
            self.muppets[previous_muppet].unset_icon()
            muppet = self.sequence[self.counter_sequence]
            self.muppets[muppet].respond()
        else:
            previous_muppet = self.sequence[self.counter_sequence - 1]
            self.muppets[previous_muppet].unset_icon()
            self.timer.stop()
            self.muppets_active = True
            self.play_button.setText("Repeat...")
            # self.toggle_buttons_cursor()

    def check_sequence(self, i):
        self.counter_ok += 1
        if not self.sequence[self.counter_ok] == i:
            self.end.play()
            self.game = False
            self.play_button.setCursor(QCursor(Qt.PointingHandCursor))
            self.play_button.setText(
                f"Nope! Score: {len(self.sequence) - 1}. Play?")
            self.counter_ok = -1
            self.counter_sequence = -2
        elif self.counter_ok < len(self.sequence) - 1:
            self.muppets[i].respond()
        else:
            self.muppets[i].respond()
            self.play_button.setText(
                f"Yes! Score: {len(self.sequence)}")
            self.counter_ok = -1
            self.counter_sequence = -2
            self.timer.start(1000)


if __name__ == "__main__":
    appname = "Muppet Memory Game!"
    # QFontDatabase.addApplicationFont(":/font")
    QFontDatabase.addApplicationFont(":/BalooBhaiRegular.ttf")
    app = QApplication([])
    app.setApplicationName(appname)
    app.setWindowIcon(QIcon(":app"))
    win = MainWindow(appname)
    win.show()
    sys.exit(app.exec_())
