#!/usr/bin/env python3

import sys

# Functions

''' Brute-Force: O(n^3)
def find_triple(numbers, target=2020):
    for number_0 in numbers:
        for number_1 in numbers:
            for number_2 in numbers:
                if number_0 + number_1 + number_2 == 2020:
                    return (number_0, number_1, number_2)
    return []
'''

def find_pair(numbers, target=2020):
    differences = set()
    for number in numbers:
        if number in differences:
            return [number, target - number]
        differences.add(target - number)
    return []

def find_triple(numbers, target=2020):
    for number in numbers:
        pair = find_pair(numbers, target - number)
        if pair:
            return [number] + pair
    return []

# Main Execution

def main():
    numbers = [int(l) for l in sys.stdin]
    triple    = find_triple(numbers)
    print(triple[0] * triple[1] * triple[2])

if __name__ == '__main__':
    main()
