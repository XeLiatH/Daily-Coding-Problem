# -*- coding: utf8 -*-


def find_missing_integer(integers: list):
    # I think this should be O(n) ?
    # remove duplicates
    integers = list(set(integers))
    # remove negative values and 0
    integers = [item for item in integers if item > 0]
    # sort the array
    integers.sort()

    # TODO: maybe could be done in simpler way?
    iter = 1
    for integer in integers:
        if iter != integer:
            break
        iter = iter + 1
    return iter


if __name__ == "__main__":
    print(2 == find_missing_integer([3, 4, -1, 1]))
    print(3 == find_missing_integer([1, 2, 0]))
