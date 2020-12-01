#!/usr/bin/env python3

import sys

# Functions

''' Brute-force: O(n^2)
def find_pair(numbers, target=2020):
    for number_0 in numbers:
        for number_1 in numbers:
            if number_0 + number_1 == 2020:
                return (number_0, number_1)
    return []
'''

def find_pair(numbers, target=2020):
    differences = set()
    for number in numbers:
        if number in differences:
            return [number, target - number]
        differences.add(target - number)
    return []

# Main Execution

def main():
    numbers = [int(l) for l in sys.stdin]
    pair    = find_pair(numbers)
    print(pair[0] * pair[1])

if __name__ == '__main__':
    main()
