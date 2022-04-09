# Kattis level: 1.7
# Link: https://open.kattis.com/problems/peragrams

#!usr/bin/env python3 

import sys

def peragram(word):
    letters_replace = 0
    if word == word[::-1]:
        return letters_replace
    i = 0
    while i < len(word):
        if word[:i] == word[::-1]:
            letters_replace = i
            return letters_replace
        i = i + 1


def main():
    word = sys.stdin.readline().strip()
    print(peragram(word))


if __name__ == "__main__":
    main()