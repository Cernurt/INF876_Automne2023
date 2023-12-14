#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import math
import pytest
from codewars.logger import logging

"""
A square of squares

https://www.codewars.com/kata/54c27a33fb7da0db0100040e/train/python

Given an integral number, determine if it's a square number:
In mathematics, a square number or perfect square is an integer that is the square of an integer; 
in other words, it is the product of some integer with itself.

The tests will always use some integral number, so don't worry about that in dynamic typed languages.

review: 
    2013/08/26

"""


@logging()
def is_square(n):
    if n == 0:
        return True
    elif n > 0:
        for i in range(n // 2 + 1):
            if i ** 2 == n:
                return True
            elif i ** 2 > n:
                break

    return False


@logging("math.sqrt")
def is_square_1(n):
    return n > -1 and math.sqrt(n) % 1 == 0


@logging("n**0.5")
def is_square_2(n):
    return n >= 0 and (n**0.5) % 1 == 0


@logging("n**0.5")
def is_square_3(n):
    if n >= 0:
        if int(n**.5)**2 == n:
            return True
    return False


@logging("best: is_integer()")
def is_square_4(n):
    return n >= 0 and math.sqrt(n).is_integer()


@pytest.mark.parametrize('number, expected', [[-1, False], [0, True], [1, True], [2, False], [4, True], [5, False]])
def test_is_square(number, expected):
    print()
    print("input".center(80, "="))
    print(number)
    print("input".center(80, "="))
    result = is_square_4(number)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
