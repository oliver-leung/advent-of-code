from os.path import join, dirname
from typing import List


def parse(filename: str) -> List[str]:
    with open(join(dirname(__file__), filename)) as f:
        data = [line.strip() for line in f.readlines()]
        # data = [int(n, base=2) for n in data]

    return data

def part1(data: List[str]):
    gam, eps = '', ''
    half = len(data) / 2
    size = len(data[0])

    for i in range(size):
        ones = sum(1 for n in data if n[i] == '1')
        gam += '1' if ones > half else '0'
        eps += '0' if ones > half else '1'

    gam = int(gam, base=2)
    eps = int(eps, base=2)
    return gam * eps


if __name__ == '__main__':
    data = parse('day03.txt')
    ans1 = part1(data)
    print(ans1)
