# Kattis level - 1.1-1.4
# Link - https://open.kattis.com/problems/heimavinna

#!usr/bin/env python3

import sys

def count_homework(homework):
    num_homework = 0
    for n in homework:
        if "-" in n:
            n = n.split("-")
            num_homework = num_homework + 1 + (int(n[-1]) - int(n[0]))
        else:
            num_homework = num_homework + 1
    return num_homework

def main():
  homework = sys.stdin.readline().strip().split(";")
  print(count_homework(homework))


if __name__ == "__main__":
    main()