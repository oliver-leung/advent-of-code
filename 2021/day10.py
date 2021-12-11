from os.path import join, dirname
from typing import List
import sys
from statistics import median


def parse(filename: str) -> List:
    with open(join(dirname(__file__), filename)) as f:
        data = [line.strip() for line in f.readlines()]

    return data

def illegal_char(chunk):
    stack = []
    for char in chunk:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            last = stack.pop()
            if last + char not in ['()', '[]', '{}', '<>']:
                return char

def part1(data):
    score = 0

    for chunk in data:
        illegal = illegal_char(chunk)
        if illegal == ')':
            score += 3
        elif illegal == ']':
            score += 57
        elif illegal == '}':
            score += 1197
        elif illegal == '>':
            score += 25137

    return score

def complete(chunk):
    stack = []
    for char in chunk:
        if char in ['(', '[', '{', '<']:
            stack.append(char)
        else:
            last = stack.pop()
            if last + char not in ['()', '[]', '{}', '<>']:
                raise Exception

    return stack

def compl_score(chars):
    score = 0
    for char in chars:
        score *= 5
        if char == '(':
            score += 1
        elif char == '[':
            score += 2
        elif char == '{':
            score += 3
        elif char == '<':
            score += 4
    return score


def part2(data):
    data = [chunk for chunk in data if illegal_char(chunk) is None]

    scores = []
    for chunk in data:
        chars = complete(chunk)
        scores.append(compl_score(reversed(chars)))

    return median(scores)

if __name__ == '__main__':
    input = sys.argv[1]
    data = parse(input)
    print(part1(data))
    print(part2(data))
