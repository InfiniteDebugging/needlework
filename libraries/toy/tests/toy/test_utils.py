import pytest

from toy.utils import random_letters


@pytest.mark.parametrize(
    "size",
    list(range(1, 10))
)
def test_random_letters(size: int):
    result = random_letters(size)
    assert len(result) == size

