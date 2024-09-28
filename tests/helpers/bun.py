from dataclasses import dataclass


@dataclass
class Bun:
    name: str
    price: float | int

BLACK_BUN = Bun(name='black bun',
                     price=100)

WHITE_BUN = Bun(name='white bun',
                     price=200)

RED_BUN = Bun(name='red bun',
                     price=300)