# -*- coding: utf-8 -*-

"""
    > 004 @ Stripe
    ~~~~~~~~~~~~~~
    Given an array of integers, find the first missing positive integer in linear time and constant
    space. In other words, find the lowest positive integer that does not exist in the array.
    The array can contain duplicates and negative numbers as well.

    For example, the input ```[3, 4, -1, 1]``` should give ```2```.
    The input ```[1, 2, 0]``` should give ```3```.

    __
    You can modify the input array in-place.

"""


def find_first_positive_missing(nums: list):
    """
    1. Get maximum
    2. Create lookup table
    3. Iterate from 0 to max
    4. If i is not in lookup table, return i
    5. Else return maximum + 1

    :param nums: pool of numbers
    :return: the first positive integer missing
    """

    if not nums:
        return 1

    maximum = max(nums)

    lookup = {}
    for num in nums:
        lookup[num] = True

    # todo: Not sure if this complies with constant space since range creates a list of values
    for i in range(1, maximum):
        if not lookup.get(i):
            return i

    return maximum + 1


if __name__ == "__main__":
    assert find_first_positive_missing([3, 4, -1, 1]) == 2
    assert find_first_positive_missing([-2, -1, 10]) == 1
    assert find_first_positive_missing([1, 2, 0]) == 3
    assert find_first_positive_missing([1, 2, 0, 4, 3, -1]) == 5
