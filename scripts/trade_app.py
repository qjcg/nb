#!/usr/bin/python3
# A basic trading application.

import trade

print(trade.execute_trade("buy", "AAPL", 50))
print(trade.execute_trade("sell", "GOOG", 99))

print("Testing whether NYSE is in list of known markets:")
print("NYSE" in trade.MARKETS)
