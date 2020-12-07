#!/usr/bin/env python3

import re
import sys

# Constants

CONTAIN_RE = r'^(.*) bags contain\s(.*)$'
TARGETS_RE = r'(\d+) ([a-z]+ [a-z]+) bags*[,.]' 
SOURCE     = 'shiny gold'

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

def count_bags(rules, source):
    return sum(
        number * (count_bags(rules, bag) + 1) for bag, number in rules[source].items()
    )

# Main Execution

def main():
    rules = parse_rules()
    bags  = count_bags(rules, SOURCE)

    print(bags)

if __name__ == '__main__':
    main()
