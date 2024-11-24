from praktikum.database import Database
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class Test_database():
    def test_available_buns(self):
        database = Database()
        buns = database.available_buns()
        assert len(buns) == 3, "Должно быть три доступные булочки"
        assert buns[0].get_name() == "black bun", "Первая булочка должна быть 'black bun'"
        assert buns[1].get_name() == "white bun", "Вторая булочка должна быть 'white bun'"
        assert buns[2].get_name() == "red bun", "Третья булочка должна быть 'red bun'"
        assert buns[0].get_price() == 100, "Цена первой булочки должна быть 100"

    def test_available_ingredients(self):
        database = Database()
        ingredients = database.available_ingredients()
        assert len(ingredients) == 6, "Должно быть шесть доступных ингредиентов"
        assert ingredients[0].get_name() == "hot sauce", "Первый ингредиент должен быть 'hot sauce'"
        assert ingredients[0].get_type() == INGREDIENT_TYPE_SAUCE, "Первый ингредиент должен быть соусом"
        assert ingredients[3].get_name() == "cutlet", "Четвёртый ингредиент должен быть 'cutlet'"
        assert ingredients[3].get_type() == INGREDIENT_TYPE_FILLING, "Четвёртый ингредиент должен быть начинкой"