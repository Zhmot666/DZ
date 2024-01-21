# Класс Alphabet
# TODO: 1. Создайте класс Alphabet [X]
# TODO: 2. Создайте метод __init__(), внутри которого будут определены два динамических свойства:
#  1) lang - язык и 2) letters - список букв. Начальные значения свойств берутся из входных параметров метода. [X]
# TODO: 3. Создайте метод print(), который выведет в консоль буквы алфавита [X]
# TODO: 4. Создайте метод letters_num(), который вернет количество букв в алфавите [X]
#
# Класс EngAlphabet
# TODO: 1. Создайте класс EngAlphabet путем наследования от класса Alphabet [X]
# TODO: 2. Создайте метод __init__(), внутри которого будет вызываться родительский метод __init__().
#  В качестве параметров ему будут передаваться обозначение языка(например, 'En') и строка, состоящая из всех букв
#  алфавита(можно воспользоваться свойством ascii_uppercase из модуля string). [X]
# TODO: 3. Добавьте приватное статическое свойство __letters_num, которое будет хранить количество букв в алфавите. [X]
# TODO: 4. Создайте метод is_en_letter(), который будет принимать букву в качестве параметра и определять,
#  относится ли эта буква к английскому алфавиту. [X]
# TODO: 5. Переопределите метод letters_num() - пусть в текущем классе классе он будет возвращать значение
#  свойства __letters_num. [X]
# TODO: 6. Создайте статический метод example(), который будет возвращать пример текста на английском языке. [X]


from string import ascii_uppercase as sau


class Alphabet:
    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = letters

    def print(self):
        print(f'Список букв алфавита: {self.letters}')

    def letters_num(self):
        print(f'Количество букв в алфавите равно: {len(self.letters)}')


class EngAlphabet(Alphabet):
    __letters_num = ''

    def __init__(self, language, alphabet):
        super().__init__(language, alphabet)

    @property
    def letters_num(self):
        return self.__letters_num

    @letters_num.setter
    def letters_num(self, value):
        self.__letters_num = len(sau)

    def is_en_letter(self, letter_eng: str):
        if len(letter_eng) > 1:
            print('Строка содержит более одной буквы')
        elif letter_eng.upper() in self.letters:
            print(f'Буква {letter_eng} относится к английскому алфавиту')
        else:
            print(f'Буква {letter_eng} не относится к английскому алфавиту')

    @staticmethod
    def example():
        print('This is an example text in English')


def main():
    abc_eng = EngAlphabet('En', sau)
    abc_eng.print()
    print(abc_eng.letters_num)
    abc_eng.is_en_letter('F')
    abc_eng.is_en_letter('Щ')
    abc_eng.example()


if __name__ == '__main__':
    main()
