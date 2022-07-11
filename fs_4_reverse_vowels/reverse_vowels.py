def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """

    vowels = 'aeiouAEIOU'
    arr_s = [char for char in s]
    front_idx = 0
    back_idx = len(arr_s)-1
    output = ""

    while front_idx < back_idx:

        while arr_s[front_idx] not in vowels:
            # print('front while loop firing', front_idx, arr_s[front_idx])
            front_idx += 1
        # print('front loop found vowel @', front_idx,
            #   "vowel was", arr_s[front_idx])
            if front_idx == len(arr_s):
                return

        frontswap = arr_s[front_idx]

        while arr_s[back_idx] not in vowels:
            # print('back while loop firing', back_idx, arr_s[back_idx])
            back_idx -= 1
        # print('back loop found vowel @', back_idx,
            #   "vowel was", arr_s[back_idx])

        arr_s[front_idx], arr_s[back_idx] = arr_s[back_idx], arr_s[front_idx]
        front_idx += 2
        back_idx -= 2

        output = (''.join(arr_s))
    return output


print(
    reverse_vowels("Hello!"),

    reverse_vowels("Tomatoes"),

    reverse_vowels("Reverse Vowels In A String"),

    reverse_vowels("aeiou"),

    reverse_vowels("why try, shy fly?"),
)
