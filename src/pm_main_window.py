from PySide6.QtWidgets import QApplication, QMainWindow

from pm_menu_bar import PmMenuBar


class PmMainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Password Manager")

        self.setFixedSize(800, 600)

        self.pm_menu_bar = PmMenuBar(self)


if __name__ == "__main__":
    app = QApplication([])
    window = PmMainWindow()
    window.show()
    app.exec()
