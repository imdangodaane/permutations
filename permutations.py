#!/usr/bin/env python3


def permutations(elems):
    if len(elems) <= 1:
        return [elems]
    else:
        lst = []
        for i in range(len(elems)):
            main = elems[i]
            remainElems = elems[:i] + elems[i+1:]
            for p in permutations(remainElems):
                lst.append([main] + p)
        return lst


print(permutations([1, 2, 3, 4]))
