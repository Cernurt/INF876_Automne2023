#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
Sum of two lowest positive integers

https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python
https://www.codewars.com/kata/558fc85d8fd1938afb000014/solutions/python

Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. 
No floats or non-positive integers will be passed.

For example, when an array is passed like [19, 5, 42, 2, 77], the output should be 7.

[10, 343445353, 3453445, 3453545353453] should return 3453455.

review: 
    2013/08/26

"""


@logging()
def sum_two_smallest_numbers(numbers):
    # your code here
    numbers.sort()

    return numbers[0] + numbers[1]


@logging("one line version")
def sum_two_smallest_numbers_1(numbers):
    return sum(sorted(numbers)[:2])


@logging("smallest1 < smallest2")
def sum_two_smallest_numbers_2(numbers):
    smallest1 = None
    smallest2 = None
    for n in numbers:
        if not smallest1 or n < smallest1:  # n < smallest1 < smallest2
            smallest2 = smallest1
            smallest1 = n
        elif not smallest2 or n < smallest2:    # smallest1 < n < smallest2
            smallest2 = n
    return smallest1 + smallest2


@logging("build-in function: min")
def sum_two_smallest_numbers_3(numbers):
    first_min = min(numbers)
    numbers.remove(first_min)
    second_min = min(numbers)
    return first_min + second_min


from heapq import nsmallest
@logging("heapq.nsmallest")
def sum_two_smallest_numbers_4(numbers):
    return sum(nsmallest(2, numbers))


@logging("list method pop and index")
def sum_two_smallest_numbers_5(numbers):
    return numbers.pop(numbers.index(min(numbers))) + numbers.pop(numbers.index(min(numbers)))


@pytest.mark.parametrize('number, expected', [[[5, 8, 12, 18, 22], 13],
                                              [[7, 15, 12, 18, 22], 19],
                                              [[25, 42, 12, 18, 22], 30],
                                              [[25, 42, 12, 18, 22, 1, 2], 3],
                                              [[25, 42, 12, 18, 22, 2, 2], 4],
                                              ])
def test_sum_two_smallest_numbers(number, expected):
    print()
    print("input".center(80, "="))
    print(number)
    print("input".center(80, "="))
    result = sum_two_smallest_numbers_2(number)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
