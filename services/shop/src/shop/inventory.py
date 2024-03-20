from decimal import Decimal
from random import random, randint
from toy.utils import random_letters

from shop.models import ToyModel


def _to_money(number: float) -> Decimal:
    return Decimal(round(number, 2))


def get_toys(n: int) -> list[ToyModel]:
    return [
        ToyModel(
            name=random_letters(randint(2, 5)),
            price=_to_money(10 * random()),
        )
        for _ in range(n)
    ]

