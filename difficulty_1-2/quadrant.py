# Kattis level: 1.3
# Link https://open.kattis.com/problems/quadrant

#!usr/bin/env python3

import sys

def what_q(x, y):
    if x < 0 and y > 0:
        return 2
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y < 0:
        return 3
    elif x > 0 and y > 0:
        return 1


def main():
    x = int(sys.stdin.readline().strip())
    y = int(sys.stdin.readline().strip())

    print(what_q(x, y))

if __name__=="__main__":
    main()