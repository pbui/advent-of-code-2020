#!/usr/bin/env python3

import sys

# Functions

def read_hand(stream=sys.stdin):
    hand = []
    while card := stream.readline().strip():
        if card.isdigit():
            hand.append(int(card))
    return hand

def play_game(hand1, hand2):
    while hand1 and hand2:
        card1 = hand1.pop(0)
        card2 = hand2.pop(0)

        if card1 > card2:
            hand1.append(card1)
            hand1.append(card2)
        else:
            hand2.append(card2)
            hand2.append(card1)

    return hand1 if hand1 else hand2

def compute_score(winner):
    return sum(card * index for index, card in enumerate(winner[::-1], 1))

# Main Execution

def main():
    hand1  = read_hand()
    hand2  = read_hand()
    winner = play_game(hand1, hand2)
    score  = compute_score(winner)

    print(score)

if __name__ == '__main__':
    main()
