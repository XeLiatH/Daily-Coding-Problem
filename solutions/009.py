# -*- coding: utf-8 -*-

"""
    > 009 @ Airbnb
    ~~~~~~~~~~~~~~
    Given a list of integers, write a function that returns the largest sum of non-adjacent
    numbers. Numbers can be 0 or negative.

    For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6,
    and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

    __
    Follow-up: Can you do this in O(N) time and constant space?

"""


def largest_sum(numbers: list):
    prev, largest = 0, 0
    for number in numbers:
        prev, largest = largest, max(largest, prev + number)

    return largest


if __name__ == '__main__':
    assert largest_sum([2, 4, 6, 2, 5]) == 13
    assert largest_sum([5, 1, 1, 5]) == 10
