#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
Highest Scoring Word

https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

Given a string of words, you need to find the highest scoring word.
Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
For example, the score of abad is 8 (1 + 2 + 1 + 4).
You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string.
All letters will be lowercase and all inputs will be valid.

review: 
    2013/08/27

"""


@logging("Lance: list comprehension")
def high(x):
    words = x.split()
    score_lst = [sum([ord(i) - 96 for i in x]) for x in words]
    return words[score_lst.index(max(score_lst))]


@logging("list comprehension")
def high_0_2(x):
    s, n = x.split(), [sum(ord(c) - 96 for c in y) for y in x.split()]
    return s[n.index(max(n))]


@logging("best: one line with lambda")
def high_1(x):
    return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


@logging("for loop other than list comprehension")
def high_2(x):
    words = x.split(' ')
    lst1 = []
    for i in words:
        scores = [sum([ord(char) - 96 for char in i])]
        lst1.append(scores)
    return words[lst1.index(max(lst1))]


@logging("easy to understand")
def high_3(x):
    highest_score = 0
    for word in x.split(' '):
        score = sum(ord(c) - 96 for c in word)
        if score > highest_score:
            highest_score = score
            highest_word = word

    return highest_word


@logging("smart: max function with lambda key")
def high_4(words):
    return max(words.split(), key=lambda word: sum(ord(c) - ord('a') + 1 for c in word.lower()))


import string
@logging("smart: string class")
def high_5(x):
    return max(x.split(), key=lambda word: sum(string.ascii_lowercase.index(c)+1 for c in word))


@pytest.mark.parametrize('args, expected', [['man i need a taxi up to ubud', 'taxi'],
                                            ['what time are we climbing up the volcano', 'volcano'],
                                            ['take me to semynak', 'semynak'], ['aa b', 'aa'], ['b aa', 'b'],
                                            ['d bb', 'd'], ["aaa b", "aaa"]
                                            ])
def test_high_score(args, expected):
    print()
    print("input".center(80, "="))
    print(args)
    print("input".center(80, "="))
    result = high_5(args)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
