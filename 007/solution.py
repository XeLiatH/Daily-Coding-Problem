# -*- coding: utf-8 -*-

"""
    > 007.solution
    ~~~~~~~~~~~~~~

"""


def memoized(em: str, k: int, memo: list):
    """
    Helper method for dynamic programming method -> memoize

    :param em: encoded message
    :param k:
    :param memo:
    :return: int
    """

    if k == 0:
        return 1

    s = len(em) - k
    if em[s] == '0':
        return 0

    if memo[k] is not None:
        return memo[k]

    result = memoized(em, k - 1, memo)
    if k >= 2 and int(em[s:s + 2]) <= 26:
        result += memoized(em, k - 2, memo)

    memo[k] = result

    return result


def solve(em: str):
    """
    Complexity should be O(2^n) but its more memory consuming since recursion

    :param em: encoded message
    :return: int
    """

    length = len(em)

    return memoized(em, length, [None] * (length + 1))


if __name__ == '__main__':
    print(solve('111'))
    print(solve('123'))
    print(solve('011'))
