#!/usr/bin/env python3

import sys

# Constants

TARGET = 1492208709 # From Part A

# Functions

def find_contiguous_array(numbers, target):
    for start in range(len(numbers)):
        for end in range(start, len(numbers)):
            if sum(numbers[start:end]) == TARGET:
                return numbers[start:end]
    return []

# Main Execution

def main():
    numbers = [int(n) for n in sys.stdin]
    array   = find_contiguous_array(numbers, TARGET)

    print(min(array) + max(array))

if __name__ == '__main__':
    main()
