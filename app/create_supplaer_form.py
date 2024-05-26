from PyQt6.QtWidgets import QMainWindow
from .forms.create_supplaer_ui import Ui_CreateSupplaerWindow
from .database.supplies import shipment


class CreateSupplaerWindow(QMainWindow, Ui_CreateSupplaerWindow):
    def __init__(self, supplaer_id=None):
        super().__init__()
        self.setupUi(self)
        
        if supplaer_id:
            self.update_supplaer_form(supplaer_id)
            self.supplaer_id = supplaer_id
        else:
            self.create_supplaer_form()
        
        self.cancel_btn.clicked.connect(self.close)
    
    def check_data(self):
        name = self.name_line.text()
        phone = int(self.phone_line.text())
        addres = self.addres_line.text()
        data = (name, phone, addres)
        
        if name and phone and addres:
            return True, data
        else:
            data = None
            return False, data
    
    def create_supplaer(self):
        res, data = self.check_data()
        if res:
            shipment.create_supplaer(data[0], data[1], data[2])
            self.close()
    
    def create_supplaer_form(self):
        self.create_btn.setText('Создать')
        self.create_btn.clicked.connect(self.create_supplaer)
    
    def update_supplaer(self):
        res, data = self.check_data()
        if res:
            shipment.update_supplaer(self.supplaer_id, data[0], data[1], data[2])
            self.close()
    
    def update_supplaer_form(self, supplaer_id):
        self.create_btn.setText('Сохранить')
        self.create_btn.clicked.connect(self.update_supplaer)
        update_item = shipment.get_supplaer(supplaer_id)
        if update_item['code'] == 200:
            update_item = update_item['data']
            self.name_line.setText(update_item[1])
            self.phone_line.setText(str(update_item[2]))
            self.addres_line.setText(update_item[3])