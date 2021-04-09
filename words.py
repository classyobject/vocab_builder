"""
    Copyright (c) 2021 SS
    File name: words.py
    Author: SS
    Date created: 2021-3-28
    Date last modified: 2021-3-28
    Python Version: 3.8
"""

import wordlist as wl


# Word categories in alphabetical order
Bad = wl.WordList(wl.BAD)
Baseball = wl.WordList(wl.BASEBALL)
Basketball = wl.WordList(wl.BASKETBALL)
Emotions = wl.WordList(wl.EMOTIONS)
Employment = wl.WordList(wl.EMPLOYMENT)
Environment = wl.WordList(wl.ENVIRONMENT)
Family = wl.WordList(wl.FAMILY)
Good = wl.WordList(wl.GOOD)
Helpful = wl.WordList(wl.HELP)
Sports = wl.WordList(wl.SPORTS)
Touching = wl.WordList(wl.TOUCHING)
Unhelpful = wl.WordList(wl._HELP)


# Return concatenated list of list(s)
def All():
    return wl.WordList._all
