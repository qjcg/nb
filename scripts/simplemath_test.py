import simplemath


def test_mul():
    assert simplemath.mul(5, 10) == 50


def test_mul_zero():
    assert simplemath.mul(100, 0) == 0


def test_add():
    assert simplemath.add(5, 10) == 15
