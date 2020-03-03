# -*- coding: utf-8 -*-

"""
    > 002 @ Uber
    ~~~~~~~~~~~~
    Given an array of integers, return a new array such that each element at index i of
    the new array is the product of all the numbers in the original array except the one at i.
    For example, if our input was [1, 2, 3, 4, 5], the expected output would be
    [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

    __
    Follow-up: what if you can't use division?

"""

from functools import reduce


def calc_product_division(nums: list):
    """
    1. Calc product of all numbers
    2. Divide the product by each number
    3. Save the number to resulting list

    :param nums: given numbers
    :return:
    """

    length = len(nums)
    if length <= 0:
        return []

    result = [None] * length

    product = reduce((lambda x, y: x * y), nums)

    for i in range(length):
        result[i] = product / nums[i]

    return result


if __name__ == '__main__':
    assert calc_product_division([]) == []
    assert calc_product_division([1, 2, 3, 4, 5]) == [120, 60, 40, 30, 24]
    assert calc_product_division([3, 2, 1]) == [2, 3, 6]
