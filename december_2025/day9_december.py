"""
Given an array of elements, return the element that appears most frequently.

    There will always be a single most frequent element.
"""

def most_frequent(arr):
    frequency = {}
    for i in arr:
        if i not in frequency:
            frequency[i] = 1
        else:
            frequency[i] += 1
    max_freq = 0
    for key, value in frequency.items():
        if value > max_freq:
            max_freq = value
            arr = key
    return arr