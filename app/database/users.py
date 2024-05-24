from .db.database_manager import DBManager

class UserDatabaseScripts(DBManager):
    def __init__(self):
        super().__init__()
        
        self.id = int
        self.name = str
        self.phone = int
        self.email = str
        self.post_id = int
        
    def check_user(self, login, password):
        req = self.execute("SELECT id, name, phone, email, post_id "
                        "FROM users "
                        "WHERE login= ? AND password = ? ", 
                        args=(login, password, ), many=False)
        
        if req['code'] == 200:
            self.id = req['data'][0]
            self.name = req['data'][1]
            self.phone = req['data'][2]
            self.email = req['data'][3]
            self.post_id = req['data'][4]
            
        return req
    
    def get_user(self, user_id):
        req = self.execute("SELECT id, name, phone, email, login, password, post_id "
                        "FROM users "
                        "WHERE id = ? ",
                        args=(user_id, ), many=False)
        
        return req
    
    def get_users(self):
        req = self.execute("SELECT id, name, phone, email, post_id "
                        "FROM users "
                        "WHERE id > 1 ")
        
        return req
    
    def delete_user(self, user_id):
        req = self.execute("DELETE FROM users "
                         "WHERE id = ?",
                        args=(user_id, ))
        
        return req
    
    def create_user(self, name, phone, email, login, password):
        req = self.execute("INSERT INTO users(name, phone, email, login, password, post_id) "
                        "VALUES (?, ?, ?, ? ,?, 2) ", 
                        args=(name, phone, email, login, password, ), many=False)
        
        return req
    
    def update_user(self, id, name, phone, email, login, password):
        req = self.execute("UPDATE users "
                           "SET name = ?, phone = ?, email = ?, login = ?, password = ? "
                           "WHERE id = ?", 
                        args=(name, phone, email, login, password, id), many=False)
        
        return req
    
    def get_post(self, id_post):
        req = self.execute("SELECT name "
                        "FROM posts "
                        "WHERE id= ? ", 
                        args=(id_post, ), many=False)
        
        if req['code'] == 200:
            return req['data'][0]
        else:
            return None
    
user = UserDatabaseScripts()