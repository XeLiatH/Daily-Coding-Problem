# -*- coding: utf-8 -*-

"""
    > 007 @ Facebook
    ~~~~~~~~~~~~~~~~
    Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the
    number of ways it can be decoded.
    
    For example, the message '111' would give 3, since it could be
    decoded as 'aaa', 'ka', and 'ak'.

    __
    You can assume that the messages are decodable. For example, '001' is not allowed.

"""


def memo(em: str, k: int, m: list):
    """
    Helper method for dynamic programming method -> memoize

    :param em: encoded message
    :param k:
    :param m: memo lookup variable
    :return: int
    """

    if k == 0:
        return 1

    s = len(em) - k
    if em[s] == '0':
        return 0

    if m[k] is not None:
        return m[k]

    result = memo(em, k - 1, m)
    if k >= 2 and int(em[s:s + 2]) <= 26:
        result += memo(em, k - 2, m)

    m[k] = result

    return result


def num_of_ways(em: str):
    """
    General idea is to split the problem into smaller problems
    1. for k == 0 -> return 1
    2. for

    :param em: encoded message
    :return: int
    """

    length = len(em)

    return memo(em, length, [None] * (length + 1))


if __name__ == '__main__':
    assert num_of_ways('111') == 3
    assert num_of_ways('123') == 3
    assert num_of_ways('011') == 0
