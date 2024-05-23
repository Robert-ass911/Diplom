from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from .forms.main_ui import Ui_MainWindow
from .create_item_form import CreateItemWindow
from .create_order_form import CreateOrderWindow
from .create_shipment_form import CreateShipmentiWindow
from .create_supplaer_form import CreateSupplaerWindow
from .create_user_form import CreateUserWindow
from .categoryes_form import CategoriesWindow
from .database.items import item


class MainWindow(QMainWindow, Ui_MainWindow):

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
    
    
    def item(self, item_id=None):
        if item_id:
            self.main_window = CreateItemWindow(item_id)
        else:
            self.main_window = CreateItemWindow()
        self.main_window.show()
    
    def user(self):
        self.main_window = CreateUserWindow()
        self.main_window.show()
    
    def order(self):
        self.main_window = CreateOrderWindow()
        self.main_window.show()
        
    def shipment(self):
        self.main_window = CreateShipmentiWindow()
        self.main_window.show()
        
    def supplier(self):
        self.main_window = CreateSupplaerWindow()
        self.main_window.show()
        
    def categories(self):
        self.main_window = CategoriesWindow()
        self.main_window.show()
    
    
    def delete_item(self, id):
        item.delete_item(id)
        self.get_all_items()
    
    
    def clear_table(self):
        self.data_table.clear()
        self.data_table.setRowCount(0)
        self.data_table.setColumnCount(0)
    
    def get_all_items(self):
        self.setWindowTitle('Товары')
        self.create_btn.clicked.connect(self.item)
        self.categoryes_btn.clicked.connect(self.categories)
        self.categoryes_btn.show()
        
        self.clear_table()
        
        items = item.get_items()
        if items['code'] == 200:
            col_row = 0
            items = items['data']
            row = len(items)
            self.data_table.setRowCount(row) 
            self.data_table.setColumnCount(7)
            self.data_table.setHorizontalHeaderLabels(
                ['Название', 'Описание', 'Кол-во', 'Цена', 'Категория', '', '']) 
            for it in items:
                self.data_table.setItem(col_row, 0, QTableWidgetItem(str(it[1])))
                self.data_table.setItem(col_row, 1, QTableWidgetItem(str(it[2])))
                self.data_table.setItem(col_row, 2, QTableWidgetItem(str(it[3])))
                self.data_table.setItem(col_row, 3, QTableWidgetItem(str(it[4]) + ' руб.'))
                self.data_table.setItem(col_row, 4, QTableWidgetItem(str(item.get_category(it[5]))))
                self.delte_item_btn =  QPushButton('Удалить')
                self.delte_item_btn.clicked.connect(lambda _, data=it[0]: self.delete_item(data))
                self.data_table.setCellWidget(col_row, 5, self.delte_item_btn)
                self.update_item_btn =  QPushButton('Изменить')
                self.update_item_btn.clicked.connect(lambda _, data=it[0]: self.item(data))
                self.data_table.setCellWidget(col_row, 6, self.update_item_btn)
                col_row += 1
        
    
    def get_all_users(self):
        self.setWindowTitle('Пользователи')
        self.create_btn.clicked.connect(self.user)
        self.categoryes_btn.hide()
        
        self.clear_table()
    
    def get_all_orders(self):
        self.setWindowTitle('Заказы')
        self.create_btn.clicked.connect(self.order)
        self.categoryes_btn.hide()
        
        self.clear_table()
    
    def get_all_supplies(self):
        self.setWindowTitle('Поставки')
        self.create_btn.clicked.connect(self.shipment)
        self.categoryes_btn.hide()
        
        self.clear_table()
    
    def get_all_suppliers(self):
        self.setWindowTitle('Поставщики')
        self.create_btn.clicked.connect(self.supplier)
        self.categoryes_btn.hide()
        
        self.clear_table()