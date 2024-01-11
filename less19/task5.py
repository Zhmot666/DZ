# TODO: Два метода в классе, [X]
# TODO: один принимает в себя либо строку, либо число.  []
#
# TODO: Если я передаю строку, то смотрим:
# TODO: если произведение гласных и согласных букв меньше или
#  равно длине слова, выводить все гласные, иначе согласные;  [ ]
# TODO: если число то, произведение суммы чётных цифр на длину
#  числа.  [ ]
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
            count_glas, count_sogl = 0, 0
            for i in param:
                if i in 'аеёиоуыэюя':
                    count_glas += 1
                else:
                    count_sogl += 1
            result = 0
            print(f'Переданный параметр является строкой. Результат вычислений равен: {result}')

    def calc_len(self, param):
        return len(str(param))


def main():
    task5 = NewClass()


if __name__ == "__main__":
    main()
