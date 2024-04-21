import sqlite3


class Sqlite:

    __CONNECTION = sqlite3.connect('db_sv.db')
    __CREATE_TABLE_SCRIPTS = open('SQLScripts/create_scripts.txt').read()
    __INSERT_SERIES1 = open('SQLScripts/insert_series1.txt').read()
    __INSERT_SERIES2 = open('SQLScripts/insert_series2.txt').read()
    __CHECK_SERIES_INFO = open('SQLScripts/check_series_info.txt').read()
    __UPDATE_SERIES = open('SQLScripts/update_series.txt').read()
    __DELETE_ALL_SERIES = open('SQLScripts/delete_all_series.txt').read()
    __GET_SERIES_IMAGES = open('SQLScripts/get_series_images.txt').read()
    __GET_SERIES_INFO = open('SQLScripts/get_series_info.txt').read()
    __GET_SERIES_LIST = open('SQLScripts/get_series_list.txt').read()
    __GET_PLAYER_LINK = open('SQLScripts/get_player_link.txt').read()
    __GET_SERIES_LINK = open('SQLScripts/get_series_link.txt').read()

    def __init__(self):
        with self.__CONNECTION as self.sql:
            self.sql.executescript(self.__CREATE_TABLE_SCRIPTS)

    def insert_series(self, id_series, name_series, link_series):
        with self.__CONNECTION as self.sql:
            result = self.sql.execute(self.__INSERT_SERIES1, (id_series,))
            if result.fetchone():
                return False
        with self.__CONNECTION as self.sql:
            self.sql.execute(self.__INSERT_SERIES2, (id_series, name_series, link_series))
            self.sql.commit()

    def check_series_info(self, id_series):
        with self.__CONNECTION as self.sql:
            result = self.sql.execute(self.__CHECK_SERIES_INFO, (id_series,))
            check_result = result.fetchone()
            if check_result[0] is None or check_result[1] is None or check_result[2] is None:
                return False
            else:
                return True

    def update_series(self, id_series, info_series, image_series, link_player):
        with self.__CONNECTION as self.sql:
            self.sql.execute(self.__UPDATE_SERIES, (info_series, image_series, link_player, id_series))
            self.sql.commit()

    def delete_all_series(self):
        with self.__CONNECTION as self.sql:
            self.sql.execute(self.__DELETE_ALL_SERIES)
            self.sql.commit()

    def get_series_images(self, id_series):
        with self.__CONNECTION as self.sql:
            result = self.sql.execute(self.__GET_SERIES_IMAGES, (id_series,))
            return result.fetchone()

    def get_series_info(self, id_series):
        with self.__CONNECTION as self.sql:
            result = self.sql.execute(self.__GET_SERIES_INFO, (id_series,))
            return result.fetchone()

    def get_series_list(self):
        with self.__CONNECTION as self.sql:
            result = self.sql.execute(self.__GET_SERIES_LIST)
            return result.fetchall()

    def get_series_link(self, id_series):
        with self.__CONNECTION as self.sql:
            result = self.sql.execute(self.__GET_SERIES_LINK, (id_series,))
            return result.fetchone()[0]

    def get_player_link(self, id_series):
        with self.__CONNECTION as self.sql:
            result = self.sql.execute(self.__GET_PLAYER_LINK, (id_series,))
            return result.fetchone()[0]

    def close(self):
        self.__CONNECTION.commit()
        self.__CONNECTION.close()
