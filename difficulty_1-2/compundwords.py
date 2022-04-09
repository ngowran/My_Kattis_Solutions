# Kattis level: - 1.7
# Link: https://open.kattis.com/problems/compoundwords

#!usr/bin/env python3

import sys

def make_dic(words):
    dic = {}
    for word in words:
        dic[word] = "True"
    return dic


def compoundwords(words):
    newwords = []
    for i in range(0, len(words)):
        for j in range(0, len(words)):
            if words[i] != words[j]:
                new = words[i] + words[j]
                if new not in newwords:
                    newwords.append(new)
    return newwords


def main():
    words = []
    for lines in sys.stdin:
        for word in lines.strip().split():
            words.append(word)
    compund = compoundwords(words)
    word_dic = make_dic(compund)
    for k in sorted(word_dic.keys()):
        print(k)


if __name__ == "__main__":
    main()