from abc import ABC, abstractmethod
import sqlite3
import psycopg2


class DB(ABC):

    @abstractmethod
    def select_persons(self):
        pass

    @abstractmethod
    def select_contacts(self, **kwargs):
        pass

    @abstractmethod
    def select_type_contacts(self, **kwargs):
        pass

    @abstractmethod
    def insert_person(self, **kwargs):
        pass

    @abstractmethod
    def insert_contact_info(self, **kwargs):
        pass

    @abstractmethod
    def insert_contact_type(self, **kwargs):
        pass

    @abstractmethod
    def update_person(self, **kwargs):
        pass

    @abstractmethod
    def update_contact_info(self, **kwargs):
        pass

    @abstractmethod
    def update_contact_type(self, **kwargs):
        pass

    @abstractmethod
    def delete_person(self, **kwargs):
        pass

    @abstractmethod
    def delete_contact_info(self, **kwargs):
        pass

    @abstractmethod
    def delete_contact_type(self, **kwargs):
        pass


class Sqlite(DB):
    __CONNECTION = sqlite3.connect('contact_list.db')

    __CREATE_SCRIPTS1 = '''CREATE TABLE IF NOT EXISTS Person(PersonID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            LastName VARCHAR(50) NOT NULL,
                                            FirstName VARCHAR(50) NOT NULL,
                                            Patronymic VARCHAR(50));'''
    __CREATE_SCRIPTS2 = '''CREATE TABLE IF NOT EXISTS ContactInfo(ContactID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            PersonID INT,
                                            Contact_data VARCHAR(100),
                                            ContactType INT,
                                            FOREIGN KEY(PersonID) REFERENCES Person(PersonID),
                                            FOREIGN KEY(ContactType) REFERENCES ContactTypes(TypeID));'''
    __CREATE_SCRIPTS3 = '''CREATE TABLE IF NOT EXISTS ContactTypes(TypeID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            TypeName VARCHAR(50) NOT NULL,
                                            Description VARCHAR(200));'''
    __CREATE_SCRIPTS4 = '''INSERT INTO ContactTypes (TypeName, Description) VALUES ('e-mail', 'Электронная почта')'''
    __CREATE_SCRIPTS5 = '''INSERT INTO ContactTypes (TypeName, Description) VALUES ('phone', 'Телефон')'''

    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.sql.execute(self.__CREATE_SCRIPTS1)
            self.sql.execute(self.__CREATE_SCRIPTS2)
            self.sql.execute(self.__CREATE_SCRIPTS3)
            if self.sql.execute('''SELECT * FROM ContactTypes''',).fetchall().__len__() == 0:
                self.sql.execute(self.__CREATE_SCRIPTS4)
                self.sql.execute(self.__CREATE_SCRIPTS5)

    def select_persons(self):
        with self.__CONNECTION as self.sql:
            [print(*data) for data in self.sql.cursor().execute('''SELECT PersonID as 'ID', 
                                                                        LastName as 'Фамилия', 
                                                                        FirstName as 'Имя', 
                                                                        Patronymic as 'Отчество' 
                                                                        FROM Person''').fetchall()]

    def select_contacts(self, id_person):
        with self.__CONNECTION as self.sql:
            [print(*data) for data in self.sql.cursor().execute(
                '''SELECT ci.ContactID AS 'ID',
                                ct.Description AS 'Тип контакта', 
                                ci.Contact_data AS 'Данные контакта' 
                                FROM ContactInfo AS ci
                                INNER JOIN ContactTypes AS ct ON ci.ContactType = ct.TypeID
                                WHERE ci.PersonID = ? ''',
                (id_person,)).fetchall()]

    def select_type_contacts(self):
        with self.__CONNECTION as self.sql:
            [print(*data) for data in self.sql.cursor().execute('''SELECT TypeID as 'ID', 
                                                                    Description as 'Вид контактной информации' 
                                                                    FROM ContactTypes''').fetchall()]

    def insert_person(self, last_name, first_name, patronymic):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''INSERT INTO Person (LastName, FirstName, Patronymic) 
                                VALUES (?, ?, ?)''', (last_name, first_name, patronymic))

    def insert_contact_type(self, type_name, description):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''INSERT INTO ContactTypes (TypeName, Description) 
                                VALUES (?, ?)''', (type_name, description))

    def insert_contact_info(self, id_contact, contact_type, contact_info):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''INSERT INTO ContactInfo (PersonID, Contact_data, ContactType) 
                                VALUES (?, ?, ?)''', (id_contact, contact_info, contact_type))

    def update_person(self, id_person, last_name, first_name, patronymic):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''UPDATE person SET LastName = ?, FirstName = ?, Patronymic = ? WHERE PersonID = ?''',
                             (last_name, first_name, patronymic, id_person))

    def update_contact_info(self, id_contact, contact_info):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''UPDATE ContactInfo SET Contact_data = ? WHERE ContactID = ?''',
                             (contact_info, id_contact))

    def update_contact_type(self, type_name, description, contact_type_id):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''UPDATE ContactTypes SET TypeName = ?, Description = ? WHERE TypeID = ?''',
                             (type_name, description, contact_type_id))

    def delete_person(self, id_user):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''DELETE FROM person WHERE PersonID = ?''', (id_user,))
            self.sql.execute('''DELETE FROM ContactInfo WHERE PersonID = ?''', (id_user,))

    def delete_contact_info(self, id_contact_info):
        with self.__CONNECTION as self.sql:
            self.sql.execute('''DELETE FROM ContactInfo WHERE ContactID = ?''', (id_contact_info,))

    def delete_contact_type(self, id_contact_info_type):
        with self.__CONNECTION as self.sql:
            if self.sql.execute('''SELECT * FROM ContactInfo WHERE ContactType = ?''',
                                (id_contact_info_type,)).fetchall().__len__() == 0:
                self.sql.execute('''DELETE FROM ContactTypes WHERE TypeID = ?''', (id_contact_info_type,))
            else:
                print('Удаление данных невозможно, так как данные связаны с другими таблицами')
                input('Для продолжения нажмите любую клавишу...')


class Postgresql(DB):
    # print('Заполните данные для подключения к PostgreSQL серверу. Для ввода данных по умолчанию просто нажмите Enter.')
    # host_name = input('Введите адрес сервера (по умолчанию: localhost):  ')
    # host_name = 'localhost' if host_name == '' else host_name
    # port_number = input('Введите порт сервера (по умолчанию: 5432):  ')
    # port_number = 5432 if port_number == '' else int(port_number)
    # base_name = input('Введите имя БД (по умолчанию: contact_list):  ')
    # base_name = 'contact_list' if base_name == '' else base_name
    # user_name = input('Введите имя пользователя (по умолчанию: postgres):  ')
    # user_name = 'postgres' if user_name == '' else user_name
    # base_password = input('Введите пароль:  ')
    # __CONNECTION = psycopg2.connect(host=host_name, port=port_number, database=base_name, user=user_name,
    #                                 password=base_password)


    __CONNECTION = psycopg2.connect(host='localhost', port='5432', database='contact_list', user='postgres',
                                    password='тут_должен_быть_пароль')
    __CONNECTION.autocommit = True
    __CREATE_SCRIPTS1 = '''CREATE TABLE IF NOT EXISTS Person(PersonID SERIAL PRIMARY KEY,
                                             LastName VARCHAR(50) NOT NULL,
                                             FirstName VARCHAR(50) NOT NULL,
                                             Patronymic VARCHAR(50));'''
    __CREATE_SCRIPTS2 = '''CREATE TABLE IF NOT EXISTS ContactTypes(TypeID SERIAL PRIMARY KEY,
                                             TypeName VARCHAR(50) NOT NULL,
                                             Description VARCHAR(200));'''
    __CREATE_SCRIPTS3 = '''CREATE TABLE IF NOT EXISTS ContactInfo(ContactID SERIAL PRIMARY KEY,
                                             PersonID INT,
                                             Contact_data VARCHAR(100),
                                             ContactType INT,
                                             FOREIGN KEY(PersonID) REFERENCES Person(PersonID),
                                             FOREIGN KEY(ContactType) REFERENCES ContactTypes(TypeID));'''

    __CREATE_SCRIPTS4 = '''INSERT INTO ContactTypes (TypeName, Description) VALUES ('e-mail', 'Электронная почта')'''
    __CREATE_SCRIPTS5 = '''INSERT INTO ContactTypes (TypeName, Description) VALUES ('phone', 'Телефон')'''

    def __init__(self):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute(self.__CREATE_SCRIPTS1)
            self.sql.execute(self.__CREATE_SCRIPTS2)
            self.sql.execute(self.__CREATE_SCRIPTS3)
            self.sql.execute("SELECT COUNT(*) FROM ContactTypes")
            record_count = self.sql.fetchone()[0]
            if record_count == 0:
                self.sql.execute(self.__CREATE_SCRIPTS4)
                self.sql.execute(self.__CREATE_SCRIPTS5)

    def select_persons(self):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''SELECT PersonID as "ID", 
                                 LastName as "Фамилия", 
                                 FirstName as "Имя", 
                                 Patronymic as "Отчество" 
                                 FROM Person''')
            [print(*data) for data in self.sql.fetchall()]

    def select_contacts(self, id_person):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute(
                '''SELECT ci.ContactID AS "ID",
                                ct.Description AS "Тип контакта", 
                                ci.Contact_data AS "Данные контакта" 
                                FROM ContactInfo AS ci
                                INNER JOIN ContactTypes AS ct ON ci.ContactType = ct.TypeID
                                WHERE ci.PersonID = %s ''', (id_person,))
            [print(*data) for data in self.sql.fetchall()]

    def select_type_contacts(self):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''SELECT TypeID as "ID", 
                                 Description as "Вид контактной информации" 
                                 FROM ContactTypes''')
            [print(*data) for data in self.sql.fetchall()]

    def insert_person(self, last_name, first_name, patronymic):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''INSERT INTO Person (LastName, FirstName, Patronymic) 
                                        VALUES (%s, %s, %s)''', (last_name, first_name, patronymic))

    def insert_contact_type(self, type_name, description):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''INSERT INTO ContactTypes (TypeName, Description) 
                                      VALUES (%s, %s)''', (type_name, description))

    def insert_contact_info(self, id_contact, contact_type, contact_info):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''INSERT INTO ContactInfo (PersonID, Contact_data, ContactType) 
                                    VALUES (%s, %s, %s)''', (id_contact, contact_info, contact_type))

    def update_person(self, id_person, last_name, first_name, patronymic):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''UPDATE person SET LastName = %s, FirstName = %s, Patronymic = %s 
                                        WHERE PersonID = %s''', (last_name, first_name, patronymic, id_person))

    def update_contact_info(self, id_contact, contact_info):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''UPDATE ContactInfo SET Contact_data = %s WHERE ContactID = %s''',
                             (contact_info, id_contact))

    def update_contact_type(self, type_name, description, contact_type_id):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''UPDATE ContactTypes SET TypeName = %s, Description = %s WHERE TypeID = %s''',
                             (type_name, description, contact_type_id))

    def delete_person(self, id_user):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''DELETE FROM person WHERE PersonID = %s''', (id_user,))
            self.sql.execute('''DELETE FROM ContactInfo WHERE PersonID = %s''', (id_user,))

    def delete_contact_info(self, id_contact_info):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''DELETE FROM ContactInfo WHERE ContactID = %s''', (id_contact_info,))

    def delete_contact_type(self, id_contact_info_type):
        with self.__CONNECTION.cursor() as self.sql:
            self.sql.execute('''SELECT * FROM ContactInfo WHERE ContactType = %s''',
                                             (id_contact_info_type,))
            select_result = self.sql.fetchall().__len__()
            if select_result == 0:
                self.sql.execute('''DELETE FROM ContactTypes WHERE TypeID = %s''', (id_contact_info_type,))
            else:
                print('Удаление данных невозможно, так как данные связаны с другими таблицами')
                input('Для продолжения нажмите любую клавишу...')


if __name__ == "__main__":
    pass
