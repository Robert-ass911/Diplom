from PyQt6.QtWidgets import QMainWindow
from .forms.create_user_ui import Ui_CreateUserWindow
from .database.users import user


class CreateUserWindow(QMainWindow, Ui_CreateUserWindow):
    def __init__(self, user_id=None):
        super().__init__()
        self.setupUi(self)
        
        
        if user_id:
            self.update_user_form(user_id)
            self.user_id = user_id
        else:
            self.create_user_form()
        
        self.cancel_btn.clicked.connect(self.close)
        
    def chec_input_data(self):
        name = self.name_line.text()
        phone = int(self.phone_line.text())
        email = self.email_line.text()
        login = self.login_line.text()
        password = self.password_line.text()
        if name and phone and email and login and password:
            return (name, phone, email, login, password)
        else: 
            return None
    
    def create_user(self):
        user_data = self.chec_input_data()
        if user_data:
            user.create_user(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
            self.close()
            
    def update_user(self):
        user_data = self.chec_input_data()
        if user_data:
            user.update_user(self.user_id, user_data[0], user_data[1], user_data[2], user_data[3], user_data[4])
            self.close()
        
    def create_user_form(self):
        self.create_btn.setText('Создать')
        self.create_btn.clicked.connect(self.create_user)
        
    def update_user_form(self, user_id):
        self.create_btn.setText('Сохранить')
        self.create_btn.clicked.connect(self.update_user)
        user_data = user.get_user(user_id)
        if user_data['code'] == 200:
            user_data = user_data['data']
            self.name_line.setText(user_data[1])
            self.phone_line.setText(str(user_data[2]))
            self.email_line.setText(user_data[3])
            self.login_line.setText(user_data[4])
            self.password_line.setText(user_data[5])