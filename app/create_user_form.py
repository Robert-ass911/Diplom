from PyQt6.QtWidgets import QMainWindow
from .forms.create_user_ui import Ui_CreateUserWindow


class CreateUserWindow(QMainWindow, Ui_CreateUserWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.cancel_btn.clicked.connect(self.close)