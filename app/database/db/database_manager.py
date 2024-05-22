import sqlite3
import os

DATA_PATH = 'app\\database\\db\\scripts.sql'
DB_PATH = 'app\\database\\db\\base.sqlite'

class DBManager:
    def __init__(self):
        if not self.check_base():
            self.create_base()
            
    def check_base(self) -> bool:
        return os.path.exists(DB_PATH)

    def connect_to_base(self):
        conn = sqlite3.connect(DB_PATH)
        cur = conn.cursor()
        return conn, cur

    def create_base(self):
        conn, cur = self.connect_to_base()
        try:
            cur.executescript(open(DATA_PATH, encoding="utf-8").read())
            conn.commit()
            print('Tables are created')
        except sqlite3.Error as ex:
            print(ex)
        finally:
            conn.close()

    def execute(self, query: str, args=(), many: bool = True):
        conn, cur = self.connect_to_base()
        try:
            res = cur.execute(query, args)
            result = res.fetchall() if many else res.fetchone()
            conn.commit()
            last_row_id = cur.lastrowid
            if result == None or result == []:
                return {"code": 201, "data": None}
            else:
                if last_row_id == 0:
                    return {"code": 200, "data": result}
                return {"code": 200, "data": result, 'lastrowid': last_row_id}
        except sqlite3.Error as er:
            return {"code": 400, 'eror': str(er)}
        finally:
            conn.close()

base = DBManager()