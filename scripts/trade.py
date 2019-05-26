"""A basic DRW trading library.
"""

MARKETS = [
    "NYSE",
    "NQ",
    "TSX",
]


def execute_trade(action, stock, amount):
    """Buy or sell stocks.
    """
    return f"Executed action {action} for {amount} of {stock}"
