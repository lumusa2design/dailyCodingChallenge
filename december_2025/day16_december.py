""""Consonant Count

Given a string and a target number, determine whether the string contains exactly the target number of consonants.

    Consonants are all alphabetic characters except "a", "e", "i", "o", and "u" in any case.
    Ignore digits, punctuation, spaces, and other non-letter characters when counting.

"""

def has_consonant_count(text, target):
    consonants = set("bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ")
    count = sum(1 for char in text if char in consonants)
    return count == target