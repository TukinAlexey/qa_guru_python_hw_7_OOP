"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from homework.models import Product, Cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


@pytest.fixture
def cart():
    return Cart()


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1000)

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        assert product.buy(555) is None and product.quantity == 445

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    # Проверка добавление одинакового продукта
    def test_cart_add_product(self, cart, product):
        cart.add_product(product, 3)
        cart.add_product(product, 5)
        assert cart.products[product] == 8

    # Проверка добавление другого продукта
    def test_cart_add_another_product(self, cart, product):
        another_product = Product("car", 900, "This is a car", 500)
        cart.add_product(product, 3)
        cart.add_product(another_product, 5)
        assert cart.products[product] == 3 and cart.products[another_product] == 5

    # Проверка удаления продукта, если удаляется меньше чем есть в корзине
    def test_cart_remove_product(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 2)
        assert cart.products[product] == 1

    # Проверка удаления продукта, если удаляется больше чем есть в корзине
    def test_cart_remove_product_more(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 5)
        assert product not in cart.products

    # Проверка удаления продукта, если удаляется такое же количество как и в корзине
    def test_cart_remove_product_equals_cart(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, 3)
        assert product not in cart.products

    # Проверка удаления продукта, если не передан remove_count
    def test_cart_remove_product_none(self, cart, product):
        cart.add_product(product, 3)
        cart.remove_product(product, None)
        assert product not in cart.products

    # Проверка очистки корзины
    def test_cart_clear(self, cart, product):
        cart.add_product(product, 3)
        cart.clear()
        assert product not in cart.products

    # Посчитать стоимость товаров в корзине
    def test_cart_total_price(self, cart, product):
        another_product = Product("car", 50, "This is a car", 500)
        cart.add_product(another_product, 5)
        cart.add_product(product, 3)
        assert cart.get_total_price() == 550

    # Покупка продукта добавленного в корзину
    # Успешная покупка
    def test_cart_buy(self, cart, product):
        cart.add_product(product, 500)
        assert cart.buy() is None and product.quantity == 500 and product not in cart.products

    # Попытка купить больше продуктов чем есть в магазине
    def test_cart_buy_more(self, cart, product):
        with pytest.raises(ValueError):
            cart.add_product(product, 1001)
            cart.buy()
