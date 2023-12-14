#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
Build Tower

https://www.codewars.com/kata/576757b1df89ecf5bd00073b/train/python

Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. 
A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:
[
  "  *  ",
  " *** ", 
  "*****"
]

review: 
    2013/08/27

"""


@logging()
def tower_builder(n_floors):
    sl = []

    for x in range(1, n_floors + 1):
        sn = '*' * (2 * x - 1)
        ss = ' ' * (n_floors - x)
        sl.append(ss + sn + ss)

    return sl


@logging("best: center")
def tower_builder_1(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]
    # return [("*" * (2*i+1)).center(2*(n-1)+1, " ") for i in range(n)]


@logging("one line version")
def tower_builder_2(n):
    return [" " * (n - i - 1) + "*" * (2*i + 1) + " " * (n - i - 1) for i in range(n)]


@logging("easy to understand")
def tower_builder_3(n_floors):
    tower = []
    spacing = n_floors - 1
    stars = 1
    for i in range(0, n_floors):
        tower.append(' ' * spacing + '*' * stars + spacing * ' ')
        stars += 2
        spacing -= 1
    return tower


@logging("string format")
def tower_builder_4(n_floors):
    return ['{0}{1}{0}'.format(' ' * (n_floors - 1 - x), '*' * (1 + 2 * x)) for x in range(n_floors)]


@logging("string format with center alignment")
def tower_builder_5(n):
    length = n * 2 - 1
    return ['{:^{}}'.format('*' * a, length) for a in range(1, length + 1, 2)]


@pytest.mark.parametrize('args, expected', [[1, ['*', ]], [2, [' * ', '***']], [3, ['  *  ', ' *** ', '*****']],
                                            [4, ['   *   ', '  ***  ', ' ***** ', '*******']]
                                            ])
def test_tower_builder(args, expected):
    print()
    print("input".center(80, "="))
    print(args)
    print("input".center(80, "="))
    result = tower_builder_5(args)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()

