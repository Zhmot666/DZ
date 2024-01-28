# TODO: Напишите осмысленный декоратор. [X]

def decorator(func):
    def wrapper(param):
        if 'admin' == input('Для доступа к расчету введите имя пользователя: '):
            result = func(param)
            return result
        else:
            print('Недостаточно прав')
    return wrapper


@decorator
def exponentiation(param):
    print(f'Результат равен: {param * param}')


if __name__ == '__main__':
    exponentiation(int(input('Эта функция возводит любое число в квадрат. Введите число для расчета: ')))
