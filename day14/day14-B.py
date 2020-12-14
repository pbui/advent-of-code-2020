#!/usr/bin/env python3

import itertools
import re
import sys

# Constants

WORD_SIZE = 36
MASK_RE   = r'mask = (.*)'
MEMORY_RE = r'mem\[(\d+)\] = (\d+)'

# Functions

def mask_address(mask, address):
    return ''.join([
        a if m == '0' else m for m, a in zip(mask, address)
    ])

def int_to_binary(i):
    return format(int(i), f'0{WORD_SIZE}b')

def expand_addresses(address):
    floats = address.count('X')

    for product in map(list, itertools.product('01', repeat=floats)):
        new_address = address[:]
        while 'X' in new_address:
            new_address = new_address.replace('X', product.pop(), 1)
        yield int(new_address, 2)

def process_instructions():
    memory = {}
    mask   = '0'*WORD_SIZE

    for line in sys.stdin:
        if line.startswith('mask'):
            mask = re.findall(MASK_RE, line)[0]
            continue


        address, value = re.findall(MEMORY_RE, line)[0]
        address_masked = mask_address(mask, int_to_binary(address))
        
        for address in expand_addresses(address_masked):
            memory[address] = value

    return memory

# Main Execution

def main():
    memory = process_instructions()
    total  = sum(int(v) for v in memory.values())

    print(total)

if __name__ == '__main__':
    main()
