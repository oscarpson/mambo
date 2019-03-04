import sqlite3

class Sdatabase():
    def __init__(self):
        pass
        

    def  insertData(self,name,email):
        self.db = sqlite3.connect(':memory:')
        self.cursor = self.db.cursor()
        self.cursor.execute('''
            CREATE TABLE users(id INTEGER PRIMARY KEY, name TEXT,
                            phone TEXT, email TEXT unique, password TEXT)
        ''')
        self.db.commit()
        cursor = self.db.cursor()
        name1 = name

        email1 = email

        
        # Insert user 
        cursor.execute('''INSERT INTO users(name, email)
                        VALUES(?,?)''', (name1, email1))
        print('First user inserted')

        print('Second user inserted')
        
        self.db.commit()
        return 'First user inserted'
