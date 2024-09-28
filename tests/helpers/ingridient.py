from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    price: float | int


SALAT = Ingredient(name='salat',
                   price=19.99)

MEAT = Ingredient(name='meat',
                  price=999.99)

HOT_SAUCE = Ingredient(name='hot sauce',
                     price=100)

SOUR_CREAM = Ingredient(name='hot sauce',
                     price=100)

CHILI_SAUCE = Ingredient(name='hot sauce',
                     price=100)

CUTLET = Ingredient(name='cutlet',
                    price = 100)

DINOSAUR = Ingredient(name="dinosaur",
                       price=200)

SAUSAGE = Ingredient(name='sausage',
                     price = 300)
