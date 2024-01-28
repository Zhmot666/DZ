# Класс Tomato:
# TODO: Создайте класс Tomato [X]
# TODO: Создайте статическое свойство states, которое будет содержать все стадии созревания помидора [X]
# TODO: Создайте метод init(), внутри которого будут определены два динамических protected свойства: [X]
#  1) _index - передается параметром [X]
#  2) и _state - принимает первое значение из словаря states [X]
# TODO: Создайте метод grow(), который будет переводить томат на следующую стадию созревания [X]
# TODO: Создайте метод is_ripe(), который будет проверять, что томат созрел (достиг последней стадии созревания) [X]

# Класс TomatoBush
# TODO: Создайте класс TomatoBush [X]
# TODO: Определите метод init(), который будет принимать в качестве параметра количество томатов и на его основе будет
#  создавать список объектов класса Tomato. Данный список будет храниться внутри динамического свойства tomatoes. [X]
# TODO: Создайте метод grow_all(), который будет переводить все объекты из списка томатов
#  на следующий этап созревания [X]
# TODO: Создайте метод all_are_ripe(), который будет возвращать True, если все томаты из списка стали спелыми [X]
# TODO: Создайте метод give_away_all(), который будет чистить список томатов после сбора урожая [X]
#
# Класс Gardener
# TODO: Создайте класс Gardener [X]
# TODO: Создайте метод init(), внутри которого будут определены два динамических свойства:
#  1) name - передается параметром, является публичным [X]
#  2) и _plant - принимает объект класса Tomato, является protected [X]
# TODO: Создайте метод work(), который заставляет садовника работать,
#  что позволяет растению становиться более зрелым [X]
# TODO: Создайте метод harvest(), который проверяет, все ли плоды созрели. [X]
#  Если все - садовник собирает урожай. [X]
#  Если нет - метод печатает предупреждение. [X]
# TODO: Создайте статический метод knowledge_base(), который выведет в консоль справку по садоводству. [X]
#
# TODO: Вызовите справку по садоводству [X]
# TODO: Создайте объекты классов TomatoBush и Gardener [X]
# TODO: Используя объект класса Gardener, поухаживайте за кустом с помидорами [X]
# TODO: Попробуйте собрать урожай [X]
# TODO: Если томаты еще не дозрели, продолжайте ухаживать за ними [X]
# TODO: Соберите урожай [X]

class Tomato:
    states = {'Отсутствует': 0,
              'Цветение': 1,
              'Опыление': 2,
              'Формирование плода': 3,
              'Созревание': 4,
              'Готов к сбору урожая': 5}

    def __init__(self, index):
        self._index = index
        self._state = 0

    def grow(self):
        if self._state < 5:
            self._state += 1

    def is_ripe(self):
        return self._state == 5


class TomatoBush:
    def __init__(self, num):
        self.tomatoes = [Tomato(i) for i in range(num)]

    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    def all_are_ripe(self):
        return all([tomato.is_ripe() for tomato in self.tomatoes])

    def give_away_all(self):
        self.tomatoes = []


class Gardener:

    def __init__(self, name, plant):
        self.name = name
        self._plant = plant

    def work(self):
        self._plant.grow_all()

    def harvest(self):
        if self._plant.all_are_ripe():
            self._plant.give_away_all()
            print("Урожай собран!")
        else:
            print("Плоды еще не созрели.")

    @staticmethod
    def knowledge_base():
        print('Тут должна быть справка по садоводству, но так как я закончил с/х училище более 25 лет назад, то я '
              'ничего не помню и мне нечего сказать по этому поводу :)')


def main():
    Gardener.knowledge_base()
    bush = TomatoBush(5)
    gardener = Gardener('Ботанический сад', bush)
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.work()
    gardener.harvest()
    gardener.work()
    gardener.work()
    gardener.work()
    gardener.work()
    gardener.work()
    gardener.harvest()


if __name__ == '__main__':
    main()
