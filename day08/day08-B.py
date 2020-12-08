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

    def run(self, reset=False):
        ''' Execute the Console's code one instruction at a time based on the
        value of the internal program counter.  

        Terminate when we encounter a repeat instruction (tracked by history
        set) or if the program counter goes beyond the last instruction code.
        '''
        if reset:
            self.accumulator = 0
            self.counter     = 0

        history = set()
        while self.counter not in history and self.counter < len(self.code):
            history.add(self.counter)
            operation, argument = self.code[self.counter]
            self.operations[operation](argument)

        return self.counter >= len(self.code)

# Main Execution

def main():
    console = Console()
    console.load()

    # To determine which instruction needs to be fixed, simply brute-force
    # search by swapping each jmp or nop code one at a time, executing the
    # console, and checking if it terminates.
    original_code = console.code[:]
    for instruction, (operation, argument) in enumerate(original_code):
        if operation == 'nop':
            continue

        # Swap jmp and nop operations.
        new_operation             = 'jmp' if operation == 'nop' else 'nop'
        console.code[instruction] = (new_operation, argument)

        # Check if console terminates; end search when it does.
        if console.run(reset=True):
            break

        # Restore instruction to previous operation.
        console.code[instruction] = (operation, argument)
            
    print(console.accumulator)

if __name__ == '__main__':
    main()
