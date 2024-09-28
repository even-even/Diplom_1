from dataclasses import dataclass


@dataclass
class Ingredient:
    name: str
    price: float | int

BLACK_BUN = Ingredient(name='black bun',
                     price=100)

WHITE_BUN = Ingredient(name='white bun',
                     price=200)

RED_BUN = Ingredient(name='red bun',
                     price=300)