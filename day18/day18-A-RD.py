#!/usr/bin/env python3

import collections
import operator
import sys

# Structures

Node = collections.namedtuple('Node', 'value left right')

# Functions

def parse_token(stream):
    while stream and stream[0].isspace():
        stream.pop(0)

    token = ''
    if stream:
        if stream[0] in ('(', ')', '+', '*'):
            token = stream.pop(0)
        elif stream[0].isdigit():
            while stream and stream[0].isdigit():
                token += stream.pop(0)
            token = int(token)

    return token

def parse_expression(stream):
    left  = parse_token(stream)
    value = None
    right = None

    if isinstance(left, int):
        value = parse_token(stream)
        if not value or value == ')':
            return left
        right = parse_expression(stream)

    if left == '(':
        left  = parse_expression(stream)
        value = parse_token(stream)
        if not value or value == ')':
            return left
        right = parse_expression(stream)

    return Node(value, left, right)

def evaluate(expression):
    if isinstance(expression, int):
        return expression

    if expression.value == '+':
        return evaluate(expression.left) + evaluate(expression.right)
    else:
        return evaluate(expression.left) * evaluate(expression.right)

# Main Execution

def main():
    total = 0
    for line in sys.stdin:
        expression = parse_expression(list(line))
        print(expression)
        evaluation = evaluate(expression)
        print(evaluation)
        total     += evaluation

    print(total)

if __name__ == '__main__':
    main()
