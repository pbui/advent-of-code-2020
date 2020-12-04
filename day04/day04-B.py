#!/usr/bin/env python3

import re
import sys

# Constants

PASSPORT_FIELDS = ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')

# Functions

def read_passport():
    passport = {}

    while line := sys.stdin.readline().strip():
        for pair in line.split():
            field, value = pair.split(':')
            passport[field] = value

    return passport

def validate_numeric_field(passport, field, minimum, maximum):
    '''
    >>> validate_numeric_field({'byr': '2002'}, 'byr', 1920, 2002)
    True
    
    >>> validate_numeric_field({'byr': '2003'}, 'byr', 1920, 2002)
    False
    '''

    if not re.match(r'^\d{4}$', passport[field]):
        return False

    return minimum <= int(passport[field]) <= maximum

def validate_height(passport):
    '''
    >>> validate_height({'hgt': '60in'})
    True

    >>> validate_height({'hgt': '190cm'})
    True
    
    >>> validate_height({'hgt': '190in'})
    False
    
    >>> validate_height({'hgt': '190'})
    False
    '''
    try:
        height, units = re.findall(r'^(\d+)(in|cm)$', passport['hgt'])[0]
    except (IndexError, ValueError):
        return False
        
    if units == 'cm':
        minimum, maximum = 150, 193
    else:
        minimum, maximum = 59, 76

    return minimum <= int(height) <= maximum

def validate_hair_color(passport):
    '''
    >>> validate_hair_color({'hcl': '#123abc'})
    True
    
    >>> validate_hair_color({'hcl': '#123abz'})
    False
    
    >>> validate_hair_color({'hcl': '123abc'})
    False
    '''
    return bool(re.match(r'^#[0-9a-f]{6}$', passport['hcl']))

def validate_eye_color(passport):
    '''
    >>> validate_eye_color({'ecl': 'brn'})
    True
    
    >>> validate_eye_color({'ecl': 'wat'})
    False
    '''
    return passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}

def validate_passport_id(passport):
    '''
    >>> validate_passport_id({'pid': '000000001'})
    True
    
    >>> validate_passport_id({'pid': '0123456789'})
    False
    '''
    return bool(re.match('^\d{9}$', passport['pid']))

# Main Execution

def main():
    valid = 0

    while passport := read_passport():
        if not all(field in passport for field in PASSPORT_FIELDS):
            continue

        valid += all([
            validate_numeric_field(passport, 'byr', 1920, 2002),
            validate_numeric_field(passport, 'iyr', 2010, 2020),
            validate_numeric_field(passport, 'eyr', 2020, 2030),
            validate_height(passport),
            validate_hair_color(passport),
            validate_eye_color(passport),
            validate_passport_id(passport),
        ])

    print(valid)

if __name__ == '__main__':
    main()
