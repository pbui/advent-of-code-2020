#!/usr/bin/env python3

import re
import sys

# Constants

CONTAIN_RE = r'^(.*) bags contain\s(.*)$'
TARGETS_RE = r'(\d+) ([a-z]+ [a-z]+) bags*[,.]' 
TARGET     = 'shiny gold'

# Functions

def parse_rule():
    try:
        source, targets = re.findall(CONTAIN_RE, sys.stdin.readline().strip())[0]
    except IndexError:
        return None

    rule = {source: {}}
    for count, target in re.findall(TARGETS_RE, targets):
        rule[source][target] = int(count)

    return rule

def parse_rules():
    rules = {}
    while rule := parse_rule():
        rules |= rule
    return rules

def contains_target(rules, source, target):
    frontier = [source]
    visited  = set()

    while frontier:
        color = frontier.pop()
        if color in visited:
            continue

        if color == target:
            return True

        visited.add(color)

        for neighbor, amount in rules[color].items():
            frontier.append(neighbor)

    return False

# Main Execution

def main():
    rules = parse_rules()
    count = 0

    for source in rules:
        if source == TARGET:
            continue

        count += int(contains_target(rules, source, TARGET))

    print(count)

if __name__ == '__main__':
    main()
