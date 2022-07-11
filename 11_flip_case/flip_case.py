def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    swap2 = to_swap.swapcase()
    output = [ltr.swapcase() if ltr.lower() == (to_swap.lower())
              else ltr for ltr in phrase]
    return ''.join(output)


print(flip_case('Where Has Every Decent Pelican Eaten?', 'e'))
