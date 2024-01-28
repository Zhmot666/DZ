# TODO: Дан класс корзина продуктов. [ ]
# TODO: реализовать сложение и вычитание из продуктов.  [ ]
# TODO: В качестве корзины предусмотреть словарь, в который будут помещены продукты, [ ]
# TODO: Создаете 2 разных объекта, они должны складывать, вычитать.  [ ]
# TODO: **Так же реализуйте бонусную систему.

from random import randint as ri


class ProductBasket:
    def __init__(self):
        self.products = {}

    def __add__(self, other):
        result = ProductBasket()
        for product_name, quantity in self.products.items():
            result.add_product(product_name, quantity)
        for product_name, quantity in other.products.items():
            result.add_product(product_name, quantity)
        return result

    def __sub__(self, other):
        result = ProductBasket()
        product_name, quantity = next(iter(other.items()))
        for product_name, quantity in self.products.items():
            result.add_product(product_name, quantity)
        return result

    def add_product(self, product_name, quantity):
        if product_name in self.products:
            self.products[product_name] += quantity
        else:
            self.products[product_name] = quantity

    def remove_product(self, product_name, quantity):
        if product_name in self.products:
            if self.products[product_name] > quantity:
                self.products[product_name] -= quantity
            else:
                del self.products[product_name]

    def get_total_price(self):
        total_price = 0
        for product_name, quantity in self.products.items():
            total_price += quantity * self.get_product_price(product_name)
        return total_price

    def get_product_price(self, product_name):
        return 0

class Store(ProductBasket):
    def __init__(self):
        super().__init__()
        self.fill_store()

    def fill_store(self):
        fruits = ['яблоко', 'апельсин', 'банан', 'груша', 'мандарин']
        for fruit in fruits:
            self.add_product(fruit, ri(1, 20))

    def get_product_price(self, product_name):
        if product_name == 'яблоко':
            return 1.5
        elif product_name == 'банан':
            return 2.0
        elif product_name == 'апельсин':
            return 1.0
        elif product_name == 'груша':
            return 1.2
        elif product_name == 'мандарин':
            return 0.8
        else:
            return 0


class CustomerBasket(ProductBasket):
    def __init__(self):
        super().__init__()

    def get_product_price(self, product_name):
        return Store().get_product_price(product_name)

    def get_discounted_price(self):
        total_price = self.get_total_price()
        if total_price > 100:
            return total_price * 0.9
        else:
            return total_price


if __name__ == '__main__':
    store = Store()
    basket = CustomerBasket()

    print('Содержимое магазина:')
    for product_name, quantity in store.products.items():
        print(f'{product_name}: {quantity}')

    print('Содержимое корзины покупателя:')
    for product_name, quantity in basket.products.items():
        print(f'{product_name}: {quantity}')

    store - {'яблоко': 3}
    basket + {'яблоко': 3}

    print('Содержимое магазина после перемещения:')
    for product_name, quantity in store.products.items():
        print(f'{product_name}: {quantity}')

    print('Содержимое корзины покупателя после перемещения:')
    for product_name, quantity in basket.products.items():
        print(f'{product_name}: {quantity}')

    print(f'Общая стоимость продуктов в корзине покупателя: {basket.get_total_price()} руб.')
    print(f'Цена со скидкой: {basket.get_discounted_price()} руб.')
