from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Test_ingridient():
    def test_get_name(self):
        # Создаю ингридиент с определенными параметрами
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Ketchup", 50)
        # Проверяю, что метод возвращает верное имя
        assert ingredient.get_name() == "Ketchup"

    def test_get_price(self):
        # Создаю ингридиент с определенными параметрами
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Cheese", 70)
        # Проверяю, что метод возвращает верную цену
        assert ingredient.get_price() == 70

    def test_get_type(self):
        # Создаю ингридиент с определенными параметрами
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Mayonnaise", 50)
        # Проверяю, что метод возвращает верный тип
        assert ingredient.get_type() == "SAUCE", "Метод get_type() должен возвращать 'SAUCE'"

    def test_change_name(self):
        # Создаю ингридиент с определенными параметрами
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Bacon", 90)
        # Меняю имя ингридиента
        ingredient.name = "Turkey"
        # Проверяю, что возвращается измененное имя
        assert ingredient.get_name() == "Turkey"

    def test_change_price(self):
        # Создаю ингридиент с определенными параметрами
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Bacon", 90)
        # Меняю цену
        ingredient.price = 120
        # Проверяю, что возвращается измененная цена
        assert ingredient.get_price() == 120

    def test_change_type(self):
        # Создаю ингридиент с определенными параметрами
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Lettuce", 30)
        # Меняю тип ингридиента
        ingredient.type = INGREDIENT_TYPE_SAUCE
        # Проверяю, что возвращается измененный тип ингридиента
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE