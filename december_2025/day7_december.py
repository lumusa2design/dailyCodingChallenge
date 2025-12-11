"""Given a string sentence, return a compressed version of the sentence where consecutive duplicate words are replaced by the word followed with the number of times it repeats in parentheses.

    Only consecutive duplicates are compressed.
    Words are separated by single spaces.

For example, given "yes yes yes please", return "yes(3) please"""
def compress_string(sentence):
    words = sentence.split(" ")
    compressed_words = {}
    for i in words:
        if i in compressed_words:
            compressed_words[i] += 1
        else:
            compressed_words[i] = 1
    return sentence