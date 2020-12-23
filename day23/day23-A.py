#!/usr/bin/env python3

import sys

# Classes

class Cup:
    def __init__(self, label, right=None):
        self.label = int(label)
        self.right = right


    def push(self, label):
        self.right = Cup(label, self.right if self.right else self)
        return self.right

    def pop(self):
        right      = self.right
        self.right = self.right.right
        return right.label

    def __str__(self):
        return f'{self.label}'

# Functions

def link_cups(labels):
    head    = Cup(labels.pop(0))
    current = head
    for label in labels:
        current = current.push(label)
    return head
   
def dump_cups(head):
    cups    = [f'({head})']
    current = head.right

    while current != head:
        cups.append(f'{current.label}')
        current = current.right

    return ' '.join(cups)

def find_cup(head, target):
    while head.label != target:
        head = head.right
    return head

def find_max(head):
    maximum = head.label
    current = head.right

    while current != head:
        if current.label > maximum:
            maximum = current.label
        current = current.right

    return maximum

def play_game(cups, moves=100):
    current = cups

    for move in range(1, moves + 1):
        print(f'\n-- move {move} --')
        print(f'cups:', dump_cups(current))

        # Pick up three cups immediately clockwise of current cup
        three_cups = [current.pop(), current.pop(), current.pop()]
        print(f'pick up:', ' '.join(map(str, three_cups)))
        
        # Select destination cup, where label is equal to current cup's label - 1
        destination_label = current.label - 1

        # Make sure destination isn't in one of three cups
        while destination_label in three_cups:
            destination_label -= 1

        # If destnation is below lowest value (1), then wrap to highest in remaining cups
        if destination_label == 0:
            destination_label = find_max(current)

        # Place cups after destination
        destination = find_cup(current, destination_label)
        
        print(f'destination: {destination}')

        for label in three_cups:
            destination = destination.push(label)
        
        # Advance to next cup
        current = current.right

    return current

def order_cups(cups):
    first = find_cup(cups, 1)
    return ''.join(dump_cups(first).split()[1:])

# Main Execution

def main():
    #cups = link_cups(list('389125467'))
    cups = link_cups(list('193467258'))
    cups = play_game(cups)

    print(order_cups(cups))

if __name__ == '__main__':
    main()
