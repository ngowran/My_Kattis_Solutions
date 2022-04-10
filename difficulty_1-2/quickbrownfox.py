# Kattis level: 1.6
# Link: https://open.kattis.com/problems/quickbrownfox

#!usr/bin.env python3
import sys
from string import punctuation

alphbet = "abcdefghijklmnopqrstuvwxyz"

def is_pangram(line):
    missing = ""
    for char in alphbet:
            if char not in line:
                missing = missing + char
    if len(missing) > 0:
        return f"missing {missing}"
    else:
        return f"pangram"

def main():
    num = sys.stdin.readline().strip()
    for lines in sys.stdin:
        line = lines.strip(punctuation).lower().split()
        line = "".join(line)
        line = sorted(line)
        print(is_pangram(line))

        

if __name__ == "__main__":
    main()