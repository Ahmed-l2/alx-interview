#!/usr/bin/python3
"""Module for canUnlockAll function"""


def canUnlockAll(boxes):
    """a method that determines if all the boxes can be opened."""
    keys = [0]
    opened = []

    while (True):
        keyFound = False

        for index, box in enumerate(boxes):
            if index in keys and box not in opened:
                opened.append(index)
                for key in box:
                    if key not in keys:
                        keys.append(key)
                        keyFound = True

        if not keyFound:
            break

    if len(keys) == len(boxes):
        return True
    else:
        return False
