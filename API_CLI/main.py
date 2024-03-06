from data_client import Sqlite, Postgresql


def main():
    while True:
        choice_bd = input('''
Добро пожаловать !!!
Выберите БД:
1. Sqlite
2. Postgresql
Ваш выбор: ''')

        match choice_bd:
            case '1':
                db = Sqlite()
                break
            case '2':
                db = Postgresql()
                break
            case _:
                print('Вы не выбрали БД для подключения')

    while True:
        choice_menu = input('''
1. Показать все данные
2. Добавить данные
3. Обновить данные
4. Удалить данные
5. Выход
Ваш выбор: ''')

        match choice_menu:
            case '1':
                db.select()
            case '2':
                db.insert(input('Введите ваш логин: '), input('Введите ваш пароль: '))
            case '3':
                db.update(input('Введите ваш id: '), input('Введите ваш логин: '), input('Введите ваш пароль: '))
            case '4':
                db.delete(input('Введите ваш id: '))
            case '5':
                db.commit()
                break
            case _:
                print('Такого пункта меню нет')


if __name__ == '__main__':
    main()

# pyinstaller --onefile  main.py
