#!/usr/bin/env python3

import re
import sys

# Constants

PASSWORD_RE = r'(\d+)-(\d+) ([a-z]+): ([a-z]+)'

# Main Execution

def main():
    valid = 0
    for line in sys.stdin:
        index_1, index_2, letter, password = re.findall(PASSWORD_RE, line.strip())[0]
        index_1 = int(index_1) - 1
        index_2 = int(index_2) - 1
        valid  += int((password[index_1] == letter) ^ (password[index_2] == letter))

    print(valid)

if __name__ == '__main__':
    main()
