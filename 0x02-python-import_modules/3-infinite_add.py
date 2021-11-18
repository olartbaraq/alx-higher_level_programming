#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num = len(sys.argv)
    if num == 1:
        print("{}".format(num - 1))
    elif num > 1:
        result = 0
        for i in range(1, num):
            result += int(sys.argv[i])
        print("{}".format(result))
