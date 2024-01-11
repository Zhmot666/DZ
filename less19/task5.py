# TODO: Два метода в классе, [X]
# TODO: один принимает в себя либо строку, либо число.  [X]
#
# TODO: Если я передаю строку, то смотрим:
# TODO: если произведение гласных и согласных букв меньше или
#  равно длине слова, выводить все гласные, иначе согласные;  [X]
# TODO: если число то, произведение суммы чётных цифр на длину
#  числа.  [X]
# TODO: Длину строки и числа искать во втором методе.  [X]

class NewClass:

    def __init__(self):
        pass

    def result(self, param):
        len_param = self.calc_len(param)
        if param.isdigit():
            result = sum([int(i) for i in param if i in '24680']) * len_param
            print(f'Переданный параметр является числом. Результат вычислений равен: {result}')
        else:
            glas = sum([1 for i in param if i in 'аеёиоуыэюя'])
            if glas * (len_param - glas) <= len(param):
                result = [i for i in param if i in 'аеёиоуыэюя']
            else:
                result = [i for i in param if i not in 'аеёиоуыэюя']
            print(f'Переданный параметр является строкой. Вот результат обработки строки: {result}')

    def calc_len(self, param):
        return len(str(param))


def main():
    task5 = NewClass()
    task5.result(input('Введите строку для обработки: '))


if __name__ == "__main__":
    main()
