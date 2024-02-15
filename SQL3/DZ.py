# TODO: Создать 2 таблицы в Базе Данных. [X]
# TODO: Одна таблица будет хранить текстовые данные(1 колонка), [ X]
# TODO: другая числовые (1 колонка). [X]
# TODO: Есть список, состоящий из чисел и слов. [X]
# TODO: Если элемент списка слово: записать его в соответствующую таблицу, [X]
# TODO: затем посчитать длину слова и записать её в числовую таблицу. [X]
# TODO: Если элемент списка число: проверить, если число чётное записать его в таблицу чисел, [X]
# TODO: если нечётное, то записать во вторую таблицу слово: «нечётное» [X]
# TODO: Если число записей во второй таблице больше 5, то удалить 1 запись в первой таблице. [X]
# TODO: Если меньше, то обновить 1 запись в первой таблице на «hello» [ ]

import sqlite3
import random


def create_field(conn, table_name, column_name, value):
    sql = f"INSERT INTO {table_name} ({column_name}) VALUES (?)"
    conn.execute(sql, (value,))
    conn.commit()


# Генератор случайного списка слов и чисел
def list_generation(long_list):
    r_l = list()
    words_list = ['дом', 'лес', 'гора', 'рука', 'день', 'ночь', 'глаз', 'свет', 'мост', 'путь', 'душа', 'вода', 'цвет',
                  'муза', 'книга', 'поле', 'голос', 'сон', 'мед', 'гриб', 'друг', 'парк', 'дым', 'море', 'град',
                  'песок', 'пламя', 'камень', 'снег', 'птица', 'волк', 'цветок', 'звук', 'дождь', 'полет', 'звезда',
                  'мечта', 'песня', 'время', 'полет', 'порт', 'парус', 'молоко', 'полет', 'портфель', 'печь', 'полет',
                  'портфель', 'печь', 'полет']
    for i in range(long_list):
        if random.choice([1, 2]) == 1:
            r_l.append(random.randint(1, 10))
        else:
            r_l.append(random.choice(words_list))
    return r_l


def main():
    random_list = list_generation(int(input('Введите длину генерируемого списка: ')))
    print(random_list)
    connection = sqlite3.connect('DB_DZ.db')
    cursor = connection.cursor()
    cursor.execute('''DROP TABLE IF EXISTS text_table''')
    cursor.execute('''DROP TABLE IF EXISTS number_table''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS text_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        text_fields TEXT
        )
    ''')
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS number_table (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        number_fields INTEGER
        )
    ''')
    for i in random_list:
        if isinstance(i, str):
            create_field(connection, 'text_table', 'text_fields', i)
            create_field(connection, 'number_table', 'number_fields', len(i))
        else:
            if i % 2 == 0:
                create_field(connection, 'number_table', 'number_fields', i)
            else:
                create_field(connection, 'text_table', 'text_fields', 'нечётное')

    result = (connection.execute(f"SELECT COUNT(*) FROM number_table")).fetchone()
    cursor = connection.cursor()
    if result[0] > 5:
        cursor.execute('DELETE FROM text_table WHERE id=1')
    else:
        cursor.execute('''UPDATE text_table SET text_fields = 'hello' WHERE id = 1''')
    connection.commit()
    connection.close()


if __name__ == "__main__":
    main()
