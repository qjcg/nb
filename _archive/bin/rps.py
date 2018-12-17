#!/usr/bin/env python3
# Play rock paper scissors

import logging
import random
import sys

debug_mode = None
if len(sys.argv) > 1:
    debug_mode = sys.argv[1]

# Set up levelled logging.
if debug_mode:
    mylevel = logging.DEBUG
else:
    mylevel = logging.INFO

logging.basicConfig(filename='rps.log',level=mylevel)


hands = ("rock", "paper", "scissors")

def gen_cpu_hand():
    """Generate a hand for the CPU player.
    """
    hand = random.choice(hands)
    logging.debug(f"CPU hand selected: {hand}")
    return hand

if __name__ == '__main__':
    user_hand = input("Please choose a hand (rock, paper, scissors): ")
    cpu_hand = gen_cpu_hand()
    print(f"User: {user_hand}\nCPU: {cpu_hand}")
    logging.info(f"Game completed, User: {user_hand}, CPU: {cpu_hand}")
