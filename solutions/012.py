# -*- coding: utf-8 -*-

"""
    > 012 @ Amazon
    ~~~~~~~~~~~~~~
    There exists a staircase with N steps, and you can climb up either 1 or 2 steps
    at a time. Given N, write a function that returns the number of unique ways you
    can climb the staircase. The order of the steps matters.

    For example, if N is 4, then there are 5 unique ways:

    - 1, 1, 1, 1
    - 2, 1, 1
    - 1, 2, 1
    - 1, 1, 2
    - 2, 2

    What if, instead of being able to climb 1 or 2 steps at a time, you could climb any
    number from a set of positive integers X? For example, if X = {1, 3, 5}, you could
    climb 1, 3, or 5 steps at a time.

"""


def num_of_ways_to_climb(n: int, steps: list):
    """
    :param n: number of steps
    :param steps: number of steps that can be taken
    :return: number of ways to use steps
    """

    if n < min(steps):
        return 0

    ways = 0
    for step in steps:
        if n == step:
            ways += 1
        elif n > step:
            ways += num_of_ways_to_climb(n - step, steps)

    return ways


if __name__ == '__main__':
    assert num_of_ways_to_climb(4, [1, 2]) == 5
