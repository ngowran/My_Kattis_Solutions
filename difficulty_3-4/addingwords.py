#!usr/bin/env python3

# Kattis level: 3.7
# Link: https://open.kattis.com/problems/addingwords

import sys

calc_dict = {}

def defin(word, number):
    calc_dict[word] = int(number)


def calc(to_cal):
    try:
        number = calc_dict[to_cal[0]]
        i = 0
        while i < len(to_cal):
            if to_cal[i] == "+":
                number = number + calc_dict[to_cal[i + 1]]
            elif to_cal[i] == "-":
                number = number - calc_dict[to_cal[i + 1]]
            i = i + 1
    except KeyError:
        return " ".join(to_cal) + " unknown"
    if number in calc_dict.values():
        for k, v in calc_dict.items():
            if v == number:
                return " ".join(to_cal) + " " + k
    else:
      return " ".join(to_cal) + " unknown"


def main():
    for lines in sys.stdin:
        input_line = lines.strip().split()
        i = 0
        while i < len(input_line):
            if input_line[0] == "def":
                defin(input_line[1], input_line[2])
            elif input_line[0] == "calc":
                print(calc(input_line[1:]))
                break
            elif input_line[0] == "clear":
                calc_dict.clear()
            i = i + 1


if __name__ == "__main__":
    main()
