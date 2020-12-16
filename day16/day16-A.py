#!/usr/bin/env python3

import itertools
import re
import sys

# Functions

def read_rules():
    rules = {}

    while line := sys.stdin.readline().strip():
        field, ranges = line.split(':', 1)
        rules[field]  = [
            (int(s), int(e)) for s, e in re.findall(r'(\d+)-(\d+)', ranges)
        ]

    return rules

def read_tickets():
    return [
        [int(f) for f in l.split(',')] for l in sys.stdin if ',' in l
    ]

def flatten(iterable):
    return list(itertools.chain.from_iterable(iterable))

def find_invalid_fields(rules, ticket):
    all_ranges = flatten(rules.values())

    for value in ticket:
        if not any(s <= value <= e for s, e in all_ranges):
            yield value

# Main Execution

def main():
    rules    = read_rules()
    tickets  = read_tickets()
    nearby   = tickets[1:]
    invalids = flatten(
        find_invalid_fields(rules, ticket) for ticket in nearby
    )

    print(sum(invalids))

if __name__ == '__main__':
    main()
