#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
Convert string to camel case

https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python
https://www.codewars.com/kata/517abf86da9663f1d2000003/solutions/python

Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also often referred to as Pascal case).
The next words should be always capitalized.

review:
    2023/08/25

key point:
    re.split("[-_]", text)
    text.replace('-', ' ').replace('_', ' ').split()
    x.capitalize()
    text.title()
    re.compile(r'(?i)[-_]([a-z])')  #(?!) means case-insensitive
    re.findall(r"[^-_]+", text)

review: 
    2013/08/26

"""
import re


@logging("list[:1] is a list")
def to_camel_case(text):
    if len(text) == 0:
        return ""
    str_list = re.split("[-_]", text)
    new_str = ''.join(str_list[:1] + [t.capitalize() for t in str_list[1:]])

    # # print(str_list)
    # new_str = str_list[0]
    # for i in range(1, len(str_list)):
    #     new_str = new_str + str_list[i].capitalize()

    return new_str


@logging("Coder1: replace")
def to_camel_case_1(text):
    removed = text.replace('-', ' ').replace('_', ' ').split()
    if len(removed) == 0:
        return ''
    return removed[0] + ''.join([x.capitalize() for x in removed[1:]])


@logging("Coder2: title")
def to_camel_case_2(text):
    return text[:1] + text.title()[1:].replace('_', '').replace('-', '')


@logging("Coder3: sub")
def to_camel_case_3(text):
    return re.sub('[_-](.)', lambda x: x.group(1).upper(), text)


@logging("Coder4: replace")
def to_camel_case_4(text):
    words = text.replace('_', '-').split('-')
    return words[0] + ''.join([x.title() for x in words[1:]])


PATTERN = re.compile(r'(?i)[-_]([a-z])')


@logging("Coder5: re.compile")
def to_camel_case_5(text):
    return PATTERN.sub(lambda m: m.group(1).upper(), text)


@logging("Coder6: list comprehension")
def to_camel_case_6(text):
    return text[0] + ''.join([w[0].upper() + w[1:] for w in text.replace("_", "-").split("-")])[1:] if text else ''


@logging("Coder7: map")
def to_camel_case_7(text):
    words = re.split(r'[-_]', text)
    words[1:] = list(map(str.capitalize, words[1:]))
    return "".join(words)
    # a = re.split('[-_]', text)
    # return a[0]+''.join(map(str.capitalize, a[1:]))


@logging("Coder8: findall")
def to_camel_case_8(text):
    text = re.findall(r"[^-_]+", text)
    return text[0] + "".join(w.capitalize() for w in text[1:]) if text else ""


@pytest.mark.parametrize('string, expected', [["", ""], ["the-stealth", "theStealth"],
                                              ["The_Stealth_Warrior", "TheStealthWarrior"],
                                              ["The_Stealth-Warrior-test", "TheStealthWarriorTest"]])
def test_to_camel_case(string, expected):
    print()
    print("input".center(80, "="))
    print(string)
    print("input".center(80, "="))
    result = to_camel_case_5(string)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
