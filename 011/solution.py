# -*- coding: utf-8 -*-

"""
    > 011.solution
    ~~~~~~~~~~~~~~

"""


def solve(s: str, d: list):
    return [word for word in d if word[:len(s)] == s]


if __name__ == '__main__':
    print(solve('de', ['dog', 'deer', 'deal']))
