from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QPushButton
from .forms.categories_ui import Ui_CategoriesWindow
from .database.items import item


class CategoriesWindow(QMainWindow, Ui_CategoriesWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.print_categories()
        
        self.create_btn.clicked.connect(self.crate_cetegory)
        self.cancel_btn.clicked.connect(self.close)
    
    def get_categories(self):
        categories = item.get_categoryes()
        if categories['code'] == 200:
            self.categories = categories['data']
    
    def crate_cetegory(self):
        name = self.name_line.text()
        item.create_category(name)
        self.print_categories()
    
    def delete_category(self, category_id):
        item.delete_category(category_id)
        self.print_categories()
    
    def print_categories(self):
        self.get_categories()
        col_row = 0
        row = len(self.categories)
        self.tableWidget.setRowCount(row) 
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setHorizontalHeaderLabels(
            ['', ''])
        for cat in self.categories:
                self.tableWidget.setItem(col_row, 0, QTableWidgetItem(str(cat[1])))
                self.delte_category_btn =  QPushButton('Удалить')
                self.delte_category_btn.clicked.connect(lambda _, data=cat[0]: self.delete_category(data))
                self.tableWidget.setCellWidget(col_row, 1, self.delte_category_btn)
                col_row += 1