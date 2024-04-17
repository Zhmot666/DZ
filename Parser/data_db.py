import sqlite3


class Sqlite:

    __CONNECTION = sqlite3.connect('db_sqlite.db')
    __CREATE_TABLE_SCRIPTS = open('create_scripts.txt').read()

    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.sql.executescript(self.__CREATE_TABLE_SCRIPTS)

    def insert(self, values: list):
        with self.__CONNECTION as self.sql:
            query = '''INSERT INTO iphone(title, price, link) VALUES(?, ?, ?)'''
            try:
                self.sql.executemany(query, values)
            except:
                print('Data save Error')

    def select(self):
        with self.__CONNECTION as self.sql:
            self.cursor = self.sql.cursor()
            self.cursor.execute('''SELECT * FROM iphone''')
            return self.cursor.fetchall()
