#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(
    "A client for Chicago Liquidity Institute Transactions")

parser.add_argument("--deposit", "-d", type=float, help="deposit amount")
parser.add_argument("--withdraw", "-w", type=float, help="withdraw amount")
parser.add_argument("--balance", "-b", action='store_true', help="get balance")
parser.add_argument("--trade", "-t", type=str, choices=['buy', 'sell'],
                    help="execute trade action")

args = parser.parse_args()

if args.deposit:
    print(f"Depositing: {args.deposit}")

if args.withdraw:
    print(f"Withdrawing: {args.withdraw}")

if args.balance:
    print(f"Your balance is: $422222223.14")

if args.trade:
    print(f"Executing trade action: {args.trade}")
