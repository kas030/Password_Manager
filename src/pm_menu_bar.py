from PySide6.QtWidgets import QMenuBar
from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtCore import Slot


class PmMenuBar:

    def __init__(self, main_window):
        self.main_window = main_window
        self.menu_bar = self.main_window.menuBar()
        self.init_file_menu()

    def init_file_menu(self):
        file_menu = self.menu_bar.addMenu("文件(&F)")

        new_action = file_menu.addAction("新建(&N)…")
        new_action.setShortcut(QKeySequence("Ctrl+N"))
        new_action.setStatusTip("新建密码数据库文件")
        new_action.triggered.connect(self.new_file)
        file_menu.addAction(new_action)

        open_action = file_menu.addAction("打开(&O)…")
        open_action.setShortcut(QKeySequence("Ctrl+O"))
        open_action.setStatusTip("打开密码数据库文件")
        open_action.triggered.connect(self.open_file)
        file_menu.addAction(open_action)

        file_menu.addSeparator()

        save_action = file_menu.addAction("保存(&S)")
        save_action.setShortcut(QKeySequence("Ctrl+S"))
        save_action.setStatusTip("保存当前文件")
        save_action.triggered.connect(self.save_file)
        file_menu.addAction(save_action)

        save_action = file_menu.addAction("另存为(&A)…")
        save_action.setShortcut(QKeySequence("Ctrl+Shift+S"))
        save_action.setStatusTip("将当前数据库另存")
        save_action.triggered.connect(self.save_as)
        file_menu.addAction(save_action)

        save_all_action = file_menu.addAction("全部保存(&L)")
        save_all_action.setStatusTip("保存所有打开的密码数据库")
        save_all_action.triggered.connect(self.save_all_file)
        file_menu.addAction(save_all_action)

    @Slot()
    def new_file(self):
        print("新建")

    @Slot()
    def open_file(self):
        print("打开")

    @Slot()
    def save_file(self):
        print("保存")

    @Slot()
    def save_as(self):
        print("另存为")

    @Slot()
    def save_all_file(self):
        print("全部保存")
