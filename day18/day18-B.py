#!/usr/bin/env python3

import sys

# Constants

OPERATORS = ('+', '*')
PARENS    = ('(', ')')

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
    ''' Parse expression from infix to RPN '''
    queue = []
    stack = []

    while token := parse_token(stream):
        if isinstance(token, int):
            queue.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack[-1] not in PARENS:
                queue.append(stack.pop())
            stack.pop()
        elif token in OPERATORS:
            while stack and stack[-1] in OPERATORS and stack[-1] >= token:
                queue.append(stack.pop())
            stack.append(token)

    while stack and stack[-1] in OPERATORS:
        queue.append(stack.pop())

    return queue

def evaluate(expression):
    ''' Evaluate RPN expression '''
    stack = []

    while expression:
        token = expression.pop(0)
        if token in OPERATORS:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result   = operand1 + operand2 if token == '+' else operand1 * operand2
        else:
            result   = token
            
        stack.append(result)

    return stack[0]

# Main Execution

def main():
    total = 0
    for line in sys.stdin:
        expression = parse_expression(list(line))
        evaluation = evaluate(expression)
        total     += evaluation

    print(total)

if __name__ == '__main__':
    main()
