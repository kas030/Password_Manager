from PySide6.QtCore import Slot
from PySide6.QtGui import QKeySequence

import new_db_dialog


class PmMenuBar:

    def __init__(self, main_window):
        self.main_window = main_window
        self.menu_bar = self.main_window.menuBar()

        # 初始化菜单选项
        self._init_file_menu()
        self._init_edit_menu()

    def _init_file_menu(self):
        file_menu = self.menu_bar.addMenu("文件(&F)")

        new_action = file_menu.addAction("新建(&N)…")
        new_action.setShortcut(QKeySequence("Ctrl+N"))
        new_action.triggered.connect(self._new_file)
        file_menu.addAction(new_action)

        open_action = file_menu.addAction("打开(&O)…")
        open_action.setShortcut(QKeySequence("Ctrl+O"))
        open_action.triggered.connect(self._open_file)
        file_menu.addAction(open_action)

        file_menu.addSeparator()

        save_action = file_menu.addAction("保存(&S)")
        save_action.setShortcut(QKeySequence("Ctrl+S"))
        save_action.triggered.connect(self._save_file)
        file_menu.addAction(save_action)

        save_action = file_menu.addAction("另存为(&A)…")
        save_action.setShortcut(QKeySequence("Ctrl+Shift+S"))
        save_action.triggered.connect(self._save_as)
        file_menu.addAction(save_action)

        save_all_action = file_menu.addAction("全部保存(&L)")
        save_all_action.triggered.connect(self._save_all_file)
        file_menu.addAction(save_all_action)

    def _init_edit_menu(self):
        edit_menu = self.menu_bar.addMenu("编辑(&E)")

        copy_action = edit_menu.addAction("复制(&C)…")
        copy_action.setShortcut(QKeySequence("Ctrl+C"))
        copy_action.triggered.connect(self._copy)
        edit_menu.addAction(copy_action)

        copy_record_action = edit_menu.addAction("复制记录(&I)")
        copy_record_action.setShortcut(QKeySequence("Ctrl+Shift+C"))
        copy_record_action.triggered.connect(self._copy_record)
        edit_menu.addAction(copy_record_action)

        edit_menu.addSeparator()

        new_record_action = edit_menu.addAction("新建记录(&N)…")
        new_record_action.triggered.connect(self._new_record)
        edit_menu.addAction(new_record_action)

        remove_record_action = edit_menu.addAction("删除记录(&D)…")
        remove_record_action.setShortcut(QKeySequence("Delete"))
        remove_record_action.triggered.connect(self._remove_record)
        edit_menu.addAction(remove_record_action)

    @Slot()
    def _new_file(self):
        dialog = new_db_dialog.NewDBDialog(self.main_window)
        dialog.exec()

    @Slot()
    def _open_file(self):
        print("打开")

    @Slot()
    def _save_file(self):
        print("保存")

    @Slot()
    def _save_as(self):
        print("另存为")

    @Slot()
    def _save_all_file(self):
        print("全部保存")

    @Slot()
    def _copy(self):
        print("复制...")

    @Slot()
    def _copy_record(self):
        print("复制记录")

    @Slot()
    def _new_record(self):
        print("新建记录")

    @Slot()
    def _remove_record(self):
        print("删除记录")
