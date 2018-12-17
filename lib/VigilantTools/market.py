"""
The market module contains functions for interacting with financial markets.
"""

def arbitrage(m1='TSX', m2='NYSE'):
    """The arbitrage function will perform an arbitrage sale accross two
    markets passed as arguments:

        Args:
            m1, m2: string
        Returns:
            string

    >>> arbitrage()
    'Arbitrage from TSX to NYSE'

    >>> arbitrage('ABC', 'XYZ')
    'Arbitrage from ABC to XYZ'
    """

    return f"Arbitrage from {m1} to {m2}"
