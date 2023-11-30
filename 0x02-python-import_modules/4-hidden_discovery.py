#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
'''
index = dir(hidden_4)

for index, name in enumerate(index):
    if name[0] == '_':
        continue
    else:
        print("{}".format(name))
'''
for item in dir(hidden_4):
    if item[:2] == '__':
        print("{}".format(item))