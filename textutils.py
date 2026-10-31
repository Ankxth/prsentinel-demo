"""Small text helpers."""


def word_count(text):
    """Number of words in text, split on any whitespace."""
    words = text.split()
    return len(words)


def initials(name):
    """Upper-case first letter of each part of a name: 'ada lovelace' -> 'AL'."""
    parts = name.split()
    result = ""
    for part in parts:
        result += part[0].upper()
    return result
