#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1
    output = 0
    if count == 0:
        print("0")
    else:
        for i in range(1, count + 1):
            output += int(sys.argv[i])
        print("{}".format(output))
