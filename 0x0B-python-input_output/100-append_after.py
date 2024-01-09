#!/usr/bin/python3
"""
Contains the function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """appends "new_string" after a line containing
    "search_string" in "filename" """
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        newlines = []
        for line in lines:
            if search_string in line:
                line = line.strip() + '\n'
                newlines.append(line)
                newlines.append(new_string + '\n')
            else:
                newlines.append(line.strip() + '\n')
    with open('READEME.txt', 'w', encoding='utf-8') as output:
        output.writelines(newlines)
