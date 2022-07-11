def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """

    output = ()
    max_idx = 1
    for a in nums:
        for b in nums:
            while nums.index(a) <= max_idx & nums.index(b) <= max_idx:
                if a+b == goal:
                    output = (a, b)
            max_idx += 1


# print(
#     sum_pairs([1, 2, 2, 10], 4),
# )

print('wharggar')

# something has broken. When I run this, my fans go out of control and no other python script will run. Did I make some kind of memory leak?
