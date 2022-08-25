#!/usr/bin/python3
def is_permutation(string_a, string_b):

    if len(string_a) != len(string_b):
        return False

    frequencies_a = char_frequencies(string_a)
    frequencies_b = char_frequencies(string_b)

    result = True

    for key in frequencies_a.keys():
        if frequencies_b.get(key) == None or frequencies_a[key] != frequencies_b[key]:
            result = False

    return result

def char_frequencies(string):

    frequencies = {}

    for c in string:
        if frequencies.get(c) == None:
            frequencies[c] = 1
        else:
            frequencies[c] += 1

    return frequencies


print(is_permutation("asd", "bbbfeef")) # false
print(is_permutation("casa", "pedo")) # false
print(is_permutation("asac23", "casa23")) # true
print(is_permutation("12jitu23", "31tjui22")) # true
print(is_permutation("asac23", "cazsa23")) # false