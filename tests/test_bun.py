import pytest

from praktikum.bun import Bun
from tests.helpers.bun import BLACK_BUN, RED_BUN, WHITE_BUN


class TestBun:
    @pytest.mark.parametrize('name, price', ((BLACK_BUN.name, BLACK_BUN.price), (WHITE_BUN.name, WHITE_BUN.price)))
    def test_get_bun_name(self, name, price):
        bun = Bun(name, price)
        bun_name = bun.get_name()
        assert bun_name == name

    @pytest.mark.parametrize('name, price', ((WHITE_BUN.name, WHITE_BUN.price), (RED_BUN.name, RED_BUN.price)))
    def test_get_bun_price(self, name, price):
        bun = Bun(name, price)
        bun_price = bun.get_price()
        assert bun_price == price
