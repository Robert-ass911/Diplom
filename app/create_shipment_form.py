from PyQt6.QtWidgets import QMainWindow
from .forms.create_shipment_ui import Ui_CreateShipmentiWindow
from .database.supplies import shipment
from .database.items import item
from  datetime import datetime

class CreateShipmentiWindow(QMainWindow, Ui_CreateShipmentiWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.quantityBox.setMinimum(1)
        
        self.supplaers = self.get_supplaers()
        self.items = self.get_items()
        
        self.filling_data()
        
        self.activ_item = dict
        self.activ_supplaer = dict
        self.get_activ_item()
        self.get_activ_supplaer()
        
        self.itemBox.currentTextChanged.connect(self.get_activ_item)
        self.supplaerBox.currentTextChanged.connect(self.get_activ_supplaer)
        self.cancel_btn.clicked.connect(self.close)
        self.create_btn.clicked.connect(self.create_shipment)
                
    def get_items(self):
        items = item.get_items()
        if items['code'] == 200:
            return items['data']
    
    def get_supplaers(self):
        supplaers = shipment.get_supplaers()
        if supplaers['code'] == 200:
            return supplaers['data']
        
    def get_activ_item(self):
        for item in self.items:
            if item[1] == self.itemBox.currentText():
                self.activ_item = item
    
    def get_activ_supplaer(self):
        for supplaer in self.supplaers:
            if supplaer[1] == self.supplaerBox.currentText():
                self.activ_supplaer = supplaer
    
    def filling_data(self):
        self.data_label.setText(str(datetime.now().date()))
        
        for item in self.items:
            self.itemBox.addItem(f'{item[1]}')
        
        for supplaer in self.supplaers:
            self.supplaerBox.addItem(f'{supplaer[1]}')
            
    def create_shipment(self):
        data = datetime.now().date()
        quantity = self.quantityBox.value()
        item_id = self.activ_item[0]
        supplaer_id = self.activ_supplaer[0]
        if item.update_quantity_item(item_id, -quantity):
            shipment.create_shipment(data, quantity, item_id, supplaer_id)
            self.close()