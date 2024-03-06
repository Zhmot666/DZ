from abc import ABC, abstractmethod
import sqlite3
import psycopg2


class DB(ABC):

    @abstractmethod
    def select(self):
        pass

    @abstractmethod
    def insert(self, **kwargs):
        pass

    @abstractmethod
    def update(self, **kwargs):
        pass

    @abstractmethod
    def delete(self, **kwargs):
        pass


class Sqlite(DB):
    __CONNECTION = sqlite3.connect('db_sqlite.db')
    __CREATE_SCRIPTS = '''CREATE TABLE IF NOT EXISTS person(id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                                                           login TEXT UNIQUE,
                                                           password TEXT);'''

    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.sql.execute(self.__CREATE_SCRIPTS)

    def select(self):
        with self.__CONNECTION as self.sql:
            [print(*data) for data in self.sql.cursor().execute('''SELECT * FROM person''').fetchall()]

    # def update(self, id_user, login, password):
    def update(self, login, password, id_user):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''UPDATE person SET login = ?, password = ? WHERE id_user = ?''',
                             (login, hash(password), id_user))

    def insert(self, login, password):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''INSERT INTO person(login, password) VALUES(?, ?)''', (login, hash(password)))

    def delete(self, id_user):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''DELETE FROM person WHERE id_user = ?''', (id_user,))


class Postgresql(DB):
    __CONNECTION = psycopg2.connect(host='localhost', port='5432', database='cli_crud', user='postgres',
                                    password=input('Введите пароль для доступа к базе данных: '))
    __CREATE_SCRIPTS = '''CREATE TABLE IF NOT EXISTS person(id_user SERIAL PRIMARY KEY,
                                                           login TEXT UNIQUE,
                                                           password TEXT)'''

    def __init__(self):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute(self.__CREATE_SCRIPTS)

    def select(self):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''SELECT * FROM person''')
            [print(*data) for data in self.sql.fetchall()]

    def update(self, id_user, login, password):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''UPDATE person SET login = %S, password = %s WHERE id_user = %s''',
                             (login, hash(password), id_user))

    def insert(self, login, password):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''INSERT INTO person(login, password) VALUES(%s, %s)''', (login, hash(password)))

    def delete(self, id_user):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''DELETE FROM person WHERE id_user = %s''', (id_user,))

    def commit(self):
        self.__CONNECTION.commit()
