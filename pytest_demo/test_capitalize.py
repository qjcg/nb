import pytest


def capital_case(x):
    """Capitalize the string passed as argument.

    >>> capital_case("foo")
    'Foo'
    """
    if not isinstance(x, str):
        raise TypeError('Argument must be a string')
    return x.capitalize()


def test_capital_case():
    assert capital_case('semaphore') == 'Semaphore'


def test_raises_exception_on_non_string_arguments():
    with pytest.raises(TypeError):
        capital_case(9)
