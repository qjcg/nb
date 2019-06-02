import pytest
import stringfuncs


def test_my_upper():
    assert stringfuncs.my_upper("aaa") == "AAA"
    assert stringfuncs.my_upper("Hello World & DRW") == "HELLO WORLD & DRW"


def test_my_upper_empty():
    assert stringfuncs.my_upper("") == ""


def test_my_upper_badarg():
    with pytest.raises(AttributeError):
        stringfuncs.my_upper(42)
