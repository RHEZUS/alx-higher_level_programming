#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    rom_n = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
