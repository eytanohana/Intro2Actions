from main import add, subtract, mulitply, divide, pow


def test_add():
    assert add(5, 5) == 10, 'Add failed'


def test_subtract():
    assert subtract(4, 3) == 1, 'Subtract failed'


def test_multiply():
    assert mulitply(6, 2) == 12, 'Multiply failed'


def test_divide():
    assert divide(28, 7) == 4, 'Divide failed'


def test_power():
    assert pow(2, 3) == 8, 'Power failed'
