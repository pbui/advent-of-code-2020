#!/usr/bin/env python3

import collections
import sys

# Constants

PRECEDENCE = {
    '+' : 1,
    '*' : 1,
}

# Structures

Node = collections.namedtuple('Node', 'op lhs rhs')

# Functions

def parse_primary(tokens):
    if tokens[0] == '(':
        tokens.pop(0)
        primary = parse_expression(tokens)
        tokens.pop(0)
    else:
        primary = tokens.pop(0)

    return primary

def parse_expression(tokens, precedence=0):
    lhs = parse_primary(tokens)

    while tokens and PRECEDENCE.get(tokens[0], -1) >= precedence:
        op  = tokens.pop(0)
        rhs = parse_expression(tokens, PRECEDENCE[op] + 1)
        lhs = Node(op, lhs, rhs)

    return lhs

def evaluate(expression):
    if isinstance(expression, str):
        return int(expression)

    if expression.op == '+':
        return evaluate(expression.lhs) + evaluate(expression.rhs)
    else:
        return evaluate(expression.lhs) * evaluate(expression.rhs)

# Main Execution

def main():
    total = 0
    for line in sys.stdin:
        tokens     = [token for token in line if not token.isspace()]
        expression = parse_expression(tokens)
        evaluation = evaluate(expression)
        total     += evaluation

    print(total)

if __name__ == '__main__':
    main()
