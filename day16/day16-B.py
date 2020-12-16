#!/usr/bin/env python3

import collections
import functools
import itertools
import operator
import re
import sys

# Functions

def read_rules():
    rules = {}

    while line := sys.stdin.readline().strip():
        field, ranges = line.split(':', 1)
        rules[field]  = [(int(start), int(end)) for start, end in re.findall(r'(\d+)-(\d+)', ranges)]

    return rules

def read_tickets():
    return [[int(field) for field in line.split(',')] for line in sys.stdin if ',' in line]

def flatten(iterable):
    return itertools.chain.from_iterable(iterable)

def is_ticket_valid(rules, ticket):
    return all(any(s <= v <= e for s, e in flatten(rules.values())) for v in ticket)

def find_matches(rules, tickets):
    matches = collections.defaultdict(list)

    for index in range(len(tickets[0])):
        for field, ranges in rules.items():
            found = True
            for ticket in tickets:
                if not any(s <= ticket[index] <= e for s, e in ranges):
                    found = False
                    break

            if found:
                matches[field].append(index)

    return matches

def find_fields(matches):
    fields = {}

    while matches:
        singles = [(field, indices[0]) for field, indices in matches.items() if len(indices) == 1]

        for field, index in singles:
            fields[index] = field
            for f in matches:
                matches[f].remove(index)
            del matches[field]

    return fields

# Main Execution

def main():
    rules    = read_rules()
    tickets  = read_tickets()
    valids   = [ticket for ticket in tickets if is_ticket_valid(rules, ticket)]

    matches  = find_matches(rules, valids)
    fields   = find_fields(matches)

    values   = [value for index, value in enumerate(tickets[0]) if fields[index].startswith('departure')]
    result   = functools.reduce(operator.mul, values, 1)

    print(result)

if __name__ == '__main__':
    main()
