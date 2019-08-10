# -*- coding: utf8 -*-


def simple_approach(numbers: list):
    """
    The simplest solution I could come up with
    Complexity O(n^2)

    :param numbers: iterated array
    :return: array of products
    """

    length = len(numbers)
    array = [1] * length

    for i in range(length):
        for j in range(length):
            if i != j:
                array[i] *= numbers[j]
    return array


if __name__ == '__main__':
    print(simple_approach([1, 2, 3, 4, 5]))
    print(simple_approach([3, 2, 1]))
