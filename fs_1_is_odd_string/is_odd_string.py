def is_odd_string(word):
    """Is the sum of the character-positions odd?

    Word is a simple word of uppercase/lowercase letters without punctuation.

    For each character, find it's "character position" ("a"=1, "b"=2, etc).
    Return True/False, depending on whether sum of those numbers is odd.

    For example, these sum to 1, which is odd:

        >>> is_odd_string('a')
        True

        >>> is_odd_string('A')
        True

    These sum to 4, which is not odd:

        >>> is_odd_string('aaaa')
        False

        >>> is_odd_string('AAaa')
        False

    Longer example:

        >>> is_odd_string('amazing')
        True
    """

    # Hint: you may find the ord() function useful here
    offset = 96
    sum = 0
    for char in word:
        sum += ord(char)-offset
    if sum % 2 == 0:
        return False
    return True


# print(
#     is_odd_string('a'),
#     is_odd_string('A'),
#     is_odd_string('aaaa'),
#     is_odd_string('AAaa'),
#     is_odd_string('amazing')
# )
