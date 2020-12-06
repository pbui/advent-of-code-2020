#!/usr/bin/env python3

import sys

# Functions

def parse_group():
    group = set()
    while line := sys.stdin.readline().strip():
        group |= set(line)
    return group

def parse_groups():
    while group := parse_group():
        yield group

# Main Execution

def main():
    counts = sum(len(g) for g in parse_groups())
    print(counts)

if __name__ == '__main__':
    main()
