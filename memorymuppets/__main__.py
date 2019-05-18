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
        self.mode = 0
        self.sequence = []
        self.counter_ok = -1
        self.counter_sequence = -2
        self.timer = QTimer()
        self.timer.timeout.connect(self.play_sequence)

    def muppet_pressed(self, i):
        def button_response():
            if self.game and self.muppets_active:
                self.check_sequence(i)
            elif self.muppets_active:
                self.muppets[i].respond()
        return button_response

    def play_button_pressed(self):
        if not self.game:
            self.muppets_active = False
            self.game = True
            self.sequence = []
            self.timer.start(100)
            self.start.play()

    def reset_counters(self):
        self.counter_ok = -1
        self.counter_sequence = -2

    def shuffle_sequence(self):
        if self.mode == 0:
            self.sequence.append(randint(0, 5))
        elif self.mode == 1:
            rounds = len(self.sequence)
            self.sequence = [randint(0, 5) for i in range(rounds + 1)]

    def play_sequence(self):
        self.counter_sequence += 1
        if self.counter_sequence == -1:
            self.play_button.setCursor(QCursor(Qt.ArrowCursor))
            self.play_button.setText("Now, remember...")
            self.timer.start(1000)
            self.shuffle_sequence()
        elif self.counter_sequence == 0:
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

    def check_sequence(self, i):
        self.counter_ok += 1
        if not self.sequence[self.counter_ok] == i:
            self.end.play()
            self.game = False
            self.play_button.setCursor(QCursor(Qt.PointingHandCursor))
            self.play_button.setText(
                f"Nope! Score: {len(self.sequence) - 1}. Play?")
            self.reset_counters()
        elif self.counter_ok < len(self.sequence) - 1:
            self.muppets[i].respond()
        else:
            self.muppets[i].respond()
            self.play_button.setText(
                f"Yes! Score: {len(self.sequence)}")
            self.muppets_active = False
            self.reset_counters()
            self.timer.start(1000)


def run_game():
    appname = "Muppet Memory Game!"
    app = QApplication([])
    app.setApplicationName(appname)
    app.setWindowIcon(QIcon(":app"))
    win = MainWindow(appname)
    win.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run_game()
