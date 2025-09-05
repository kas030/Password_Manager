import os

from PySide6.QtWidgets import (
    QDialog,
    QDialogButtonBox,
    QLabel,
    QHBoxLayout,
    QLineEdit,
    QVBoxLayout,
    QPushButton,
    QFileDialog,
    QGridLayout,
    QMessageBox,
)


class NewDBDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("新建密码数据库")

        # 添加“确认”和“取消”按钮
        self.buttonBox = QDialogButtonBox()
        self.buttonBox.addButton(QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.addButton(QDialogButtonBox.StandardButton.Cancel)
        self.buttonBox.accepted.connect(self._on_ok_clicked)
        self.buttonBox.rejected.connect(self.reject)

        # 添加“选择文件位置”输入框、“浏览”按钮
        location_layout = QHBoxLayout()

        self.location_label = QLabel("位置(&L):")
        self.location_line_edit = QLineEdit()
        self.location_label.setBuddy(self.location_line_edit)
        self.location_browse_btn = QPushButton("浏览(&B)…")
        self.location_browse_btn.clicked.connect(self._on_browse_clicked)

        location_layout.addWidget(self.location_label)
        location_layout.addWidget(self.location_line_edit)
        location_layout.addWidget(self.location_browse_btn)

        # 添加设置主密码、确认密码控件
        password_layout = QGridLayout()

        self.password_label = QLabel("密码(&P):")
        self.password_line_edit = QLineEdit()
        self.password_line_edit.setEchoMode(QLineEdit.Password)
        self.password_label.setBuddy(self.password_line_edit)

        self.confirm_password_label = QLabel("确认密码(&C):")
        self.confirm_password_line_edit = QLineEdit()
        self.confirm_password_line_edit.setEchoMode(QLineEdit.Password)
        self.confirm_password_label.setBuddy(self.confirm_password_line_edit)

        password_layout.addWidget(self.password_label, 0, 0)
        password_layout.addWidget(self.password_line_edit, 0, 1)
        password_layout.addWidget(self.confirm_password_label, 1, 0)
        password_layout.addWidget(self.confirm_password_line_edit, 1, 1)

        # 设置对话框总布局
        main_layout = QVBoxLayout()
        main_layout.addLayout(location_layout)
        main_layout.addLayout(password_layout)
        main_layout.addWidget(self.buttonBox)
        self.setLayout(main_layout)

        self.setMinimumWidth(400)

    def _on_ok_clicked(self):
        if not self._check_file_path_validity():
            return

        if not self._check_password_validity():
            return

        if not self._confirm_overwrite():
            return

        self.accept()

    def _check_file_path_validity(self) -> bool:
        path = self.location_line_edit.text().strip()

        # 检查路径是否为空
        if not path:
            QMessageBox.warning(self, "无效路径", "文件路径不能为空。")
            return False

        # 检查路径是否存在
        dir_path = os.path.dirname(path)
        if not os.path.exists(dir_path):
            QMessageBox.warning(self, "无效路径", "文件目录不存在。")
            return False

        # 检查文件名是否合法
        file_name = os.path.basename(path)
        invalid_chars = r'<>:"/\|?*'
        if not file_name or any(char in file_name for char in invalid_chars):
            QMessageBox.warning(
                self, "无效文件名", "文件名不能包含下列任何字符：\n" + invalid_chars
            )
            return False

        return True

    def _check_password_validity(self) -> bool:
        # 检查密码是否为空
        password = self.password_line_edit.text()
        if not password:
            QMessageBox.warning(self, "无效密码", "密码不能为空。")
            return False

        # 检查密码和确认密码是否匹配
        confirm_password = self.confirm_password_line_edit.text()
        if password != confirm_password:
            QMessageBox.warning(self, "密码不匹配", "两次输入的密码不一致。")
            return False

        return True

    def _confirm_overwrite(self) -> bool:
        path = self.location_line_edit.text().strip()

        # 如果文件存在，询问用户是否覆盖
        if os.path.exists(path):
            reply = QMessageBox.question(
                self,
                "确认覆盖",
                f"文件 '{path}' 已存在。是否覆盖？\n注意，覆盖后文件内容将无法恢复。",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No,
            )
            # 用户取消操作
            if reply == QMessageBox.StandardButton.No:
                return False
            # 尝试删除文件
            else:
                try:
                    os.remove(path)
                except Exception as e:
                    QMessageBox.critical(
                        self,
                        "错误",
                        f"无法覆盖文件 '{path}'。\n错误信息：{str(e)}",
                    )
                    return False

        return True

    def _on_browse_clicked(self):
        file_description = "数据库文件"
        file_extension = ".db"
        file_filter = file_description + " (*" + file_extension + ")"

        default_path = os.path.expanduser("~/Documents/")

        file_path, _ = QFileDialog.getSaveFileName(
            self, "选择文件位置", default_path, file_filter
        )

        self.location_line_edit.setText(file_path)
