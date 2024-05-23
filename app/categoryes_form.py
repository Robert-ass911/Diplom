from PyQt6.QtWidgets import QMainWindow
from .forms.categories_ui import Ui_CategoriesWindow


class CategoriesWindow(QMainWindow, Ui_CategoriesWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)