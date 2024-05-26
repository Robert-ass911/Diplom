from PyQt6.QtWidgets import QMainWindow
from .forms.create_order_ui import Ui_CreateOrderWindow
from .database.items import item
from .database.users import user
from .database.orders import order
from datetime import datetime


class CreateOrderWindow(QMainWindow, Ui_CreateOrderWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.quantityBox.setMinimum(1)
        self.items = self.get_items()
        self.filling_data()
        self.activ_item = dict
        self.get_activ_item()

        self.quantityBox.valueChanged.connect(self.print_price)
        self.itemBox.currentTextChanged.connect(self.get_activ_item)
        self.cancel_btn.clicked.connect(self.close)
        self.create_btn.clicked.connect(self.create_order)
    
    def filling_data(self):
        self.data_label.setText(str(datetime.now().date()))
        self.name_label.setText(user.name)
        for item in self.items:
            self.itemBox.addItem(f'{item[1]}')
    
    def print_price(self):
        self.price_label.setText(f'{self.quantityBox.value() * self.activ_item[4]} руб.')
    
    def get_items(self):
        items_list = item.get_items()
        if items_list['code'] == 200:
            return items_list['data']
        
    def get_activ_item(self):
        for item in self.items:
            if item[1] == self.itemBox.currentText():
                self.activ_item = item
                self.quantityBox.setMaximum(item[3])
                self.price_label.setText(str(self.quantityBox.value() * item[4]) + 'руб.')
    
    def create_order(self):
        data = datetime.now().date()
        quantity = self.quantityBox.value()
        price_order = self.quantityBox.value() * self.activ_item[4]
        user_id = user.id
        item_id = self.activ_item[0]
        
        if data and quantity and price_order and user_id and item_id:
            if item.update_quantity_item(item_id, quantity):
                order.create_order(data, quantity, price_order, user_id, item_id)
                self.close()