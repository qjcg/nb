#!/usr/bin/env python3
"""Play rock paper scissors.
"""

from argparse import ArgumentParser
import logging
import random


hands = ("rock", "paper", "scissors")


def gen_cpu_hand():
    """Generate a hand for the CPU player.
    """
    hand = random.choice(hands)
    logging.debug(f"CPU hand selected: {hand}")
    return hand


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-d', '--debug',
                        action='store_true', help="debug mode")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO)
    if args.debug:
        logging.getLogger().setLevel(logging.DEBUG)

    user_hand = input("Please choose a hand (rock, paper, scissors): ")
    cpu_hand = gen_cpu_hand()
    print(f"User: {user_hand}\nCPU: {cpu_hand}")
    logging.info(f"Game completed, User: {user_hand}, CPU: {cpu_hand}")
