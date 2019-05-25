import stringfuncs


TEST_DATA = [
    {"data": "aaa", "expected": "AAA"},
    {"data": "aaa aaa aaa", "expected": "AAA AAA AAA"},
]


def test_upper():
    for t in TEST_DATA:
        assert stringfuncs.my_upper(t["data"]) == t["expected"]
