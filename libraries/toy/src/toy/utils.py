from string import ascii_lowercase
from random import choices


def random_letters(size: int) -> str:
    return ''.join(choices(ascii_lowercase, k=size))

