def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?

        >>> same_frequency(551122, 221515)
        True

        >>> same_frequency(321142, 3212215)
        False

        >>> same_frequency(1212, 2211)
        True
    """

    for d in str(num1):
        if str(num1).count(d) != str(num2).count(d):
            return False
    return True


# print(
#     same_frequency(551122, 221515),
#     same_frequency(321142, 3212215),
#     same_frequency(1212, 2211)
# )
