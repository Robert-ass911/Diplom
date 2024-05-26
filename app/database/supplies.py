from .db.database_manager import DBManager

class SuppliesDatabaseScripts(DBManager):
    def __init__(self):
        super().__init__()
        
    def get_supplies(self):
        req = self.execute("SELECT id, data, quantity, item_id, supplaer_id "
                        "FROM supplies ")
        
        return req
    
    def create_shipment(self, data, quantity, item_id, supplaer_id):
        req = self.execute("INSERT INTO supplies(data, quantity, item_id, supplaer_id) "
                        "VALUES (?, ?, ?, ?) ", 
                        args=(data, quantity, item_id, supplaer_id))
        
        return req
    
    def get_supplaers(self):
        req = self.execute("SELECT * "
                        "FROM suppliers ")
        
        return req
    
    def get_supplaer(self, supplaer_id):
        req = self.execute("SELECT id, name, phone, addres "
                        "FROM suppliers "
                        "WHERE id = ? ",
                        args=(supplaer_id, ), many=False)
        
        return req
    
    def create_supplaer(self, name, phone, addres):
        req = self.execute("INSERT INTO suppliers(name, phone, addres) "
                        "VALUES (?, ?, ?) ", 
                        args=(name, phone, addres))
        
        return req
    
    def delete_supplaer(self, supplaer_id):
        req = self.execute("DELETE FROM suppliers "
                         "WHERE id = ?",
                        args=(supplaer_id, ))
        
        return req
    
    def update_supplaer(self, id, name, phone, addres):
        req = self.execute("UPDATE suppliers "
                           "SET name = ?, phone = ?, addres = ? "
                           "WHERE id = ?", 
                        args=(name, phone, addres, id), many=False)
        
        return req
        
shipment = SuppliesDatabaseScripts()