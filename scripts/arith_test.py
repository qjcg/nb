import arith

TEST_DATA_MUL = [
    {"input": (1, 2), "expected": 2},
    {"input": (2, 2), "expected": 4},
    {"input": (1000, 29), "expected": 29000},
]


def test_mul():
    for t in TEST_DATA_MUL:
        got = arith.mul(*t["input"])
        assert got == t["expected"], f"Expected {t['expected']}, Got: {got}"
