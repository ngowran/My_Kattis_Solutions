# Kattis level: 1.7
# Link: https://open.kattis.com/problems/peragrams

#!usr/bin/env python3 

import sys

def peragram(word):
    count = 0
    word_dic = {}
    for char in word:
        if char not in word_dic:
            word_dic[char] = 1
        else:
            word_dic[char] += 1
    for k, v in word_dic.items():
        if v % 2 != 0:
            count += 1
    if count != 0:
        count = count - 1
    return count 


def main():
    word = sys.stdin.readline().strip()
    print(peragram(word))


if __name__ == "__main__":
    main()