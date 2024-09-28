import pytest
from praktikum.database import Database
from praktikum.bun import Bun
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from tests.helpers.ingridient import HOT_SAUCE, SOUR_CREAM, CHILI_SAUCE, CUTLET, DINOSAUR, SAUSAGE
from tests.helpers.bun import BLACK_BUN, WHITE_BUN, RED_BUN


class TestDatabase:
    @pytest.mark.parametrize("type_of_bun, price", ((BLACK_BUN.name, BLACK_BUN.price),
                                                    (WHITE_BUN.name, WHITE_BUN.price), (RED_BUN.name, RED_BUN.price)))
    def test_available_buns_true(self, type_of_bun, price):
        bun = Bun(type_of_bun, price)
        database = Database()
        database.buns.append(bun)
        assert bun in database.available_buns()

    @pytest.mark.parametrize("ingredient_type, name, amount", [
        (INGREDIENT_TYPE_SAUCE, HOT_SAUCE.name, HOT_SAUCE.price),
        (INGREDIENT_TYPE_SAUCE, SOUR_CREAM.name, SOUR_CREAM.price),
        (INGREDIENT_TYPE_SAUCE, CHILI_SAUCE.name, CHILI_SAUCE.price),
        (INGREDIENT_TYPE_FILLING, CUTLET.name, CUTLET.price),
        (INGREDIENT_TYPE_FILLING, DINOSAUR.name, DINOSAUR.price),
        (INGREDIENT_TYPE_FILLING, SAUSAGE.name, SAUSAGE.price)
    ])
    def test_available_ingredients(self, ingredient_type, name, amount):
        ingredient = Ingredient(ingredient_type, name, amount)
        database = Database()
        database.ingredients.append(ingredient)
        assert ingredient in database.available_ingredients()
