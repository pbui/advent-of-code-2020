#!/usr/bin/env python3

import collections
import sys

# Functions

def parse_group():
    group  = collections.defaultdict(int)
    people = 0

    while line := sys.stdin.readline().strip():
        for question in line:
            group[question] += 1
        people += 1

    return people, group

def parse_groups():
    while (pair := parse_group()) and pair[0] > 0:
        yield pair

# Main Execution

def main():
    counts = sum(len([1 for v in g.values() if v == p]) for p, g in parse_groups())
    print(counts)

if __name__ == '__main__':
    main()
