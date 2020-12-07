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

def contains(rules, source, target, first=False):
    if source == target:
        return not first

    return any(contains(rules, neighbor, target) for neighbor in rules[source])

# Main Execution

def main():
    rules = parse_rules()
    count = sum(1 for source in rules if contains(rules, source, TARGET, True))

    print(count)

if __name__ == '__main__':
    main()
