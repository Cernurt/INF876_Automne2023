#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
Middle character

You are going to be given a word. Your job is to return the middle character of the word. 
If the word's length is odd, return the middle character. If the word's length is even, return the middle 2 characters.

review: 
    2013/08/27

"""


@logging()
def get_middle(s):
    sl = len(s)
    if sl % 2 == 0:
        return s[(sl // 2-1):(sl // 2+1)]
    else:
        return s[(sl-1) // 2]


@logging("divmod: Return the tuple (x//y, x%y).")
def get_middle_1(s):
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]


@logging("best: reverse index")
def get_middle_2(s):
    i = (len(s) - 1) // 2
    return s[i:-i] or s


@logging("while: reverse index")
def get_middle_3(s):
    while len(s) > 2:
        s = s[1:-1]
    return s


@pytest.mark.parametrize('number, expected', [["test", "es"], ["testing", "t"], ["middle", "dd"], ["A", "A"],
                                              ["of", "of"]])
def test_get_middle(number, expected):
    print()
    print("input".center(80, "="))
    print(number)
    print("input".center(80, "="))
    result = get_middle_3(number)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()

