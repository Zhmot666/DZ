import requests
from PyQt5 import uic, QtWidgets
from PyQt5.QtGui import QPixmap
import sv_parse
import data_db
from sqlite3 import Binary as S3b
import webbrowser


class MyApp(QtWidgets.QMainWindow):
    def __init__(self):
        url = 'http://seasonvar.ru'
        super(MyApp, self).__init__()
        uic.loadUi("ui/form.ui", self)
        self.parser = sv_parse.SVparse(url)
        self.UpdateButton.clicked.connect(self.parse_today)
        self.PlayerButton.clicked.connect(self.click_play_button)
        self.db = data_db.Sqlite()
        self.TableSeries.cellClicked.connect(self.click_table_series)

    def parse_today(self):
        series_list = self.parser.parse_today()
        self.db.delete_all_series()
        for series in series_list:
            self.db.insert_series(series['id'], series['title'], series['link'])

        self.TableSeries.clear()
        self.TableSeries.setColumnCount(2)
        # self.TableSeries.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        self.TableSeries.horizontalHeader().setStretchLastSection(True)
        self.TableSeries.setHorizontalHeaderLabels(['ID', 'Название сериала'])
        self.TableSeries.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TableSeries.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.TableSeries.setAlternatingRowColors(True)
        self.TableSeries.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.TableSeries.setShowGrid(True)
        self.TableSeries.setSortingEnabled(False)
        self.TableSeries.setColumnHidden(0, True)
        self.TableSeries.setColumnHidden(1, False)

        self.TableSeries.setRowCount(0)
        series_list_db = self.db.get_series_list()
        for series in series_list_db:
            row = self.TableSeries.rowCount()
            self.TableSeries.insertRow(row)
            self.TableSeries.setItem(row, 0, QtWidgets.QTableWidgetItem(series[0]))
            self.TableSeries.setItem(row, 1, QtWidgets.QTableWidgetItem(str(series[1])))

        self.TableSeries.resizeColumnsToContents()
        self.TableSeries.resizeRowsToContents()

    def click_table_series(self):
        row = self.TableSeries.currentRow()
        series_id = self.TableSeries.item(row, 0).text()
        if not self.db.check_series_info(series_id):
            series_info = self.parser.parse_series(series_id)
            response = requests.get(series_info['img'])
            image_series = response.content
            self.db.update_series(series_id, series_info['description'], S3b(image_series), series_info['link'])
        get_information = self.db.get_series_info(series_id)
        self.DescriptionSeries.setText(get_information[1])
        with open('temp.jpg', "wb") as output_file:
            output_file.write(get_information[0])
        pixmap = QPixmap('temp.jpg')
        self.ImageSeries.setPixmap(pixmap)
        self.ImageSeries.setScaledContents(True)

    def click_play_button(self):
        row = self.TableSeries.currentRow()
        if row == -1:
            msg = QtWidgets.QMessageBox()
            msg.setIcon(QtWidgets.QMessageBox.Information)
            msg.setText("Выберите сериал для просмотра")
            msg.setWindowTitle("Ошибка")
            msg.exec_()
        else:
            series_id = self.TableSeries.item(row, 0).text()
            link = self.db.get_player_link(series_id)
            webbrowser.open('https:' + link)

    def closeEvent(self, event):
        self.db.close()
        self.TableSeries.clear()
