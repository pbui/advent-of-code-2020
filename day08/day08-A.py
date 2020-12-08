#!/usr/bin/env python

import sys

# Class

class Console:
    def __init__(self):
        self.accumulator = 0
        self.code        = []
        self.counter     = 0
        self.operations  = {
            'nop': self.do_nop,
            'acc': self.do_acc,
            'jmp': self.do_jmp,
        }

    def load(self, stream=sys.stdin):
        for line in sys.stdin:
            operation, argument = line.strip().split()
            self.code.append((
                operation, int(argument)
            ))

    def do_nop(self, argument):
        self.counter += 1
    
    def do_acc(self, argument):
        self.accumulator += argument
        self.counter     += 1

    def do_jmp(self, argument):
        self.counter += argument

    def run(self):
        history = set()
        while self.counter not in history and self.counter < len(self.code):
            history.add(self.counter)
            operation, argument = self.code[self.counter]
            self.operations[operation](argument)

# Main Execution

def main():
    console = Console()
    console.load()
    console.run()

    print(console.accumulator)

if __name__ == '__main__':
    main()
