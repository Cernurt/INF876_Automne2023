#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
Array.diff

https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result. 
It should remove all values from list a, which are present in list b keeping their order.
    array_diff([1,2],[1]) == [2]

If a value is present in b, all of its occurrences must be removed from the other:
    array_diff([1,2,2,2,3],[2]) == [1,3]

review: 
    2013/08/26

"""


@logging("remove items in b from a")
def array_diff(a, b):
    # remove items in b from a
    for e in b:
        # while a.count(e) > 0:
        while e in a:
            a.remove(e)
    return a


@logging("list comprehension: select items not in b from a")
def array_diff_1(a, b):
    return [x for x in a if x not in b]


@logging("list comprehension and set(b)")
def array_diff_2(a, b):
    return [x for x in a if x not in set(b)]


@logging("filter function")
def array_diff_3(a, b):
    return list(filter(lambda i: i not in b, a))


@pytest.mark.parametrize('l1, l2, expected', [([1, 2], [1], [2]), ([1, 2, 2], [1], [2, 2]), ([1, 2, 2], [2], [1]),
                                              ([1, 2, 2], [], [1, 2, 2]), ([], [1, 2], []), ([1, 2, 3], [1, 2], [3])])
def test_array_diff(l1, l2, expected):
    print()
    print("input".center(80, "="))
    print(l1, l2)
    print("input".center(80, "="))
    result = array_diff_3(l1, l2)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
