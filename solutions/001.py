# -*- coding: utf-8 -*-

"""

    > 001 @ Google
    ~~~~~~~~~~~~~~
    Given a list of numbers and a number k, return whether any two numbers 
    from the list add up to k. For example, given [10, 15, 3, 7] and k of 17, 
    return true since 10 + 7 is 17.

    __
    Bonus: Can you do this in one pass?

"""


def check_pair_sum(k: int, nums: list):
    """
    1. Go through all the numbers
    2. As you iterate, add complement to a set
    3. Two numbers add up to k if number is in complements

    Parameters:
    k (int): desired sum
    nums (list): available numbers

    Returns
    boolean: tru if there are 2 numbers in nums that add up to k

    """

    complements = set()
    for num in nums:
        if num in complements:
            return True
        complements.add(k - num)
    return False


if __name__ == '__main__':
    assert check_pair_sum(17, []) == False
    assert check_pair_sum(17, [10, 15, 3, 7]) == True
