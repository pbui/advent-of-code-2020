#!/usr/bin/env python3

# Constants

SUBJECT_NUMBER = 7

# Functions

def transform(subject_number, loop_size):
    value = 1

    for _ in range(loop_size):
        value *= subject_number
        value %= 20201227

    return value

def find_loop_size(target):
    value     = 1
    loop_size = 0

    while value != target:
        value     *= SUBJECT_NUMBER
        value     %= 20201227
        loop_size += 1

    return loop_size

# Main Execution

def main():
    #card_public_key = 5764801
    #door_public_key = 17807724
    card_public_key = 10705932
    door_public_key = 12301431

    card_loop_size  = find_loop_size(card_public_key)
    door_loop_size  = find_loop_size(door_public_key)


    print(card_loop_size)
    print(door_loop_size)
    
    encryption_key  = transform(card_public_key, door_loop_size)

    print(encryption_key)

if __name__ == '__main__':
    main()
