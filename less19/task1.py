# TODO: Напишите программу с классом Саг. [X]
# TODO: Создайте динамические свойства класса Car — color (цвет), type (тип), year (год). [X]
# TODO: Напишите пять методов.  [X]
# TODO: Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». [X]
# TODO: Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». [X]
# TODO: Третий — присвоение автомобилю года выпуска. [X]
# TODO: Четвертый метод — присвоение автомобилю типа. [X]
# TODO: Пятый — присвоение автомобилю цвета [X]

class Car:
    
    def __init__(self):
        self.color = ''
        self.type = ''
        self.year = ''

    @staticmethod
    def start_car():
        print('Автомобиль заведен')

    @staticmethod
    def stop_car():
        print('Автомобиль заглушен')

    def year_car(self, input_year):
        self.year = input_year

    def type_car(self, input_type):
        self.type = input_type

    def color_car(self, input_color):
        self.color = input_color

    
def main():
    new_car = Car()
    print('Покупаем автомобиль. Введите характеристики')
    new_car.year_car(input('Введите год выпуска автомобиля: '))
    new_car.type_car(input('Введите тип автомобиля (седан, хэтчбек, купе и т.д.): '))
    new_car.color_car(input('Введите цвет автомобиля: '))
    print('Проверка автомобиля')
    print(f'Год выпуска: {new_car.year}')
    print(f'Тип: {new_car.type}')
    print(f'Цвет: {new_car.color}')
    print('Заводим!!!')
    new_car.start_car()
    print('Глушим')
    new_car.stop_car()
    print('Всё работает, можно брать! :)')


if __name__ == "__main__":
    main()
