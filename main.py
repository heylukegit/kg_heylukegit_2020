# -*- coding: utf-8 -*-
# @Time    : 3/14/20 17:29
# @Author  : Luke
# @Contact : mh3994@columbia.edu
# @File    : main.py
# @Software: PyCharm

import sys


def isOneToOneMappingExists(s1, s2):
    """
    return a boolean to indicate whether there is a
    one-to-one mapping from string1 to string2

    :param s1: string
    :param s2: string
    :return: bool
    """
    # init two sets
    set1 = set()
    set2 = set()

    # store all the chars in a set
    for c in s1:
        set1.add(c)

    for c in s2:
        set2.add(c)

    # use the length of set to check
    if len(set1) >= len(set2):
        return True
    else:
        return False

def test():
    print("Running some test files...")
    print(isOneToOneMappingExists("abc", "bcd"))
    print(isOneToOneMappingExists("foo", "bar"))
    print(isOneToOneMappingExists("bar", "foo"))
    print("-----------")
    print(isOneToOneMappingExists("", ""))
    print(isOneToOneMappingExists("a", "cc"))
    print(isOneToOneMappingExists("ab", "ccdd"))


if __name__ == "__main__":
    # test()

    # read the strings from sys.argv
    s1 = sys.argv[1]
    s2 = sys.argv[2]

    # call the function
    if isOneToOneMappingExists(s1, s2):
        print("true")
    else:
        print("false")






