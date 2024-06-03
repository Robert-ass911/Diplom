from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from .forms.main_ui import Ui_MainWindow
from .create_item_form import CreateItemWindow
from .create_order_form import CreateOrderWindow
from .create_shipment_form import CreateShipmentiWindow
from .create_supplaer_form import CreateSupplaerWindow
from .create_user_form import CreateUserWindow
from .categoryes_form import CategoriesWindow
from .database.items import item
from .database.users import user
from .database.orders import order
from .database.supplies import shipment


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
    
    def clear_table(self):
        self.data_table.clear()
        self.data_table.setRowCount(0)
        self.data_table.setColumnCount(0)
    
    def item(self, item_id=None):
        if item_id:
            self.main_window = CreateItemWindow(item_id)
        else:
            self.main_window = CreateItemWindow()
        self.main_window.show()
    
    def user(self, user_id=None):
        if user_id:
            self.main_window = CreateUserWindow(user_id)
        else:
            self.main_window = CreateUserWindow()
        self.main_window.show()
    
    def order(self):
        self.main_window = CreateOrderWindow()
        self.main_window.show()
        
    def shipment(self):
        self.main_window = CreateShipmentiWindow()
        self.main_window.show()
        
    def supplier(self, supplaer_id):
        if supplaer_id:
            self.main_window = CreateSupplaerWindow(supplaer_id)
        else:
            self.main_window = CreateSupplaerWindow()
        self.main_window.show()
        
    def categories(self):
        self.main_window = CategoriesWindow()
        self.main_window.show()
    
    
    def delete_item(self, id):
        item.delete_item(id)
        self.get_all_items()
    
    def delete_user(self, id):
        user.delete_user(id)
        self.get_all_users()
        
    def delete_supplaer(self, id):
        shipment.delete_supplaer(id)
        self.get_all_suppliers()
    
    
    def get_all_items(self):
        self.setWindowTitle('Товары')
        self.create_btn.disconnect()
        self.create_btn.clicked.connect(self.item)
        self.create_btn.show()
        self.categoryes_btn.disconnect()
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
        if user.post_id == 1:
            self.create_btn.disconnect()
            self.create_btn.clicked.connect(self.user)
            self.create_btn.show()
        else:
            self.create_btn.hide()
            
        self.categoryes_btn.hide()
        
        self.clear_table()
        
        users = user.get_users()
        if users['code'] == 200:
            col_row = 0
            users = users['data']
            row = len(users)
            self.data_table.setRowCount(row)
            
            if user.post_id == 1:
                self.data_table.setColumnCount(6)
            else:
                self.data_table.setColumnCount(4)
                
            self.data_table.setHorizontalHeaderLabels(
                ['Имя', 'Телефон', 'Почта', 'Должность', '', '']) 
            for us in users:
                self.data_table.setItem(col_row, 0, QTableWidgetItem(str(us[1])))
                self.data_table.setItem(col_row, 1, QTableWidgetItem(str(us[2])))
                self.data_table.setItem(col_row, 2, QTableWidgetItem(str(us[3])))
                self.data_table.setItem(col_row, 3, QTableWidgetItem(str(user.get_post(us[4]))))
                if user.post_id == 1:
                    self.delte_item_btn =  QPushButton('Удалить')
                    self.delte_item_btn.clicked.connect(lambda _, data=us[0]: self.delete_user(data))
                    self.data_table.setCellWidget(col_row, 4, self.delte_item_btn)
                    self.update_user_btn =  QPushButton('Изменить')
                    self.update_user_btn.clicked.connect(lambda _, data=us[0]: self.user(data))
                    self.data_table.setCellWidget(col_row, 5, self.update_user_btn)
                col_row += 1
    
    def get_all_orders(self):
        self.setWindowTitle('Заказы')
        self.create_btn.disconnect()
        self.create_btn.clicked.connect(self.order)
        self.create_btn.show()
        self.categoryes_btn.hide()
        
        self.clear_table()
        
        orders = order.get_orders()
        if orders['code'] == 200:
            col_row = 0
            orders = orders['data']
            row = len(orders)
            self.data_table.setRowCount(row) 
            self.data_table.setColumnCount(5)
            self.data_table.setHorizontalHeaderLabels(
                ['Дата', 'Кол-во', 'Цена', 'Менеджер', 'Товар']) 
            for ord in orders:
                
                ord_user = user.get_user(ord[4])
                if ord_user['code'] == 200:
                    ord_user = ord_user['data'][1]
                
                ord_item = item.get_item(ord[5])
                if ord_item:
                    ord_item = ord_item[1]
                    
                self.data_table.setItem(col_row, 0, QTableWidgetItem(str(ord[1])))
                self.data_table.setItem(col_row, 1, QTableWidgetItem(str(ord[2])))
                self.data_table.setItem(col_row, 2, QTableWidgetItem(str(ord[3])))
                self.data_table.setItem(col_row, 3, QTableWidgetItem(str(ord_user)))
                self.data_table.setItem(col_row, 4, QTableWidgetItem(str(ord_item)))
                col_row += 1
    
    def get_all_supplies(self):
        self.setWindowTitle('Поставки')
        self.create_btn.disconnect()
        self.create_btn.clicked.connect(self.shipment)
        self.create_btn.show()
        self.categoryes_btn.hide()
        
        self.clear_table()
        
        supplies = shipment.get_supplies()
        if supplies['code'] == 200:
            supplies = supplies['data']
            col_row = 0
            row = len(supplies)
            self.data_table.setRowCount(row) 
            self.data_table.setColumnCount(4)
            self.data_table.setHorizontalHeaderLabels(
                ['Дата', 'Кол-во', 'Товар', 'Поставщик']) 
            for sup in supplies:
                
                sup_item = item.get_item(sup[3])
                if sup_item:
                    sup_item = sup_item[1]
                    
                sup_suppliers = shipment.get_supplaer(sup[4])
                if sup_suppliers['code'] == 200:
                    sup_suppliers = sup_suppliers['data'][1]
                    
                self.data_table.setItem(col_row, 0, QTableWidgetItem(str(sup[1])))
                self.data_table.setItem(col_row, 1, QTableWidgetItem(str(sup[2])))
                self.data_table.setItem(col_row, 2, QTableWidgetItem(str(sup_item)))
                self.data_table.setItem(col_row, 3, QTableWidgetItem(str(sup_suppliers)))
                col_row += 1
    
    def get_all_suppliers(self):
        self.setWindowTitle('Поставщики')
        self.create_btn.disconnect()
        self.create_btn.clicked.connect(self.supplier)
        self.create_btn.show()
        self.categoryes_btn.hide()
        
        self.clear_table()
        
        suppliers = shipment.get_supplaers()
        if suppliers['code'] == 200:
            col_row = 0
            suppliers = suppliers['data']
            row = len(suppliers)
            self.data_table.setRowCount(row) 
            self.data_table.setColumnCount(5)
            self.data_table.setHorizontalHeaderLabels(
                ['Название', 'Телефон', 'Аддрес', '', '']) 
            for it in suppliers:
                self.data_table.setItem(col_row, 0, QTableWidgetItem(str(it[1])))
                self.data_table.setItem(col_row, 1, QTableWidgetItem(str(it[2])))
                self.data_table.setItem(col_row, 2, QTableWidgetItem(str(it[3])))
                self.delte_item_btn =  QPushButton('Удалить')
                self.delte_item_btn.clicked.connect(lambda _, data=it[0]: self.delete_supplaer(data))
                self.data_table.setCellWidget(col_row, 3, self.delte_item_btn)
                self.update_item_btn =  QPushButton('Изменить')
                self.update_item_btn.clicked.connect(lambda _, data=it[0]: self.supplier(data))
                self.data_table.setCellWidget(col_row, 4, self.update_item_btn)
                col_row += 1