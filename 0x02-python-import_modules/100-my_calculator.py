#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, div, mul, sub

length = len(sys.argv) - 1

# checks the number of arguments
if length != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])

match sys.argv[2]:
    case '+':
        print("{} {} {} = {}".format(a, sys.argv[2], b, add(a, b)))
    case '-':
        print("{} {} = {}".format(a, sys.argv[2],  b, sub(a, b)))
    case "*":
        print("{} {} {} = {}".format(a, sys.argv[2],  b, mul(a, b)))
    case '/':
        print("{} {} {} = {}".format(a, sys.argv[2],  b, div(a, b)))
    case _:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
