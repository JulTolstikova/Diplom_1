from unittest.mock import Mock

import pytest

import data
from praktikum.burger import Burger

class Test_burger():
    @pytest.fixture()
    def mock_bun(self):
        mock = Mock()
        mock.name = "spinach"
        mock.price = 100
        mock.get_name.return_value = "spinach"
        mock.get_price.return_value = 100
        return mock

    @pytest.fixture()
    def mock_ingredient(self):
        mock = Mock()
        mock.ingredient_type = "sauce"
        mock.name = "ketchup"
        mock.price = 50
        mock.get_name.return_value = "ketchup"
        mock.get_price.return_value = 50
        mock.get_type.return_value = "sauce"
        return mock

    def test_set_buns(mock_bun):
        # Создаем экземпляр бургера
        burger = Burger()
        # Устанавливаем булочку
        burger.set_buns(mock_bun)
        # Проверяем, что в бургере есть добавленная булочка
        assert burger.bun == mock_bun

    def test_add_ingredient_type(mock_bun, mock_ingredient):
        # Создаем экземпляр бургера
        burger = Burger()
        # Устанавливаем булочку
        burger.set_buns(mock_bun)
        # Добавляем ингридиент
        burger.add_ingredient(mock_ingredient)
        # Проверяем, что в бургере есть добавленный ингридиент
        assert burger.ingredients[0] == mock_ingredient

    def test_add_ingredient_quantity(mock_bun, mock_ingredient):
        # Создаем экземпляр бургера
        burger = Burger()
        # Устанавливаем булочку
        burger.set_buns(mock_bun)
        # Добавляем ингридиент
        burger.add_ingredient(mock_ingredient)
        # Проверяем, что добавлен один ингридиент
        assert len(burger.ingredients) == 1

    def test_remove_ingredient(mock_bun, mock_ingredient):
        # Создаем экземпляр бургера
        burger = Burger()
        # Устанавливаем булочку
        burger.set_buns(mock_bun)
        # Добавляем ингридиент
        burger.add_ingredient(mock_ingredient)
        # Удаляем ингридиент
        burger.remove_ingredient(0)
        # Проверяем, что в бургере нет ингридиентов
        assert len(burger.ingredients) == 0

    def test_move_ingredient(mock_bun, mock_ingredient):
        # Создаем экземпляр бургера
        burger = Burger()
        # Устанавливаем булочку
        burger.set_buns(mock_bun)
        # Добавляем два разных ингридиента
        salad = Mock()
        cheese = Mock()
        burger.add_ingredient(salad)
        burger.add_ingredient(cheese)
        # Меняем ингридиенты местами
        burger.move_ingredient(0, 1)
        # Проверяем, что ингридиенты располагаются в нужном порядке
        assert burger.ingredients == [cheese, salad]

    def test_burger_get_price(self, mock_bun, mock_ingredient):
        # Создаем экземпляр бургера
        burger = Burger()
        # Устанавливаем булочку и добавляем ингредиент
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        # Устанавливаем ожидаемую цену за бургер
        expected_price = mock_bun.get_price() * 2 + mock_ingredient.get_price()
        # Проверяем, что цена за бургер соответствует ожидаемой
        assert burger.get_price() == expected_price

    def test_get_receipt(self, mock_bun, mock_ingredient):
        # Создаем экземпляр бургера
        burger = Burger()
        # Устанавливаем булочку и добавляем ингредиент
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient)
        # Получаем чек
        receipt = burger.get_receipt()
        # Ожидаемый результат
        expected_receipt = (
            "(==== spinach ====)\n"
            "= sauce ketchup =\n"
            "(==== spinach ====)\n"
            "\nPrice: 250"
        )
        # Проверяем, что полученный чек совпадает с ожидаемым
        assert receipt == expected_receipt