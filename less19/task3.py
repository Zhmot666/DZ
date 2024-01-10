# Создайте класс Example. [X]
#
# В нём пропишите 3 метода. Две переменные
# задайте статически(1®), [X]
# две динамически( int). [X]
#
# Первый метод: создайте переменную внутри этой функции и выведите её. [X]
#
# Второй метод: верните сумму 2-ух статичных переменных. [X]
#
# Третий метод: верните результат возведения первой динамической
# переменной во вторую динамическую переменную. [X]
#
# Создайте объект класса. [X]
# Вызовите эти методы. [X]
# Напечатайте первое статическое свойство. [X]

class Exemple:
    stat_var1 = 3
    stat_var2 = 5

    def __init__(self, dyn_var1, dyn_var2):
        self.dynamic_var1 = dyn_var1
        self.dynamic_var2 = dyn_var2

    def method1(self, dyn_var3):
        self.dynamic_var3 = dyn_var3
        print(f'Созданная переменная равна {self.dynamic_var3}')

    def method2(self):
        print(f'Сумма статичных переменных равна {self.stat_var1 + self.stat_var2}')

    def method3(self):
        print(f'Возведение первой динамической переменной в степень второй динамической переменной равно '
              f'{self.dynamic_var1**self.dynamic_var2}')


def main():
    Training_Object = Exemple(int(input('Введите первую динаимческую переменную: ')),
                              int(input('Введите вторую динаимческую переменную: ')))
    Training_Object.method1(int(input('Введите третью динаимческую переменную: ')))
    Training_Object.method2()
    Training_Object.method3()
    print(f'Первое статическое свойство - {Training_Object.stat_var1}')

if __name__ == "__main__":
    main()
