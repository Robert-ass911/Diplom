from PyQt6.QtWidgets import QApplication
import sys
from app.login_form import LoginWindow


if __name__ == '__main__': 
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec()