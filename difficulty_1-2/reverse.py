# Kattis level: 1.2 - 1.5
# Link: https://open.kattis.com/problems/ofugsnuid

#!usr/bin/env python3
import sys

def main():
    n =  [int(n) for n in sys.stdin]
    need = n[1:]
    for num in need[::-1]:
        print(num)

if __name__ == "__main__":
    main()