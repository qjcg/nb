import trade


def arbitrage(mkt1, mkt2):
    """Execute arbitrage trade.
    """
    print(f"Arbitraging from {mkt1} to {mkt2}")


if __name__ == '__main__':
    arbitrage("USA", "CAN")
    trade.execute_trade("buy", "AAPL", 500.00)
    trade.execute_trade("sell", "RHT", 11500.00)
