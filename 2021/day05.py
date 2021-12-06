from os.path import join, dirname
from typing import List
import re
from collections import defaultdict


def parse(filename: str) -> List:
    with open(join(dirname(__file__), filename)) as f:
        data = [line.strip() for line in f.readlines()]

    output = []
    for line in data:
        coords = re.split(r',| -> ', line)
        coords = [int(x) for x in coords]
        output.append(coords)

    return output

def add_segment(board, x1, y1, x2, y2):
    for x in range(min(x1, x2), max(x1, x2) + 1):
        for y in range(min(y1, y2), max(y1, y2) + 1):
            board[(x, y)] += 1
    
    return board


def add_segment_diag(board, x1, y1, x2, y2):
    xs = range(min(x1, x2), max(x1, x2) + 1)
    ys = range(min(y1, y2), max(y1, y2) + 1)
    if x1 > x2:
        xs = reversed(xs)
    if y1 > y2:
        ys = reversed(ys)
    for x, y in zip(xs, ys):
        board[(x, y)] += 1

    return board

def part1(data) -> int:
    board = defaultdict(int)
    for x1, y1, x2, y2 in data:
        if x1 == x2 or y1 == y2:
            board = add_segment(board, x1, y1, x2, y2)

    return sum(1 for n in board.values() if n >=2)


def part2(data) -> int:
    board = defaultdict(int)
    for x1, y1, x2, y2 in data:
        if x1 == x2 or y1 == y2:
            board = add_segment(board, x1, y1, x2, y2)
        else:
            board = add_segment_diag(board, x1, y1, x2, y2)

    return sum(1 for n in board.values() if n >= 2)

if __name__ == '__main__':
    data = parse('day05.txt')
    print(part1(data))
    print(part2(data))