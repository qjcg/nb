from trade import do_trade, do_arbitrage


def test_do_trade():
    assert do_trade() == 42


def test_arbitrage():
    assert do_arbitrage() == 43
