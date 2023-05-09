#!/usr/bin/python3
for a in range(97, 123):
    if a != ord('e') or a != ord('q'):
        print("{}".format(chr(a)), end="")
    else:
        continue
