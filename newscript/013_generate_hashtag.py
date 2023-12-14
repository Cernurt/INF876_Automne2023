#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
The Hashtag Generator

https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

The marketing team is spending way too much time typing in hashtags.
Let's help them with our own Hashtag Generator!

Here's the deal:
    It must start with a hashtag (#).
    All words must have their first letter capitalized.
    If the final result is longer than 140 chars it must return false.
    If the input or the result is an empty string it must return false.

Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false

review: 
    2013/08/27

"""


@logging("Lance: title()")
def generate_hashtag(s):
    # if len(s) == 0 or len(s) > 140:
    #     return False
    # s = s.title().replace(" ", "")
    #
    # return "#"+s
    return '#' + s.strip().title().replace(' ', '') if 0 < len(s) <= 140 else False


@logging("best: title() and split()")
def generate_hashtag_1(s):
    return 0 if not s or len(s) > 140 else f'#{"".join(e for e in s.title().split())}'


@logging("capitalize()")
def generate_hashtag_2(s):
    output = "#"

    for word in s.split():
        output += word.capitalize()

    return False if (len(s) == 0 or len(output) > 140) else output


@logging("short version: capitalize()")
def generate_hashtag_3(s):
    if len(s) > 140 or not s: return False
    return '#' + ''.join(w.capitalize() for w in s.split())


generate_hashtag_4 = lambda d: (lambda b: d > '' < b == b[:139] and '#' + b)(d.title().replace(' ', ''))


@pytest.mark.parametrize('args, expected', [['Codewars', '#Codewars'], ['Codewars      ', '#Codewars'],
                                            ['      Codewars', '#Codewars'], ['Codewars Is Nice', '#CodewarsIsNice'],
                                            ['codewars is nice', '#CodewarsIsNice'], ['c i n', '#CIN'],
                                            ['CoDeWaRs is niCe', '#CodewarsIsNice'], ['', False],
                                            ['codewars  is  nice', '#CodewarsIsNice'],
                                            [
                                                'Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat',
                                                False]
                                            ])
def test_generate_hashtag(args, expected):
    print()
    print("input".center(80, "="))
    print(args)
    print("input".center(80, "="))
    result = generate_hashtag_4(args)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
