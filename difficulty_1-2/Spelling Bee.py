# Kattis level: 1.9
# Link: https://open.kattis.com/problems/spellingbee

#!usr/bin/env python3

import sys

def is_true(word, hex_word):
    for char in word:
        if char not in hex_word:
            return False
    return True

def main():
    hex_word = sys.stdin.readline().strip()
    center_letter = hex_word[0]
    num_words = sys.stdin.readline()
    words = [w.strip() for w in sys.stdin if len(w.strip()) >= 4]
    correct_words = [w for w in words if center_letter in w]

    final_words = []
    for word in correct_words:
        if is_true(word, hex_word) == True:
            final_words.append(word)

    print("\n".join(final_words))


if __name__ == "__main__":
    main()