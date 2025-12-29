"""

Given an array of integers and a target number, find all pairs of elements in the array whose values add up to the target and return the sum of their indices.

For example, given [2, 3, 4, 6, 8] and 10, you will find two valid pairs:

    2 and 8 (2 + 8 = 10), whose indices are 0 and 4
    4 and 6 (4 + 6 = 10), whose indices are 2 and 3

Add all the indices together to get a return value of 9.
"""
def pairwise (arr, target):
    index_sum = 0
    used_indices = set()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target and i not in used_indices and j not in used_indices:
                index_sum += i + j
                used_indices.add(i)
                used_indices.add(j)

    return index_sum