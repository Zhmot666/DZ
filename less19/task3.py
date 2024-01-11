# TODO: Создайте класс Example. [X]
# TODO: В нём пропишите 3 метода. Две переменные
#   задайте статически(1®), [X]
#   две динамически( int). [X]
# TODO: Первый метод: создайте переменную внутри этой функции и выведите её. [X]
# TODO: Второй метод: верните сумму 2-ух статичных переменных. [X]
# TODO: Третий метод: верните результат возведения первой динамической
#   переменной во вторую динамическую переменную. [X]
# TODO: Создайте объект класса. [X]
# TODO: Вызовите эти методы. [X]
# TODO: Напечатайте первое статическое свойство. [X]

class Example:
    stat_var1 = 3
    stat_var2 = 5

    def __init__(self, dyn_var1, dyn_var2):
        self.dynamic_var1 = dyn_var1
        self.dynamic_var2 = dyn_var2
        self.dynamic_var3 = 0

    def method1(self, dyn_var3):
        self.dynamic_var3 = dyn_var3
        print(f'Созданная переменная равна {self.dynamic_var3}')

    def method2(self):
        print(f'Сумма статичных переменных равна {self.stat_var1 + self.stat_var2}')

    def method3(self):
        print(f'Возведение первой динамической переменной в степень второй динамической переменной равно '
              f'{self.dynamic_var1**self.dynamic_var2}')


def main():
    training_object = Example(int(input('Введите первую динамическую переменную: ')),
                              int(input('Введите вторую динамическую переменную: ')))
    training_object.method1(int(input('Введите третью динамическую переменную: ')))
    training_object.method2()
    training_object.method3()
    print(f'Первое статическое свойство - {training_object.stat_var1}')


if __name__ == "__main__":
    main()
