# Напишите программу с классом Саг. [X]
#
# Создайте динамические свойства класса Car — color (цвет), type (тип), year (год). [X]

# Напишите пять методов.
#
# Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». [X]
#
# Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». [X]
#
# Третий — присвоение автомобилю года выпуска. [X]
#
# Четвертый метод — присвоение автомобилю типа. [X]
#
# Пятый — присвоение автомобилю цвета [X]

class Car():
    
    def __init__(self):
        color = ''
        type = ''
        year = ''

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
    NewCar = Car()
    print('Покупаем автомобиль. Введите характеристики')
    NewCar.year_car(input('Введите год выпуска автомобиля: '))
    NewCar.type_car(input('Введите тип автомобиля (седан, хэчбэк, купе и т.д.): '))
    NewCar.color_car(input('Введите цвет автомобиля: '))
    print('Проверка автомобиля')
    print(f'Год выпуска: {NewCar.year}')
    print(f'Тип: {NewCar.type}')
    print(f'Цвет: {NewCar.color}')
    print('Заводим!!!')
    NewCar.start_car()
    print('Глушим')
    NewCar.stop_car()
    print('Всё работает, можно брать! :)')

if __name__ == "__main__":
    main()
