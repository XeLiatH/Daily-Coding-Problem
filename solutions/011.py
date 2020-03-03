# -*- coding: utf-8 -*-

"""
    > 011 @ Twitter
    ~~~~~~~~~~~~~~~
    Implement an autocomplete system. That is, given a query string s and a set
    of all possible query strings, return all strings in the set that have s as a prefix.
    
    For example, given the query string de and the set of strings [dog, deer, deal],
    return [deer, deal].
    
    __
    Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.


"""


def autocomplete(s: str, d: list):
    """
    :param s: query
    :param d: words
    :return:
    """

    return [word for word in d if word[:len(s)] == s]


if __name__ == '__main__':
    assert autocomplete('de', ['dog', 'deer', 'deal']) == ['dear', 'deal']
