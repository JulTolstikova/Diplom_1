from praktikum.bun import Bun


class Test_bun():
    def test_get_name(self):
        # Создаем булочку с определенными параметрами
        bun = Bun("Spinach", 100)
        # Проверяем, что имя соответствует установленному
        assert bun.get_name() == "Spinach"

    def test_get_price(self):
        # Создаем булочку с определенными параметрами
        bun = Bun("Spinach", 100)
        # Проверяем, что цена соответствует установленной
        assert bun.get_price() == 100

    def test_change_name(self):
        # Создаем булочку с определенными параметрами
        bun = Bun("Spinach", 100)
        # Меняем имя
        bun.name = "Brioche"
        # Проверяем, что имя изменено
        assert bun.get_name() == "Brioche"

    def test_change_price(self):
        # Создаем булочку с определенными параметрами
        bun = Bun("Spinach", 100)
        # Меняем цену
        bun.price = 150
        # Проверяем, что цена изменена
        assert bun.get_price() == 150