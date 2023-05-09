#!/usr/bin/python3
for a in range(97, 123):
    if a == ord('e'):
        continue
    elif a == ord('q'):
        continue
    else:
        print("{}".format(chr(a)), end="")
