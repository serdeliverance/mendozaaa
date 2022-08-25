#!/usr/bin/python3
def is_unique(string):
    if len(string) < 2:
        return True

    string_sorted = sorted(string)

    i = 1

    while i < len(string_sorted):
        prev = string_sorted[i - 1]
        curr = string_sorted[i]

        if prev == curr:
            break
        
        i += 1
    
    return False if i < len(string_sorted) else True

print(is_unique("abc"))
print(is_unique("b"))
print(is_unique("acabff"))
print(is_unique("ajeuu"))