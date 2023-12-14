#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging
from collections import Counter

"""
Take a Ten Minutes Walk

https://www.codewars.com/kata/54da539698b8a2ad76000228/train/python

You live in the city of Cartesia where all roads are laid out in a perfect grid. 
You arrived ten minutes too early to an appointment, so you decided to take the opportunity to go for a short walk. 
The city provides its citizens with a Walk Generating App on their phones -- everytime you press the button 
it sends you an array of one-letter strings representing directions to walk (eg. ['n', 's', 'w', 'e']). 

You always walk only a single block for each letter (direction) and you know it takes you one minute to traverse one city block, 
so create a function that will return true if the walk the app gives you will take you exactly ten minutes 
(you don't want to be early or late!) and will, of course, return you to your starting point. Return false otherwise.

Note: you will always receive a valid array containing a random assortment of direction letters ('n', 's', 'e', or 'w' only). 
It will never give you an empty array (that's not a walk, that's standing still!).

review: 
    2013/08/26

"""


@logging()
def is_valid_walk(walk):
    steps = len(walk)
    if steps != 10:
        return False
    count_s = walk.count('s')
    count_n = walk.count('n')
    count_e = walk.count('e')
    count_w = walk.count('w')
    if count_s == count_n and count_e == count_w:
        return True
    else:
        return False


@logging("one line version")
def is_valid_walk_1(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')


@logging("dictionary")
def is_valid_walk_2(walk):
    my_dict = dict.fromkeys(['n', 's', 'e', 'w'], 0)
    for i in walk:
        my_dict[i] += 1

    if (len(walk) == 10 and
            my_dict['n'] == my_dict['s'] and
            my_dict['e'] == my_dict['w']):
        return True
    return False


@logging("collections.Counter")
def is_valid_walk_3(walk):
    if len(walk) != 10:
        return False
    c = Counter(walk)
    return c['n'] == c['s'] and c['w'] == c['e']


@logging("best: complex number")
def is_valid_walk_4(walk):
    if len(walk) != 10: return False
    d = {'n': 1, 's': -1, 'w': 1j, 'e': -1j}
    return not sum(d[w] for w in walk)


@logging("best: variant of complex number")
def is_valid_walk_5(walk):
    if len(walk) != 10:
        return False

    x, y = 0, 0
    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
        else:
            return False

    return x == 0 and y == 0


@pytest.mark.parametrize('walk, expected', [[['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 's'], True],
                                            [['n', 'e', 's', 'w', 'n', 's', 'n', 'e', 's', 'w'], True],
                                            [['n', 's', 'n', 's', 'n', 's', 'n', 's', 'n', 'e'], False],
                                            [['w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e', 'w', 'e'], False],
                                            [['w'], False]])
def test_is_valid_walk(walk, expected):
    print()
    print("input".center(80, "="))
    print(walk)
    print("input".center(80, "="))
    result = is_valid_walk_2(walk)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
