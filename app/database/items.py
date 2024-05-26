from .db.database_manager import DBManager

class ItemDatabaseScripts(DBManager):
    def __init__(self):
        super().__init__()
    
    def get_items(self):
        req = self.execute("SELECT * "
                "FROM items ")
        
        return req
    
    def get_item(self, item_id):
        req = self.execute("SELECT * "
                "FROM items "
                "WHERE id= ? ", 
                args=(item_id, ), many=False)
        
        if req['code'] == 200:
            return req['data']
        else:
            return None
    
    def create_item(self, name, comment, quantity, price, category_id):
        req = self.execute("INSERT INTO items(name, comment, quantity, price, category_id) "
                        "VALUES (?, ?, ?, ? ,?) ", 
                        args=(name, comment, quantity, price, category_id, ), many=False)
        
        return req
    
    def update_item(self, id, name, comment, quantity, price, category_id):
        req = self.execute("UPDATE items "
                           "SET name = ?, comment = ?, quantity = ?, price = ?, category_id = ? "
                           "WHERE id = ?", 
                        args=(name, comment, quantity, price, category_id, id), many=False)
        
        return req
    
    def update_quantity_item(self, id, quantity):
        
        quantity_item = self.get_item(id)
        if quantity_item:
            quantity_item = quantity_item[3] - quantity

            req = self.execute("UPDATE items "
                            "SET quantity = ? "
                            "WHERE id = ?", 
                            args=(quantity_item, id), many=False)
            
            return True
        else:
            return False
    
    def delete_item(self, item_id):
        req = self.execute("DELETE FROM items "
                         "WHERE id = ?",
                        args=(item_id, ))
        
        return req
    
    def create_category(self, name):
        req = self.execute("INSERT INTO categoryes(name) "
                        "VALUES (?) ", 
                        args=(name, ), many=False)
        
        return req
    
    def get_categoryes(self):
        req = self.execute("SELECT * "
                "FROM categoryes ")
        
        return req
    
    def delete_category(self, category_id):
        req = self.execute("DELETE FROM categoryes "
                         "WHERE id = ?",
                        args=(category_id, ))
        
        return req
    
    def get_category(self, category_id):
        req = self.execute("SELECT name "
                "FROM categoryes "
                "WHERE id= ? ", 
                args=(category_id, ), many=False)
        
        if req['code'] == 200:
            return req['data'][0]
        else:
            return None
    
item = ItemDatabaseScripts()