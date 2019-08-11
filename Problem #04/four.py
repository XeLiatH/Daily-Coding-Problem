# -*- coding: utf8 -*-


def find_missing_number(numbers: list):
    if not numbers:
        return 1

    maximum = max(numbers)

    lookup = {}
    for num in numbers:
        lookup[num] = True

    numbers = None  # Unsetting the variable

    # Not sure if this complies with constant space since range creates a list of values
    for i in range(1, maximum):
        if not lookup.get(i):
            return i

    return maximum + 1


if __name__ == "__main__":
    print(2 == find_missing_number([3, 4, -1, 1]))
    print(1 == find_missing_number([-2, -1, 10]))
    print(3 == find_missing_number([1, 2, 0]))
    print(5 == find_missing_number([1, 2, 0, 4, 3, -1]))
