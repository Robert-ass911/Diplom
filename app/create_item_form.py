from PyQt6.QtWidgets import QMainWindow
from .forms.create_item_ui import Ui_CreateItemWindow


class CreateItemWindow(QMainWindow, Ui_CreateItemWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.cancel_btn.clicked.connect(self.close)