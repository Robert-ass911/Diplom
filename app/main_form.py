from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow
from .forms.main_ui import Ui_MainWindow
from .create_item_form import CreateItemWindow
from .create_order_form import CreateOrderWindow
from .create_shipment_form import CreateShipmentiWindow
from .create_supplaer_form import CreateSupplaerWindow
from .create_user_form import CreateUserWindow
from .categoryes_form import CategoriesWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    login_correct = pyqtSignal()
    main_window: QMainWindow

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.get_all_items()
        
        self.items_btn.clicked.connect(self.get_all_items)
        self.users_btn.clicked.connect(self.get_all_users)
        self.orders_btn.clicked.connect(self.get_all_orders)
        self.supplies_btn.clicked.connect(self.get_all_supplies)
        self.suppliers_btn.clicked.connect(self.get_all_suppliers)
    
    
    def create_item(self):
        self.main_window = CreateItemWindow()
        self.main_window.show()
    
    def create_user(self):
        self.main_window = CreateUserWindow()
        self.main_window.show()
    
    def create_order(self):
        self.main_window = CreateOrderWindow()
        self.main_window.show()
        
    def create_shipment(self):
        self.main_window = CreateShipmentiWindow()
        self.main_window.show()
        
    def create_supplier(self):
        self.main_window = CreateSupplaerWindow()
        self.main_window.show()
        
    def categories(self):
        self.main_window = CategoriesWindow()
        self.main_window.show()
    
    
    def get_all_items(self):
        self.setWindowTitle('Товары')
        self.create_btn.clicked.connect(self.create_item)
        self.categoryes_btn.clicked.connect(self.categories)
        self.categoryes_btn.show()
        
    
    def get_all_users(self):
        self.setWindowTitle('Пользователи')
        self.create_btn.clicked.connect(self.create_user)
        self.categoryes_btn.hide()
    
    def get_all_orders(self):
        self.setWindowTitle('Заказы')
        self.create_btn.clicked.connect(self.create_order)
        self.categoryes_btn.hide()
    
    def get_all_supplies(self):
        self.setWindowTitle('Поставки')
        self.create_btn.clicked.connect(self.create_shipment)
        self.categoryes_btn.hide()
    
    def get_all_suppliers(self):
        self.setWindowTitle('Поставщики')
        self.create_btn.clicked.connect(self.create_supplier)
        self.categoryes_btn.hide()