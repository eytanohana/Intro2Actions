from main import add, subtract, mulitply, divide
import sys


def tast_add():
    if sys.version_info.minor == 11:
        raise ValueError("AHHH I FAILED!!")
    assert add(5, 5) == 10, 'Add failed'


def test_subtract():
    assert subtract(4, 3) == 1, 'Subtract failed'


def test_multiply():
    assert mulitply(6, 2) == 12, 'Multiply failed'


def test_divide():
    assert divide(28, 7) == 4, 'Divide failed'

