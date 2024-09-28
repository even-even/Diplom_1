import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.helpers.ingridient import SALAT, MEAT


class TestIngredient:
    @pytest.mark.parametrize("ingredient_type, name, price", [
        (INGREDIENT_TYPE_SAUCE, SALAT.name, SALAT.price),
        (INGREDIENT_TYPE_FILLING, MEAT.name, MEAT.price)
    ])
    def test_get_type(self, ingredient_type, name, price):
        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type

    def test_get_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, SALAT.name, SALAT.price)
        assert ingredient.get_price() == SALAT.price

    def test_get_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_FILLING, MEAT.name, MEAT.price)
        assert ingredient.get_name() == MEAT.name
