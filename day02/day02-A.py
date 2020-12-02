#!/usr/bin/env python3

import collections
import re
import sys

# Constants

PASSWORD_RE = r'(\d+)-(\d+) ([a-z]+): ([a-z]+)'

# Main Execution

def main():
    valid = 0
    for line in sys.stdin:
        minimum, maximum, letter, password = re.findall(PASSWORD_RE, line.strip())[0]
        minimum = int(minimum)
        maximum = int(maximum)
        counts  = collections.Counter(password)
        valid  += int(minimum <= counts.get(letter, 0) <= maximum)

    print(valid)

if __name__ == '__main__':
    main()
