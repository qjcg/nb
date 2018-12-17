#!/usr/bin/env python3
# Demonstrate GUI automation.

import pyautogui as gui

if __name__ == '__main__':
    w, h = gui.size()
    gui.moveTo(w/2, h/2)
