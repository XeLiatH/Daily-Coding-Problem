# -*- coding: utf-8 -*-

"""
    > 002.solution
    ~~~~~~~~~~~~~~
    Finding the product off all numbers but itself

"""

from functools import reduce


def smart_approach(numbers: list):
    """
    Complexity O(2n) -> O(n)

    :param numbers:
    :return:
    """

    length = len(numbers)
    result = [None] * length

    product = reduce((lambda x, y: x * y), numbers)

    for i in range(length):
        result[i] = product / numbers[i]

    return result


def simple_approach(numbers: list):
    """
    Complexity O(n^2)

    :param numbers:
    :return:
    """

    length = len(numbers)
    array = [1] * length

    for i in range(length):
        for j in range(length):
            if i != j:
                array[i] *= numbers[j]
    return array


if __name__ == '__main__':
    print(simple_approach([1, 2, 3, 4, 5]))
    print(simple_approach([3, 2, 1]))
    print(smart_approach([1, 2, 3, 4, 5]))
    print(smart_approach([3, 2, 1]))
