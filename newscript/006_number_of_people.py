#!/usr/bin/python3
# -*- coding: UTF-8 -*-
from functools import reduce

import pytest
from codewars.logger import logging

"""
Number of People in the Bus

https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

There is a bus moving in the city which takes and drops some people at each bus stop.
You are provided with a list (or array) of integer pairs. Elements of each pair represent the number of people that get 
on the bus (the first item) and the number of people that get off the bus (the second item) at a bus stop.

Your task is to return the number of people who are still on the bus after the last bus stop (after the last array). 
Even though it is the last bus stop, the bus might not be empty and some people might still be inside the bus, 
they are probably sleeping there :D

Take a look on the test cases.
Please keep in mind that the test cases ensure that the number of people in the bus is always >= 0. 
So the returned integer can't be negative.

The second value in the first pair in the array is 0, since the bus is empty in the first bus stop.

review: 
    2013/08/26

"""


@logging()
def number(bus_stops):
    get_on = 0
    get_off = 0
    for i in range(len(bus_stops)):
        get_on += bus_stops[i][0]
        get_off += bus_stops[i][1]

    return get_on - get_off


@logging("list comprehension")
def number_1(bus_stops):
    return sum([stop[0] - stop[1] for stop in bus_stops])


@logging("best: list comprehension")
def number_2(bus_stops):
    return sum(on - off for on, off in bus_stops)


@logging("reduce")
def number_3(bus_stops):
    s = reduce(lambda a, b: [a[0]+b[0], a[1]+b[1]], bus_stops)
    print(s)
    return s[0] - s[1]

    # s = reduce(lambda a, b: [a[0]-a[1]+b[0]-b[1], 0], bus_stops)
    # return s[0]


@pytest.mark.parametrize('bus_stops, expected', [[[[10, 0], [3, 5], [5, 8]], 5],
                                              [[[3, 0], [9, 1], [4, 10], [12, 2], [6, 1], [7, 10]], 17],
                                              [[[3, 0], [9, 1], [4, 8], [12, 2], [6, 1], [7, 8]], 21]
                                              ])
def test_number(bus_stops, expected):
    print()
    print("input".center(80, "="))
    print(bus_stops)
    print("input".center(80, "="))
    result = number_2(bus_stops)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
