from praktikum.bun import Bun


class Test_bun():
    def test_get_name(self):
        bun = Bun("Spinach", 100)
        assert bun.get_name() == "Spinach"

    def test_get_price(self):
        bun = Bun("Spinach", 100)
        assert bun.get_price() == 100

    def test_change_name(self):
        bun = Bun("Spinach", 100)
        bun.name = "Brioche"
        assert bun.get_name() == "Brioche"

    def test_change_price(self):
        bun = Bun("Spinach", 100)
        bun.price = 150
        assert bun.get_price() == 150