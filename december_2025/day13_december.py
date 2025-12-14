"""Capitalize It

Given a string title, return a new string formatted in title case using the following rules:

    Capitalize the first letter of each word.
    Make all other letters in each word lowercase.
    Words are always separated by a single space.

"""

def title_case(title):
    title =  title.lower()

    words = title.split(" ")
    for i in range(len(words)):
        words[i] = words[i].capitalize()
    title = " ".join(words)
    return title