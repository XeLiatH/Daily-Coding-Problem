# -*- coding: utf8 -*-


def simple_approach(k: int, numbers: list):
    """
    The simplest solution I could come up with
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
    print(simple_approach(17, [10, 15, 3, 7]))
