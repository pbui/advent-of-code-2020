#!/usr/bin/env python3

import collections
import operator
import sys

# Constants

PRECEDENCE = {
    '+' : 2,
    '*' : 1,
}

# Structures

Node = collections.namedtuple('Node', 'op lhs rhs')

# Functions

def parse_expression(tokens, precedence=0):
    lhs = tokens.pop(0)

    if lhs == '(':
        lhs = parse_expression(tokens)
        tokens.pop(0)

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
