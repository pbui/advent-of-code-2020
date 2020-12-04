#!/usr/bin/env python3

import sys

# Constants

PASSPORT_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid')

# Functions

def read_passport():
    passport = {}

    while line := sys.stdin.readline().strip():
        for pair in line.split():
            field, value = pair.split(':')
            passport[field] = value

    return passport

# Main Execution

def main():
    valid = 0

    while passport := read_passport():
        valid += all(field in passport for field in PASSPORT_FIELDS[:-1])

    print(valid)

if __name__ == '__main__':
    main()
