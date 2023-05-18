#!/usr/bin/python3
roman_digits = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500,
                'M': 1000, '0': 0}


def roman_to_int(roman_string):
    if not isinstance(roman_string, str):
        return 0
    roman_string += '0'
    x = 0
    result = 0
    while x < len(roman_string) - 1:
        current = roman_digits[roman_string[x]]
        next = roman_digits[roman_string[x + 1]]
        if current == next:
            result += next + current
            x += 1
        elif current < next:
            result += next - current
            x += 1
        else:
            result += current
        x += 1
    return result
