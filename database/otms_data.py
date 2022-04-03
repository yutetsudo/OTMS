import sqlite3

def dict_factory(cursor, row):
    dict = {}
    for idx, col in enumerate(cursor.description):
        dict[col[0]] = row[idx]
    return dict

class OtmsDatabase():
    def __init__(self):
        self.con = sqlite3.connect('database/OTMS.db', check_same_thread=False)
        self.con.row_factory = dict_factory
        self.cur = self.con.cursor()

    def set_token(self, token):
        self.cur.execute('UPDATE otms SET token = ?', (token,))
        self.con.commit()

    def get_info(self):
        self.cur.execute('SELECT * FROM otms')
        return self.cur.fetchone()