"""

Given an array of values, remove all occurrences of the most frequently occurring element and return the resulting array.

    If multiple values are tied for most frequent, remove all of them.
    Do not change any of the other elements or their order.

"""
def purge_most_frequent(arr):
    frequency = {}
    for value in arr:
        frequency[value] = frequency.get(value, 0) + 1

    max_freq = max(frequency.values())
    most_frequent_values = {key for key, freq in frequency.items() if freq == max_freq}

    return [value for value in arr if value not in most_frequent_values]