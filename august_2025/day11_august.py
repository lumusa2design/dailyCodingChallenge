"""Vowel Balance

Given a string, determine whether the number of vowels in the first half of the string is equal to the number of vowels in the second half.

    The string can contain any characters.
    The letters a, e, i, o, and u, in either uppercase or lowercase, are considered vowels.
    If there's an odd number of characters in the string, ignore the center character.

"""

def is_balanced(s):
    vowels = ["A","E","I","O", "U"]
    s = s.upper()
    length = len(s)
    half = length // 2
    if length % 2 == 0:
        first_half = s[:half]
        second_half = s[half:]
    else:
        first_half = s[:half]
        second_half = s[half+1:]
    count_first = sum(1 for char in first_half if char in vowels)
    count_second = sum(1 for char in second_half if char in vowels) 
    return count_first == count_second
