#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from functools import reduce

import pytest
from codewars.logger import logging

"""
Persistent Bugger.

https://www.codewars.com/kata/55bf01e5a717a0d57e0000ec/train/python

Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, 
which is the number of times you must multiply the digits in num until you reach a single digit.

For example (Input --> Output):
    39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
    999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)
    4 --> 0 (because 4 is already a one-digit number)

review: 
    2013/08/27

"""


@logging()
def persistence(n):
    p = 0
    lt = len(str(n))
    while lt > 1:
        numbers = str(n)
        n = reduce(lambda x, y: int(y) * int(x), numbers)
        lt = len(str(n))
        p += 1

    return p


import operator


@logging("operator.mul same as a*b")
def persistence_1(n):
    i = 0
    while n >= 10:
        n = reduce(operator.mul, [int(x) for x in str(n)], 1)
        i += 1
    return i


@logging("one line version with recursive")
def persistence_2_1(n):
    return 0 if n < 10 else persistence_2_1(reduce(operator.mul, [int(i) for i in str(n)], 1)) + 1


@logging("one line version with recursive and map")
def persistence_2_2(n, res=0):
    return persistence_2_2(reduce(operator.mul, map(int, str(n))), res + 1) if n > 9 else res


persistence_2_3 = lambda n, c=0: persistence_2_3(reduce(lambda x, y: int(x) * int(y), str(n)), c + 1) if n >= 10 else c


@logging("for loop other than reduce")
def persistence_3(n):
    n = str(n)
    count = 0
    while len(n) > 1:
        p = 1
        for i in n:
            p *= int(i)
        n = str(p)
        count += 1
    return count


@logging("% and // other than str(n)")
def persistence_4(n):
    if n < 10: return 0
    mult = 1
    while n > 0:
        mult = n % 10 * mult
        n = n // 10
    return persistence_4(mult) + 1


@logging("best: eval()")
def persistence_5(n):
    return 0 if n < 10 else persistence_5(eval('*'.join(str(n)))) + 1


@logging("2 arguments with lambda")
def persistence_6_1(n, result=0):
    if len(str(n)) == 1:
        return result
    else:
        return persistence_6_1(reduce(lambda x, y: int(x) * int(y), str(n), 1), result + 1)


@logging("2 arguments with for loop")
def persistence_6_2(n, t=0):
    n = str(n)
    z = 1
    if len(n) != 1:
        for x in n:
            z *= int(x)
        return persistence_6_2(z, t + 1)
    else:
        return t


@pytest.mark.parametrize('args, expected', [[39, 3], [4, 0], [25, 2], [999, 4]])
def test_persistence(args, expected):
    print()
    print("input".center(80, "="))
    print(args)
    print("input".center(80, "="))
    result = persistence_5(args)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
