# -*- coding: utf-8 -*-

"""
    > 005.solution
    ~~~~~~~~~~~~~~

"""


def cons(a, b):
    def pair(f):
        return f(a, b)

    return pair


def car(f):
    def left(a, b):
        return a

    return f(left)


def cdr(f):
    def right(a, b):
        return b

    return f(right)


if __name__ == "__main__":
    print(car(cons(3, 4)))  # 3
    print(cdr(cons(3, 4)))  # 4
