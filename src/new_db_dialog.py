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

        self.accept()

    def _on_browse_clicked(self):
        file_description = "数据库文件"
        file_extension = ".db"
        file_filter = file_description + " (*" + file_extension + ")"

        default_path = os.path.expanduser("~/Documents/")

        file_path, _ = QFileDialog.getSaveFileName(
            self, "选择文件位置", default_path, file_filter
        )

        self.location_line_edit.setText(file_path)
