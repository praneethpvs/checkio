#!/usr/bin/env python
"""
Input: Two arguments. A text as a string and words as a set of strings.
Output: The number of words in the text as an integer.

################### SOLUTION
Each word in the set is matched with the given text.
If the word is found in the string the values of the count variable is increased.
The process is repeated until all the words in the given set are matched and the count value is returns.
"""


def count_words(text, words):
    count = 0
    
    temp_text = str(text).lower()
    for string in words:
        if string in temp_text:
            count += 1
    return count


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}) == 3, "Example"
    assert count_words("Bananas, give me bananas!!!", {"banana", "bananas"}) == 2, "BANANAS!"
    assert count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",
                       {"sum", "hamlet", "infinity", "anything"}) == 1, "Weird text"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
