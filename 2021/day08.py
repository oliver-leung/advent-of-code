from os.path import join, dirname
from typing import List


def parse(filename: str) -> List:
    with open(join(dirname(__file__), filename)) as f:
        data = [line.strip().split(' | ') for line in f.readlines()]
        data = [(patterns.split(), outputs.split()) for patterns, outputs in data]

    return data

def part1(data: List) -> int:
    ans = 0
    for _, outputs in data:
        ans += sum(1 for code in outputs if len(code) in [2, 3, 4, 7])
    return ans

def part2(data: List) -> int:
    ans = 0
    for patterns, outputs in data:
        pass

if __name__ == '__main__':
    data = parse('day08.txt')
    print(part1(data))
