#!/usr/bin/env python3

import sys

# Functions

def read_rules():
    rules = {}

    while line := sys.stdin.readline().strip():
        number, states = line.split(':', 1)
        states         = [s.strip().replace('"', '').split() for s in states.split(' | ')]
        rules[number]  = states

    return rules

def match_rule(rules, message, curr_state='0', indent=0):
    # Base: Match terminal
    if rules[curr_state][0][0].isalpha():
        return message[1:] if rules[curr_state][0][0] == message[0] else None

    # Recursion: Match all next states
    for states in rules[curr_state]:    # Match any
        new_message = message[:]
        for next_state in states:       # Match all
            new_message = match_rule(rules, new_message, next_state, indent + 2)
            if new_message is None:
                break

        if new_message is not None:
            return new_message

    return None

# Main Execution

def main():
    rules = read_rules()
    count = 0

    while message := sys.stdin.readline().strip():
        if match_rule(rules, list(message)) == []:
            count += 1

    print(count)

if __name__ == '__main__':
    main()
