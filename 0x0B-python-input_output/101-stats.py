#!/usr/bin/python3
"""
reads stdin line by line and computes metrics
"""
import sys

status_codes = {'200': 0, '301': 0, '400': 0, '401': 0,
                '403': 0, '404': 0, '405': 0, '500': 0}
file_size = 0
splitted_line = []
count = 0
try:
    for line in sys.stdin:
        count += 1
        splitted_line = line.strip().split(' ')
        if len(splitted_line) >= 2:
            a = count

            if splitted_line[-2] in status_codes:
                status_codes[splitted_line[-2]] += 1
                count += 1
            try:
                file_size += int(splitted_line[-1])
                if a == count:
                    count += 1
            except Exception:
                if a == count:
                    continue

            if count == 10:
                print("File size: {:d}".format(file_size))
                for key, value in sorted(status_codes.items()):
                    if value:
                        print("{:s}: {:d}".format(key, status_codes[key]))
                count = 0

        print("File size: {:d}".format(file_size))
        for key, value in sorted(status_codes.items()):
            if value:
                print("{:s}: {:d}".format(key, status_codes[key]))
except Exception:
    print("File size: {:d}".format(file_size))
    for key, value in sorted(status_codes.items()):
        if value:
            print("{:s}: {:d}".format(key, status_codes[key]))

"""['242.182.96.142', '-', '[2024-01-09', '17:33:51.002132]',
'"GET', '/projects/260', 'HTTP/1.1"', '401', '58']"""
