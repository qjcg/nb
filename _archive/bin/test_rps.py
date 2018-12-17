#!/usr/bin/env python3

import unittest

import rps

class TestRPS(unittest.TestCase):

    def test_gen_cpu_hand(self):
        hand = rps.gen_cpu_hand()
        self.assertIn(hand, ("rock", "paper", "scissors"))
