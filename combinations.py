#!/usr/bin/python3
def combinations(k, elements):

    if k == 1:
        return [ [x] for x in elements ]

    data = []

    for x in elements:
        remaining = filter(lambda y : x != y, elements)
        combs = append_all(x, combinations(k - 1, remaining))
        for comb in combs:
            data += [comb]

    return data

def append_all(elem, lists):
    return [ [elem] + lst for lst in lists ]

print(combinations(3, [1,2,3,4]))