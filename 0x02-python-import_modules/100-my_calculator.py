#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    num = len(sys.argv)
    op = ["+", "-", "*", "/"]
    if num != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        c = int(sys.argv[3])
        if sys.argv[2] == "+":
            print("{} {} {} = {}".format(a, op, b, add(a, b)))
        elif sys.argv[2] == "-":
            print("{} {} {} = {}".format(a, op, b, sub(a, b)))
        elif sys.argv[2] == "*":
            print("{} {} {} = {}".format(a, op, b, mul(a, b)))
        elif sys.argv[2] == "/":
            print("{} {} {} = {}".format(a, op, b, div(a, b)))
        elif sys.argv[2] != op:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
