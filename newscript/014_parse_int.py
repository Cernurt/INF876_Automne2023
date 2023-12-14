#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
parseInt() reloaded

https://www.codewars.com/kata/525c7c5ab6aecef16e0001a5/train/python

In this kata we want to convert a string into an integer. The strings simply represent the numbers in words.

Examples:
    "one" => 1
    "twenty" => 20
    "two hundred forty-six" => 246
    "seven hundred eighty-three thousand nine hundred and nineteen" => 783919
    
Additional Notes:
    The minimum number is "zero" (inclusively)
    The maximum number, which must be supported is 1 million (inclusively)
    The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
    All tested numbers are valid, you don't need to validate them


"""


@logging()
def parse_int(s):
    # Define a dictionary that maps words to their numerical values
    numbers = {'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
               'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9,
               'ten': 10, 'eleven': 11, 'twelve': 12, 'thirteen': 13,
               'fourteen': 14, 'fifteen': 15, 'sixteen': 16, 'seventeen': 17,
               'eighteen': 18, 'nineteen': 19, 'twenty': 20, 'thirty': 30,
               'forty': 40, 'fifty': 50, 'sixty': 60, 'seventy': 70,
               'eighty': 80, 'ninety': 90, 'hundred': 100, 'thousand': 1000,
               'million': 1000000, 'billion': 1000000000, 'and': 0}
    # Split the input string into words
    words = s.strip().split()
    # Initialize variables to keep track of the current number and the total sum
    current_num = 0
    total_sum = 0
    # Loop through all the words
    for word in words:

        if word.count('-') > 0:
            wws = word.split('-')
            c_num = 0
            for w in wws:
                n = numbers[w]
                c_num += n
            current_num += c_num
            # total_sum += c_num
        else:

            # Get the numerical value of the word from the dictionary
            num = numbers[word]

            # If the word represents a multiple of 100 or higher, multiply the current
            # number by that value and add it to the total sum
            if num >= 1000:
                total_sum = (total_sum + current_num) * num
                current_num = 0

            elif num >= 100:
                current_num *= num
                total_sum += current_num
                current_num = 0
            # If the word represents a multiple of 10 or higher, add it to the current number
            elif num >= 10:
                current_num += num
            # Otherwise, add the value of the word to the current number
            else:
                current_num += num
    # Add the final current number to the total sum and return it
    return total_sum + current_num


ONES = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine',
        'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen',
        'eighteen', 'nineteen']
TENS = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


@logging("replace '-' and then split")
def parse_int_1(string):
    print(string)
    numbers = []
    for token in string.replace('-', ' ').split(' '):
        if token in ONES:
            numbers.append(ONES.index(token))
        elif token in TENS:
            numbers.append((TENS.index(token) + 2) * 10)
        elif token == 'hundred':
            numbers[-1] *= 100
        elif token == 'thousand':
            numbers = [x * 1000 for x in numbers]
        elif token == 'million':
            numbers = [x * 1000000 for x in numbers]
    return sum(numbers)


words = {w: n for n, w in enumerate(
    'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split())}
words.update(
    {w: 10 * n for n, w in enumerate('twenty thirty forty fifty sixty seventy eighty ninety hundred'.split(), 2)})
thousands = {w: 1000 ** n for n, w in enumerate(
    'thousand million billion trillion quadrillion quintillion sextillion septillion octillion nonillion decillion'.split(),
    1)}


def parse_int_2(strng):
    num = group = 0
    for w in strng.replace(' and ', ' ').replace('-', ' ').split():
        if w == 'hundred':
            group *= words[w]
        elif w in words:
            group += words[w]
        else:
            num += group * thousands[w]
            group = 0
    return num + group


@pytest.mark.parametrize('args, expected', [['one', 1], ['twenty', 20], ['two hundred forty-six', 246],
                                            ["seven hundred eighty-three thousand nine hundred and nineteen", 783919]])
def test_parse_int(args, expected):
    print()
    print("input".center(80, "="))
    print(args)
    print("input".center(80, "="))
    result = parse_int_2(args)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
