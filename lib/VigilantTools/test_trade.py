import unittest
import trade

class TestTrade(unittest.TestCase):
    def test_sell(self):
        self.assertEqual(trade.sell(), "Sold 1 USD")
        self.assertEqual(trade.sell(5, 'CAD'), "Sold 5 CAD")
