# -*- coding: utf-8 -*-

"""
    > 004.solution
    ~~~~~~~~~~~~~~
    Find first missing positive integer in order

"""


def find_missing_number(numbers: list):
    """
    Complexity 0(3n) -> O(n)

    :param numbers:
    :return:
    """

    if not numbers:
        return 1

    maximum = max(numbers)

    lookup = {}
    for num in numbers:
        lookup[num] = True

    # todo: Not sure if this complies with constant space since range creates a list of values
    for i in range(1, maximum):
        if not lookup.get(i):
            return i

    return maximum + 1


if __name__ == "__main__":
    print(find_missing_number([3, 4, -1, 1]))
    print(find_missing_number([-2, -1, 10]))
    print(find_missing_number([1, 2, 0]))
    print(find_missing_number([1, 2, 0, 4, 3, -1]))
