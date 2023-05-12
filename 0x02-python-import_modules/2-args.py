#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    args = len(argv) - 1
    print("{} {}".format(args, "argument" if (args == 1) else "arguments"))
    for i in range(1, (args + 1)):
        print("{}: {}".format(i, argv[i]))
