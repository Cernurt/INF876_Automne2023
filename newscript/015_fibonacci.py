#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
Memoized Fibonacci

https://www.codewars.com/kata/529adbf7533b761c560004e5/train/python

Problem Context
The Fibonacci sequence is traditionally used to explain tree recursion.
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
    
This algorithm serves well its educative purpose but it's tremendously inefficient, not only because of recursion, 
but because we invoke the fibonacci function twice, and the right branch of recursion (i.e. fibonacci(n-2)) 
recalculates all the Fibonacci numbers already calculated by the left branch (i.e. fibonacci(n-1)).

This algorithm is so inefficient that the time to calculate any Fibonacci number over 50 is simply too much. 
You may go for a cup of coffee or go take a nap while you wait for the answer. 
But if you try it here in Code Wars you will most likely get a code timeout before any answers.

For this particular Kata we want to implement the memoization solution. 
This will be cool because it will let us keep using the tree recursion algorithm 
while still keeping it sufficiently optimized to get an answer very rapidly.

The trick of the memoized version is that we will keep a cache data structure (most likely an associative array) 
where we will store the Fibonacci numbers as we calculate them. 
When a Fibonacci number is calculated, we first look it up in the cache, if it's not there, 
we calculate it and put it in the cache, otherwise we returned the cached number.

Refactor the function into a recursive Fibonacci function that using a memoized data structure 
avoids the deficiencies of tree recursion. Can you make it so the memoization cache is private to this function?

review: 
    2013/08/27

"""

fib_dict = {}


@logging()
def fibonacci(n):
    if n in [0, 1]:
        fib_dict[0] = 0
        fib_dict[1] = 1
        return n

    fbn = fib_dict.get(n, False)

    if not fbn:
        fbn = fibonacci(n - 1) + fibonacci(n - 2)
        fib_dict[n] = fbn

    return fbn


def memoized(f):
    cache = {}

    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v

    return wrapped


@memoized
def fibonacci_1(n):
    if n in [0, 1]:
        return n
    return fibonacci_1(n - 1) + fibonacci_1(n - 2)


from functools import lru_cache


@lru_cache(None)
def fibonacci_2(n):
    if n in [0, 1]:
        return n
    return fibonacci_2(n - 1) + fibonacci_2(n - 2)


@logging("best: fib list")
def fibonacci_3(n):
    fib = [0, 1]
    for i in range(2, n + 1):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib[n]


@logging("global dict")
def fibonacci_4(m):
    cache = {0: 0, 1: 1}

    def fib(n):
        if n not in cache:
            cache[n] = fib(n - 1) + fib(n - 2)
        return cache[n]

    return fib(m)


def fibonacci_5(n, p1=0, p2=1):
    if n == 1 or n == 0:
        return p2
    else:
        return fibonacci_5(n - 1, p2, p1 + p2)


def fibonacci_6(n, memo={}):
    if n in [0, 1]:
        return n
    if n not in memo:
        memo[n] = fibonacci_6(n - 1, memo) + fibonacci_6(n - 2, memo)
    return memo[n]


def fibonacci_7(n):
    f1, f2 = 0, 1
    for i in range(n):
        f1, f2 = f2, f1 + f2
    return f1


@pytest.mark.parametrize('args, expected', [[70, 190392490709135], [60, 1548008755920], [50, 12586269025]])
def test_fibonacci(args, expected):
    print()
    print("input".center(80, "="))
    print(args)
    print("input".center(80, "="))
    result = fibonacci_7(args)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
