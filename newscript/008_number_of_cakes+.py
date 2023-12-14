#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import pytest
from codewars.logger import logging

"""
Pete, the baker

https://www.codewars.com/kata/525c65e51bf619685c000059/train/python

Pete likes to bake some cakes. He has some recipes and ingredients. Unfortunately he is not good in maths. 
Can you help him to find out, how many cakes he could bake considering his recipes?

Write a function cakes(), which takes the recipe (object) and the available ingredients (also an object) and 
returns the maximum number of cakes Pete can bake (integer). 
For simplicity there are no units for the amounts (e.g. 1 lb of flour or 200 g of sugar are simply 1 or 200). 
Ingredients that are not present in the objects, can be considered as 0.

review: 
    2013/08/27

"""


@logging()
def cakes(recipe, available):
    s1 = set(recipe.keys())
    s2 = set(available.keys())
    s3 = s1 - s2
    print(s3)
    if len(s3) != 0:
        return False

    cc = []
    for k in s1:
        temp = available[k] // recipe[k]
        cc.append(temp)

    return min(cc)


@logging("best: dict.get(key, default)")
def cakes_1(recipe, available):
    return min(available.get(k, 0) // recipe[k] for k in recipe)
    # return min(available.get(k, 0) // v for k, v in recipe.iteritems())


@logging("smart: raise except when key does not in dict")
def cakes_2(recipe, available):
    try:
        return min([available[k] // recipe[k] for k in recipe])
    except:
        return 0


@logging("smart: list comprehension")
def cakes_3_1(recipe, available):
    ''' Take each ingredient from the recipe, see if it is in the available ones
        and calculate how many full cakes you can make with it.
        If an ingredient is missing, we can't bake a cake. Otherwise we have to
        find the lowest possible amount of cakes.'''
    return min([available[k]//recipe[k] if k in available else 0 for k in recipe])


@logging("smart: long version of cakes_3_1")
def cakes_3_2(recipe, available):
    list = []
    for ingredient in recipe:
        if ingredient in available:
            list.append(available[ingredient]//recipe[ingredient])
        else:
            return 0
    return min(list)


@pytest.mark.parametrize('args, expected',
                         [[[{"flour": 500, "sugar": 200, "eggs": 1},
                            {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}], 2],
                          [[{"flour": 500, "sugar_": 200, "eggs": 1},
                            {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}], 0],
                          [[{"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100},
                            {"sugar": 500, "flour": 2000, "milk": 2000}], 0],
                          ])
def test_cakes(args, expected):
    print()
    print("input".center(80, "="))
    print(args)
    print("input".center(80, "="))
    result = cakes_1(args[0], args[1])
    assert result == expected
    print("output".center(80, "*"))
    print(result)
    print("output".center(80, "*"))
    print()
