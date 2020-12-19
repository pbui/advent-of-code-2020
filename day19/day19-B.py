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

def match_rule(rules, message, curr_state='0'):
    # Base: No message left
    if not message:
        return message

    # Base: Match terminal
    if rules[curr_state][0][0].isalpha():
        return message[1:] if rules[curr_state][0][0] == message[0] else message

    # Recursion: Match all next states
    for states in rules[curr_state]:    # Match any
        new_message = message[:]
        all_matched = True
        for next_state in states:       # Match all
            next_message = match_rule(rules, new_message, next_state)
            if next_message == new_message:
                all_matched = False
                break
            new_message = next_message

        if all_matched:
            return new_message

    return message

# Main Execution

def main():
    rules = read_rules()
    count = 0

    while message := sys.stdin.readline().strip():
        message   = list(message)
        match_42  = 0
        match_31  = 0

        # Consume 42's
        while (remaining := match_rule(rules, message, curr_state='42')) != message:
            message   = remaining
            match_42 += 1

        # Consume 31's
        while (remaining := match_rule(rules, message, curr_state='31')) != message:
            message   = remaining
            match_31 += 1

        # Must match at least two 42's, one 31, and the difference between 42
        # and 31 matches must be at least one.
        if not message and match_42 >= 2 and match_31 >= 1 and (match_42 - match_31) >= 1:
            count += 1

    print(count)

if __name__ == '__main__':
    main()
