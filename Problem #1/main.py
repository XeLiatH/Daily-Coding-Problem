# -*- coding: utf8 -*-

"""First problem solution"""


def simple_approach(k: int, numbers: list):
    """
    The simplest, but dumbest solution
    Complexity close to O(n^2) in the worst case

    :param k: given number
    :param numbers: iterated array
    :return: True if any two numbers in the array equal to k
    """

    length = len(numbers)
    for i in range(length - 1):
        for j in range(i + 1, length):
            if numbers[i] + numbers[j] == k:
                return True
    return False


if __name__ == '__main__':
    arr = [10, 15, 3, 7]
    k = 17

    print(simple_approach(k, arr))
