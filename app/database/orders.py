from .db.database_manager import DBManager

class OrderDatabaseScripts(DBManager):
    def __init__(self):
        super().__init__()

    def get_orders(self):
        req = self.execute("SELECT * "
                "FROM orders ")
        
        return req

    def create_order(self, data, quantity, price_order, user_id, item_id):
        req = self.execute("INSERT INTO orders(data, quantity, price_order, user_id, item_id) "
                        "VALUES (?, ?, ?, ?, ?) ", 
                        args=(data, quantity, price_order, user_id, item_id, ), many=False)
        
        return req

    def delete_order(self, order_id):
        req = self.execute("DELETE FROM orders "
                         "WHERE id = ?",
                        args=(order_id, ))
        
        return req
        
order = OrderDatabaseScripts()