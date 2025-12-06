"""

Given a string, return the number of distinct permutations that can be formed from its characters.

    A permutation is any reordering of the characters in the string.
    Do not count duplicate permutations.
    If the string contains repeated characters, repeated arrangements should only be counted once.
    The string will contain only letters (A-Z, a-z).

For example, given "abb", return 3 because there's three unique ways to arrange the letters: "abb", "bab", and "bba".
"""

from math import factorial
from collections import Counter

def count_permutations(s):
    char_count = Counter(s)
    numerator = factorial(len(s))
    denominator = 1
    for count in char_count.values():
        denominator *= factorial(count)
    return numerator // denominator