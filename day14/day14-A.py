#!/usr/bin/env python3

import re
import sys

# Constants

WORD_SIZE = 36
MASK_RE   = r'mask = (.*)'
MEMORY_RE = r'mem\[(\d+)\] = (\d+)'

# Functions

def mask_value(mask, value):
    return ''.join([
        v if m == 'X' else m for m, v in zip(mask, value)
    ])

def int_to_binary(i):
    return format(int(i), f'0{WORD_SIZE}b')

def process_instructions():
    memory = {}
    mask   = '0'*WORD_SIZE

    for line in sys.stdin:
        if line.startswith('mask'):
            mask = re.findall(MASK_RE, line)[0]
        else:
            address, value  = re.findall(MEMORY_RE, line)[0]
            memory[address] = mask_value(mask, int_to_binary(value))

    return memory

# Main Execution

def main():
    memory = process_instructions()
    total  = sum(int(v, 2) for v in memory.values())

    print(total)

if __name__ == '__main__':
    main()
