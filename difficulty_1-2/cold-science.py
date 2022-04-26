# Kattis level: 1.3
# Link: https://open.kattis.com/problems/cold
#!usr/bin/env python3
import sys

def main():
    discard = sys.stdin.readline()
    temps = sys.stdin.readline().strip().split()
    minus = [int(t) for t in temps if int(t) < 0]
    print(len(minus))


if __name__ == "__main__":
    main()