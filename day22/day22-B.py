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
    configurations = set()

    while hand1 and hand2:
        # 1. Check configuration
        configuration = (tuple(hand1), tuple(hand2))
        if configuration in configurations:
            return 1

        configurations.add(configuration)

        # 2. Draw top card from decks
        card1 = hand1.pop(0)
        card2 = hand2.pop(0)

        # 3. Both players have at least as many cards remaining in deck as
        # value of the card they drew
        if len(hand1) >= card1 and len(hand2) >= card2:
            winner = play_game(hand1[:card1], hand2[:card2])
        else:
            winner = 1 if card1 > card2 else 2

        # 4. Winner of round takes both cards
        if winner == 1:
            hand1.append(card1)
            hand1.append(card2)
        else:
            hand2.append(card2)
            hand2.append(card1)

    return 1 if hand1 else 2

def compute_score(winner):
    return sum(card * index for index, card in enumerate(winner[::-1], 1))

# Main Execution

def main():
    hand1  = read_hand()
    hand2  = read_hand()
    winner = hand1 if play_game(hand1, hand2) == 1 else hand2
    score  = compute_score(winner)

    print(score)

if __name__ == '__main__':
    main()
