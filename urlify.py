#!/usr/bin/python3
import unittest

def urlify(str, true_length):

    arr = list(str)

    space_count = 0
    index = 0
    
    for i in range(true_length - 1):
        if arr[i] == ' ':
            space_count += 1
    
    index = true_length + space_count * 2 - 1

    for i in range(true_length - 1, 0, -1):
        if arr[i] == ' ':
            arr[index] = '0'
            arr[index - 1] = '2'
            arr[index - 2] = '%'
            index -= 3
        else:
            arr[index] = arr[i]
            index -= 1

    return ''.join(arr)

result = urlify("Mr 3ohn Smith    ", 13)

print(result)