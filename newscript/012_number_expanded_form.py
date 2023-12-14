#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
Write Number in Expanded Form

https://www.codewars.com/kata/5842df8ccbd22792a4000245/train/python

You will be given a number and you will need to return it as a string in Expanded Form. For example:
    expanded_form(12) # Should return '10 + 2'
    expanded_form(42) # Should return '40 + 2'
    expanded_form(70304) # Should return '70000 + 300 + 4'

NOTE: All numbers will be whole numbers greater than 0.

review: 
    2013/08/27

"""

@logging()
def expanded_form(n):
    s = ''
    quotient = n // 10
    if quotient == 0:
        return str(n)
    else:
        s += str(n % 10)

    bt = 1
    while quotient > 0:
        if quotient % 10 != 0:
                if eval(s) == 0:
                    s = str(quotient % 10 * 10 ** bt)
                else:
                    s = str(quotient % 10 * 10 ** bt) + " + " + s
        quotient = quotient // 10
        bt += 1

    return s


@logging("best: enumerate(num)")
def expanded_form_1(num):
    num = list(str(num))
    return ' + '.join(x + '0' * (len(num) - y - 1) for y, x in enumerate(num) if x != '0')
    # return " + ".join([str(int(d) * 10**p) for p, d in enumerate(str(num)[::-1]) if d != "0"][::-1])
    # return " + ".join([str(int(v)*int("1"+"0"*(len(str(num))-(i+1)))) for i,v in enumerate(str(num)) if v != "0"])


@logging("divmod: get every number and it digit position")
def expanded_form_2(n):
    result = []
    for i in range(len(str(n)) - 1, -1, -1):
        current = 10 ** i
        top, n = divmod(n, current)
        if top:
            result.append(str(top * current))
    return ' + '.join(result)


@logging("format: concat the number of 0 into string")
def expanded_form_3(num):
    num = str(num)
    st = ''
    for j, i in enumerate(num):
        if i != '0':
            st += ' + {}{}'.format(i, (len(num[j+1:])*'0'))
    return st.strip(' +')


def expanded_form_4(n):
    ns = str(n)
    result = ''
    for i in range(len(ns)-1, -1, -1):
        if ns[i] != '0':
            if result == '':
                result = str(int(ns[i]) * 10 ** (len(ns) - 1 - i))
            else:
                result = str(int(ns[i]) * 10 ** (len(ns)-1-i)) + ' + ' + result

    return result


@pytest.mark.parametrize('args, expected', [[12, '10 + 2'], [42, '40 + 2'], [70304, '70000 + 300 + 4'],
                                            [90000, '90000'], [241420, '200000 + 40000 + 1000 + 400 + 20']
                                            ])
def test_expanded_form(args, expected):
    print()
    print("input".center(80, "="))
    print(args)
    print("input".center(80, "="))
    result = expanded_form_2(args)
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()

