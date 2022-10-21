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