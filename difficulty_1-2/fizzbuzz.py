# Kattis level:  1.4
# Link: https://open.kattis.com/problems/fizzbuzz
#!usr/bin/env python3

import sys

def main():
  x, y, n = sys.stdin.readline().strip().split()
  x = int(x)
  y = int(y)
  i = 1
  while i < int(n) + 1:
    if i % x == 0 and i % y == 0:
      print("fizzbuzz")
    elif i % x == 0:
      print("fizz")
    elif i % y == 0:
      print("buzz")
    else:
      print(i)
    i += 1


if __name__ == "__main__":
  main()
