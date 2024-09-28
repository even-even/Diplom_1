from praktikum.burger import Burger
from unittest.mock import Mock
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.helpers.ingridient import HOT_SAUCE, CHILI_SAUCE, CUTLET, SAUSAGE
from tests.helpers.bun import BLACK_BUN


class TestBurger:
    def test_set_buns_true(self):
        mock_bun = Mock()
        mock_bun.name = BLACK_BUN.name
        mock_bun.price = BLACK_BUN.price
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun
        assert burger.bun.name == "black bun"
        assert burger.bun.price == 100

    def test_add_ingredient_true(self):
        mock_ingredient = Mock()
        mock_ingredient.type = INGREDIENT_TYPE_SAUCE
        mock_ingredient.name = HOT_SAUCE.name
        mock_ingredient.price = HOT_SAUCE.price
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients
        assert len(burger.ingredients) == 1

    def test_remove_ingredient_true(self):
        mock_ingredient = Mock()
        mock_ingredient.type = INGREDIENT_TYPE_FILLING
        mock_ingredient.name = SAUSAGE.name
        mock_ingredient.price = SAUSAGE.price
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert mock_ingredient not in burger.ingredients
        assert len(burger.ingredients) == 0

    def test_move_ingredient_true(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_1.type = INGREDIENT_TYPE_FILLING
        mock_ingredient_1.name = CUTLET.name
        mock_ingredient_1.price = CUTLET.price
        burger = Burger()
        burger.add_ingredient(mock_ingredient_1)

        mock_ingredient_2 = Mock()
        mock_ingredient_2.type = INGREDIENT_TYPE_SAUCE
        mock_ingredient_2.name = CHILI_SAUCE.name
        mock_ingredient_2.price = CHILI_SAUCE.price
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0, 1)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

    def test_get_price_true(self):
        mock_bun = Mock()
        mock_bun.get_price.return_value = 100  # Используем метод get_price
        burger = Burger()
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_price.return_value = 300  # Используем метод get_price
        burger.add_ingredient(mock_ingredient)

        expected_price = (mock_bun.get_price() * 2) + mock_ingredient.get_price()
        assert burger.get_price() == expected_price

    def test_get_receipt_true(self):
        burger = Burger()

        mock_bun = Mock()
        mock_bun.get_name.return_value = BLACK_BUN.name
        mock_bun.get_price.return_value = BLACK_BUN.price
        burger.set_buns(mock_bun)

        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = SAUSAGE.name
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_FILLING
        mock_ingredient.get_price.return_value = SAUSAGE.price
        burger.add_ingredient(mock_ingredient)

        expected_receipt = (
            "(==== black bun ====)\n"  # Имя булки
            "= filling sausage =\n"  # Ингредиент
            "(==== black bun ====)\n"  # Имя булки снова
            "\nPrice: 500"
        )
        assert burger.get_receipt() == expected_receipt
