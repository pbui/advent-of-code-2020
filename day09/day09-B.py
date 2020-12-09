#!/usr/bin/env python3

import sys

# Constants

TARGET = 1492208709 # From Part A

# Functions

def find_contiguous_array(numbers, target):
    ''' Linear solution from @Nuolong '''
    start = 0
    end   = 1
    total = numbers[start]

    while end < len(numbers):
        if total == target:
            return numbers[start:end + 1]

        if total > target:
            total -= numbers[start]
            start += 1
        else:
            total += numbers[end]
            end   += 1

    '''
    for start in range(len(numbers)):
        for end in range(start, len(numbers)):
            if sum(numbers[start:end]) == target:
                return numbers[start:end]
    '''
    
    return []

# Main Execution

def main():
    numbers = [int(n) for n in sys.stdin]
    array   = find_contiguous_array(numbers, TARGET)

    print(min(array) + max(array))

if __name__ == '__main__':
    main()
