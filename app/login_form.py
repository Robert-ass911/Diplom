from PyQt6.QtWidgets import QMainWindow, QMessageBox
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
        
    def warning_window(self, titel, text):
        '''Вывод окна с предупреждением'''
        message_box = QMessageBox()
        message_box.setWindowTitle(titel)
        message_box.setText(text)
        message_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        result = message_box.exec()
        if result == QMessageBox.StandardButton.Yes:
            return True
        else:
            return False
        
    def check_user(self):
        login = self.name_input.text()
        password = self.pass_input.text()
        if user.check_user(login, password)['code'] == 200:
            self.main_window = MainWindow()
            self.main_window.show()
            self.close()
        else:
           self.warning_window('login EROR', 'Неверный логин или пароль')