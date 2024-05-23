from PyQt6.QtWidgets import QMainWindow
from .forms.create_order_ui import Ui_CreateOrderWindow


class CreateOrderWindow(QMainWindow, Ui_CreateOrderWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.cancel_btn.clicked.connect(self.close)