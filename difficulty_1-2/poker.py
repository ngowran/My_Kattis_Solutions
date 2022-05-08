# Kattis level: 1.4
# Link: https://open.kattis.com/problems/pokerhand

#!usr/bin/env python3

import sys

rank = "A23456789TJQK"

rank_dic = {}

def k_value(hand):
    suits = hand.split()
    for card in suits:
        if card[0] not in rank_dic:
            rank_dic[card[0]] = 0
        if card[0] in rank:
            rank_dic[card[0]] += 1


def main():
    hand = sys.stdin.readline().strip()
    k_value(hand)
    print(max(rank_dic.values()))

if __name__ == "__main__":
    main()