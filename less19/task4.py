# TODO: Калькулятор.
# TODO: Создайте класс, [X]
#  где реализованы функции(методы) математических операций. [X]
#  А также функция, для ввода данных. [X]

class Calc:

    def __init__(self):
        print('Привет! Я - простецкий калькулятор. Умею простые действия типа +,-,*,/.  Для того, что бы что-то '
              'посчитать, просто введите требуемое действие. Пример: 2+2 или 3*3, ну и т.д. А еще я умею во float :)'
              'Всё! Я готов к работе, погнали!!')

    def calculate(self, expression: str):
        if expression.find('+') != -1:
            return self.plus(expression.split('+'))
        elif expression.find('-') != -1:
            return self.minus(expression.split('-'))
        elif expression.find('/') != -1:
            return self.division(expression.split('/'))
        elif expression.find('*') != -1:
            return self.multiplication(expression.split('*'))
        else:
            return False

    @staticmethod
    def plus(variables):
        return float(variables[0]) + float(variables[1])

    @staticmethod
    def minus(variables):
        return float(variables[0]) - float(variables[1])

    @staticmethod
    def multiplication(variables):
        return float(variables[0]) * float(variables[1])

    @staticmethod
    def division(variables):
        return float(variables[0]) / float(variables[1])


def main():
    calculator = Calc()
    while True:
        result = calculator.calculate(input('Введите математическое выражение (для завершения работы калькулятора '
                                            'нажмите Enter в пустой строке): '))
        if result is False:
            print('До свидания!!!')
            break
        else:
            print(f'Результат вычислений равен: {result}')


if __name__ == "__main__":
    main()
