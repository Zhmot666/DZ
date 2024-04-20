import sys
from ui import QtWidgets, MyApp


def main():
    app = QtWidgets.QApplication(sys.argv)
    windows = MyApp()
    windows.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
