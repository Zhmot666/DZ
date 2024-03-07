from data_client import Sqlite, Postgresql
from pymenu import Menu


def db_selection(db_type: int):
    if db_type == 1:
        db = Sqlite()
    else:
        pass
        db = Postgresql()
    return


def main():
    print('Добро пожаловать в CRUD!!!')
    menu = Menu('Выберите БД:')
    menu.add_option("Sqlite", db_selection(1))
    menu.add_option("Postgresql", db_selection(2))
    menu.show()

    menu1 = Menu('Выбор действия')
    menu1.add_option("Показать все данные", lambda: print("SubOption 1"))
    menu1.add_option("Добавить данные", lambda: print("SubOption 2"))
    menu1.add_option("Изменить данные", lambda: print("SubOption 3"))
    menu1.add_option("Удалить данные", lambda: print("SubOption 4"))
    menu1.add_option("Выход", exit())
    menu1.show()

#     while True:
#         choice_bd = input('''
# Добро пожаловать !!!
# Выберите БД:
# 1. Sqlite
# 2. Postgresql
# Ваш выбор: ''')
#
#         match choice_bd:
#             case '1':
#                 db = Sqlite()
#                 break
#             case '2':
#                 db = Postgresql()
#                 break
#             case _:
#                 print('Вы не выбрали БД для подключения')
#
#     while True:
#         choice_menu = input('''
# 1. Показать все данные
# 2. Добавить данные
# 3. Обновить данные
# 4. Удалить данные
# 5. Выход
# Ваш выбор: ''')
#
#         match choice_menu:
#             case '1':
#                 db.select()
#             case '2':
#                 db.insert(input('Введите ваш логин: '), input('Введите ваш пароль: '))
#             case '3':
#                 db.update(input('Введите ваш id: '), input('Введите ваш логин: '), input('Введите ваш пароль: '))
#             case '4':
#                 db.delete(input('Введите ваш id: '))
#             case '5':
#                 db.commit()
#                 break
#             case _:
#                 print('Такого пункта меню нет')


if __name__ == '__main__':
    main()

# pyinstaller --onefile  main.py
