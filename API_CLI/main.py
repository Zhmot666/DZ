import tqdm
import os
import sys
from time import sleep
from data_client import Sqlite
from data_client import Postgresql


db = ''


def clear_cmd():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')


def sub_menu_select():
    global db
    while True:
        clear_cmd()
        print('Выберите действие')
        print('1. Просмотр списка абонентов')
        print('2. Просмотр контактов абонента')
        print('3. Возврат в предыдущее меню')
        print('4. Выход')
        selection = int(input('Введите номер пункта меню: '))
        match selection:
            case 1:
                clear_cmd()
                db.select_persons()
                input('Для продолжения нажмите любую клавишу...')
            case 2:
                clear_cmd()
                db.select_persons()
                db.select_contacts(int(input('Введите ID абонента: ')))
                input('Для продолжения нажмите любую клавишу...')
            case 3:
                break
            case 4:
                sys.exit(0)


def sub_menu_insert():
    global db
    while True:
        clear_cmd()
        print('Выберите действие')
        print('1. Добавление контакта')
        print('2. Добавление контактных данных')
        print('3. Добавление типа контактных данных')
        print('4. Возврат в предыдущее меню')
        print('5. Выход')
        selection = int(input('Введите номер пункта меню: '))
        match selection:
            case 1:
                last_name = input('Введите Фамилию контакта: ')
                first_name = input('Введите Имя контакта: ')
                patronymic = input('Введите Отчество контакта: ')
                db.insert_person(last_name, first_name, patronymic)
            case 2:
                clear_cmd()
                db.select_persons()
                id_contact = int(input('Введите ID абонента: '))
                db.select_type_contacts()
                contact_type = int(input('Введите ID вида контактной информации: '))
                contact_info = input('Введите контактную информацию: ')
                db.insert_contact_info(id_contact, contact_type, contact_info)
            case 3:
                clear_cmd()
                type_name = input('Введите вид контактной информации (phone, Skype и т.д.): ')
                description = input('А теперь то же самое но по русски :) ): ')
                db.insert_contact_type(type_name, description)
            case 4:
                break
            case 5:
                sys.exit(0)


def sub_menu_update():
    global db
    while True:
        clear_cmd()
        print('Выберите действие')
        print('1. Изменение контакта')
        print('2. Изменение контактных данных')
        print('3. Изменение типа контактных данных')
        print('4. Возврат в предыдущее меню')
        print('5. Выход')
        selection = int(input('Введите номер пункта меню: '))
        match selection:
            case 1:
                db.select_persons()
                id_contact = int(input('Введите ID абонента: '))
                last_name = input('Введите Фамилию контакта: ')
                first_name = input('Введите Имя контакта: ')
                patronymic = input('Введите Отчество контакта: ')
                db.update_person(id_contact, last_name, first_name, patronymic)
            case 2:
                clear_cmd()
                db.select_persons()
                id_contact = int(input('Введите ID абонента: '))
                db.select_contacts(id_contact)
                id_contact_info = int(input('Введите ID вида контактной информации: '))
                contact_info = input('Введите контактную информацию: ')
                db.update_contact_info(id_contact_info, contact_info)
            case 3:
                clear_cmd()
                db.select_type_contacts()
                print('ВНИМЕНИЕ!!! Изменения этой информации приведет к изменениям во всех связанных таблицах. '
                      'Будьте аккуратны и внимательны!')
                contact_type_id = int(input('Введите ID вида контактной информации: '))
                type_name = input('Введите вид контактной информации (phone, Skype и т.д.): ')
                description = input('А теперь то же самое но по русски :) ): ')
                db.update_contact_type(type_name, description, contact_type_id)
            case 4:
                break
            case 5:
                sys.exit(0)


def sub_menu_delete():
    global db
    while True:
        clear_cmd()
        print('Выберите действие')
        print('1. Удалить контакта')
        print('2. Удалить контактные данные')
        print('3. Удаление типа контактных данных')
        print('4. Возврат в предыдущее меню')
        print('5. Выход')
        selection = int(input('Введите номер пункта меню: '))
        match selection:
            case 1:
                db.select_persons()
                id_contact = int(input('Введите ID абонента: '))
                db.delete_person(id_contact)
            case 2:
                clear_cmd()
                db.select_persons()
                id_contact = int(input('Введите ID абонента: '))
                db.select_contacts(id_contact)
                id_contact_info = int(input('Введите ID вида контактной информации: '))
                db.delete_contact_info(id_contact_info)
            case 3:
                clear_cmd()
                db.select_type_contacts()
                print('ВНИМЕНИЕ!!! Удаление этой информации может привести к краху БАЗЫ ДАННЫХ. '
                      'Будьте аккуратны и внимательны!')
                contact_type_id = int(input('Введите ID вида контактной информации: '))
                db.delete_contact_type(contact_type_id)
            case 4:
                break
            case 5:
                sys.exit(0)


def sub_menu():
    global db
    while True:
        clear_cmd()
        print('Выберите действие')
        print('1. Просмотр данных')
        print('2. Добавление данных')
        print('3. Изменение данных')
        print('4. Удаление данных')
        print('5. Выход')
        selection = int(input('Введите номер пункта меню: '))
        match selection:
            case 1:
                sub_menu_select()
            case 2:
                sub_menu_insert()
            case 3:
                sub_menu_update()
            case 4:
                sub_menu_delete()
            case 5:
                sys.exit(0)


def main():
    global db
    clear_cmd()
    print('='*33)
    print('Добро пожаловать в адресную книгу')
    print('=' * 33)
    sleep(2)
    clear_cmd()
    while True:
        clear_cmd()
        print('Выберите тип СУБД для подключения')
        print('1. SQLite')
        print('2. Postgres')
        print('3. Выход')
        selection = int(input('Введите номер пункта меню: '))
        match selection:
            case 1:
                db = Sqlite()
                for _ in tqdm.tqdm(range(100)):
                    sleep(0.02)
                break
            case 2:
                db = Postgresql()
                for _ in tqdm.tqdm(range(100)):
                    sleep(0.02)
                break
            case 3:
                sys.exit(0)
            case _:
                print('Такого пункта меню не существует, попробуйте еще раз...')
                sleep(1)
    sub_menu()


if __name__ == '__main__':
    main()
