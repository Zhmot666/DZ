# TODO: Создайте класс Soda (для определения типа газированной воды), [X]
# TODO: принимающий 1 аргумент при инициализации (отвечающий за
#   добавку к выбираемому лимонаду, тип данных строка).  [X]
#
# TODO: В этом классе реализуйте метод show_my_drink(), [X]
#  выводящий на печать «Газировка и {ДОБАВКА}» в случае наличия добавки, [X]
#  а иначе отобразится следующая фраза: «Обычная газировка».  [X]

class Soda:
    additive = ''

    def __init__(self, additive):
        self.additive = additive

    def show_my_drink(self):
        print(f'Обычная газировка') if self.additive == '' else print(f'Газировка и {self.additive}')


def main():
    my_limonade = Soda(input('Введите наименование наполнителя (если ничего - нажмите Enter): '))
    my_limonade.show_my_drink()


if __name__ == "__main__":
    main()
