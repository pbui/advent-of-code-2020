#!/usr/bin/env python3

import re
import sys

# Constants

CONTAIN_RE = r'^(.*) bags contain\s(.*)$'
TARGETS_RE = r'(\d+) ([a-z]+ [a-z]+) bags*[,.]' 

# Functions

def parse_rules():
    rules = {}

    for line in sys.stdin:
        source, targets = re.findall(CONTAIN_RE, line.strip())[0]
        rules[source]   = {}
        for count, target in re.findall(TARGETS_RE, targets):
            rules[source][target] = int(count)

    return rules

def count_bags(rules, source):
    return sum(
        number * (count_bags(rules, bag) + 1) for bag, number in rules[source].items()
    )

# Main Execution

def main():
    rules = parse_rules()
    bags  = count_bags(rules, 'shiny gold')

    print(bags)

if __name__ == '__main__':
    main()
