from PyQt6.QtWidgets import QMainWindow
from .forms.login_ui import Ui_LoginWindow
from .main_form import MainWindow
from .database.users import user


class LoginWindow(QMainWindow, Ui_LoginWindow):

    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Вход')
        
        self.login.clicked.connect(self.check_user)
        
    def check_user(self):
        login = self.name_input.text()
        password = self.pass_input.text()
        if user.check_user(login, password)['code'] == 200:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
            print('EROR LOGIN')