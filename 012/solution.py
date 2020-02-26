# -*- coding: utf-8 -*-

"""
    > 012.solution
    ~~~~~~~~~~~~~~

"""


def solve(n: int, steps: list):
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
            ways += solve(n - step, steps)

    return ways


if __name__ == '__main__':
    assert solve(4, [1, 2]) == 5
