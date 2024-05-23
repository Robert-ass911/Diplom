from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from .forms.login_ui import Ui_LoginWindow
from .main_form import MainWindow


class LoginWindow(QMainWindow, Ui_LoginWindow):

    login_correct = pyqtSignal()
    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Вход')
        
        self.login.clicked.connect(self.check_user)
        
    def check_user(self):
        login = self.name_input.text()
        password = self.pass_input.text()
        self.main_window = MainWindow()
        self.main_window.show()
        self.close()
        
