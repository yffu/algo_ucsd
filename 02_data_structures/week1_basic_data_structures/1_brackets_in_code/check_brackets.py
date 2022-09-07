# python3

from collections import namedtuple
import os

debug = False
directory = 'tests'

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    if debug: print('left: ' + left + ' right: ' + right)
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    # 1 find first unmatched closing bracket
    # 2 find first unmatched opening bracket without the corresponding closing bracket
    # 3 if no mistakes, print no mistakes

    opening_brackets_stack = []
    for i, next in enumerate(text):
        if debug: print('i: ' + str(i) + ' next: ' + next)
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                # no more on opening bracket, return index of unmatched closing bracket
                return i + 1
            if not are_matching(opening_brackets_stack.pop().char, next):
                # no match on opening bracket, return index of closing bracket
                return i + 1
            else:
                # has match on opening bracket, pop opening bracket and continue
                continue
    # pre-condition: no more closing bracket
    if not opening_brackets_stack:
        # if no more opening bracket then Success
        return 'Success'
    else:
        # if remains opening bracket then return index of unmatched opening bracket
        return opening_brackets_stack.pop().position


def main():
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        if os.path.isfile(f) and '.a' not in f:
            text = open(f, 'r').read()
            a = open(f+'.a', 'r').read()
            if debug: print(text)
            mismatch = find_mismatch(text)
            # Printing answer, write your code here
            print('filename: ' + f)
            print('answer: ' + a)
            print('output: ' + str(mismatch))


if __name__ == "__main__":
    main()
