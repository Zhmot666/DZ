# TODO: Реализовать на свободную темы все концепции ООП, соединенные единым смыслом. [ ]

class Ship:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed

    def move(self):
        print(f"{self.name} перемещается со скоростью {self.speed} узлов.")


class CargoShip(Ship):
    def __init__(self, name, speed, capacity):
        super().__init__(name, speed)
        self.capacity = capacity

    def load(self, cargo):
        print(f"{cargo} загружается на {self.name}.")


class PassengerShip(Ship):
    def __init__(self, name, speed, capacity):
        super().__init__(name, speed)
        self.capacity = capacity

    def board(self, passenger):
        print(f"{passenger} на борту {self.name}.")


class Engine:
    def __init__(self, power):
        self.power = power

    def start(self):
        print(f"Двигатель запустился с мощностью {self.power} л.с.")


class Captain:
    def __init__(self, name):
        self.name = name

    def steer(self, ship):
        print(f"Капитан {self.name} управляет кораблём {ship.name}.")


if __name__ == '__main__':
    engine = Engine(5000)
    captain = Captain("Эдвард Джон Смит")
    ship = Ship("Титаник", 20)
    cargo_ship = CargoShip("Лоретто", 25, 10000)
    passenger_ship = PassengerShip("Королева Мария", 30, 5000)

    engine.start()
    captain.steer(ship)
    ship.move()
    cargo_ship.load("Контейнеры")
    cargo_ship.move()
    passenger_ship.board("Пассажиры")
    passenger_ship.move()
