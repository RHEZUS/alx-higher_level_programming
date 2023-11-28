#!/usr/bin/python3
flag = False
for i in range(122, 96, -1):
    if flag:
        print("{}".format(chr(i - 32)), end='')
        flag = False
    else:
        print("{}".format(chr(i)), end='')
        flag = True
