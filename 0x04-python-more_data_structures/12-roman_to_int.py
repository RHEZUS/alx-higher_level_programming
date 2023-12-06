#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    result = 0

    for i, c in enumerate(roman_string):
        if i+1 == len(roman_string) or rom_n[c] >= rom_n[roman_string[i+1]]:
            result += rom_n[c]
        else:
            result -= rom_n[c]
    return result
