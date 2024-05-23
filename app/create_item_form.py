from PyQt6.QtWidgets import QMainWindow
from .forms.create_item_ui import Ui_CreateItemWindow
from .database.items import item


class CreateItemWindow(QMainWindow, Ui_CreateItemWindow):
    def __init__(self, id_item = None):
        super().__init__()
        self.setupUi(self)
        
        self.completion_category_box()
        
        if id_item:
            self.update_item_form(id_item)
            self.id = id_item
        else:
            self.create_item_form()
        
        self.cancel_btn.clicked.connect(self.close)
        
    def get_activ_category_box(self):
        text = self.categoryBox.currentText()
        if self.categories:
            for cat in self.categories:
                if cat[1] == text:
                    return cat[0]
                
    def check_data(self):
        name = self.name_line.text()
        comment = self.textEdit.toPlainText()
        quantity = self.quantityBox.value()
        price = int(self.price_line.text())
        category_id = self.get_activ_category_box()
        data = (name, comment, quantity, price, category_id)
        
        if name and comment and quantity and price and category_id:
            return True, data
        else:
            data = None
            return False, data
        
    def create_item_form(self):
        self.create_btn.setText('Создать')
        self.create_btn.clicked.connect(self.create_item)
    
    def completion_category_box(self):
        self.categories = item.get_categoryes()
        if self.categories['code'] == 200:
            self.categories = self.categories['data']
            for cat in self.categories:
                self.categoryBox.addItem(str(cat[1]))
        else:
            self.categories = None
    
    def create_item(self):
        res, data = self.check_data()
        if res:
            item.create_item(data[0], data[1], data[2], data[3], data[4])
            self.close()
            
            
    def update_item(self):
        res, data = self.check_data()
        if res:
            print(item.update_item(self.id, data[0], data[1], data[2], data[3], data[4]))
            self.close()
            
    def update_item_form(self, id_item):
        self.create_btn.setText('Сохранить')
        self.create_btn.clicked.connect(self.update_item)
        update_item = item.get_item(id_item)
        if update_item:
            self.name_line.setText(update_item[1])
            self.textEdit.setText(update_item[2])
            self.quantityBox.setValue(update_item[3])
            self.price_line.setText(str(update_item[4]))
            self.categoryBox.setCurrentText(item.get_category(update_item[5]))
