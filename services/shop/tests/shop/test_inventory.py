import pytest

from shop.inventory import get_toys
from shop.models import ToyModel


@pytest.mark.parametrize(
    "size",
    list(range(2, 11, 2))
)
def test_get_toys(size):
    results = get_toys(size)
    assert len(results) == size
    assert all(isinstance(_t, ToyModel) for _t in results)

