from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Test_ingridient():
    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Ketchup", 1.5)
        assert ingredient.get_name() == "Ketchup", "Метод get_name() должен возвращать 'Ketchup'"

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Cheese", 2.0)
        assert ingredient.get_price() == 2.0, "Метод get_price() должен возвращать 2.0"

    def test_get_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, "Mayonnaise", 1.0)
        assert ingredient.get_type() == "SAUCE", "Метод get_type() должен возвращать 'SAUCE'"

    def test_change_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Bacon", 3.0)
        ingredient.name = "Turkey"
        assert ingredient.get_name() == "Turkey", "После изменения name, get_name() должен возвращать 'Turkey'"

    def test_change_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Bacon", 3.0)
        ingredient.price = 4.5
        assert ingredient.get_price() == 4.5, "После изменения price, get_price() должен возвращать 4.5"

    def test_change_type(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, "Lettuce", 0.5)
        ingredient.type = INGREDIENT_TYPE_SAUCE
        assert ingredient.get_type() == INGREDIENT_TYPE_SAUCE, "После изменения type, get_type() должен возвращать 'SAUCE'"