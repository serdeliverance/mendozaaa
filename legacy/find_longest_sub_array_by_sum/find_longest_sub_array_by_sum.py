def find_longest_sub_array_by_sum(arr, target):
    return find_longest_sub_array_by_sum_brute_force(arr, target)

"""
brute force solution
"""
def find_longest_sub_array_by_sum_brute_force(arr, target):
    longest_sub_array = []

    for i in range(0, len(arr)):
        sub = find_sub_array_starting_from(i, arr, target)

        if sub != [] and len(sub) > len(longest_sub_array):
            longest_sub_array = sub

    return longest_sub_array

def find_sub_array_starting_from(index, arr, target):
    sub_arr = []
    sum = 0

    for index in range(index, len(arr)):
        if sum + arr[index] > target:
            break

        sum += arr[index]
        sub_arr.append(arr[index])
    
    return sub_arr if sum == target else []

