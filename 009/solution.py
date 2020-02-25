# -*- coding: utf-8 -*-

"""
    > 009.solution
    ~~~~~~~~~~~~~~
    Largest sum of non adjacent numbers

"""


def solve(numbers: list):
    prev, largest = 0, 0
    for number in numbers:
        prev, largest = largest, max(largest, prev + number)

    return largest


if __name__ == '__main__':
    print(solve([2, 4, 6, 2, 5]))
    print(solve([5, 1, 1, 5]))
