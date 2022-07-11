def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    # TL to BR
    x = 0
    y = 0
    sum = 0
    while x <= len(matrix)-1:
        sum += matrix[y][x]
        x += 1
        y += 1
    # TR to BL
    x = len(matrix)-1
    y = 0
    while y <= len(matrix)-1:
        sum += matrix[y][x]
        x -= 1
        y += 1
    return sum


m1 = [[1, 2], [30, 40], ]


m2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ]

# print(
#     sum_up_diagonals(m1),
#     sum_up_diagonals(m2)
# )

# I did this before looking at the official solution, which is much cleaner:
#  total = 0

#     for i in range(len(matrix)):
#         total += matrix[i][i]
#         total += matrix[i][-1 - i]

#     return total

# or, probably too tersely:
#
# return sum([matrix[i][i] + matrix[i][-1 - i] for i in range(len(matrix))])
