from PyQt6.QtWidgets import QMainWindow
from .forms.create_supplaer_ui import Ui_CreateSupplaerWindow


class CreateSupplaerWindow(QMainWindow, Ui_CreateSupplaerWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.cancel_btn.clicked.connect(self.close)