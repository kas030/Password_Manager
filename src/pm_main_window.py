from PySide6.QtWidgets import QApplication, QMainWindow, QStatusBar
from PySide6.QtCore import QSize

from pm_menu_bar import PmMenuBar


class PmMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")

        self.setFixedSize(QSize(800, 600))

        self.pm_menu_bar = PmMenuBar(self)

        self.setStatusBar(QStatusBar(self))


if __name__ == "__main__":
    app = QApplication([])
    window = PmMainWindow()
    window.show()
    app.exec()
