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

def part2(data: List[str]):
    oxy = data
    co2 = data
    size = len(data[0])

    for i in range(size):
        ones = sum(1 for n in oxy if n[i] == '1')
        half = len(oxy) / 2
        if ones >= half:
            oxy = [n for n in oxy if n[i] == '1']
        else:
            oxy = [n for n in oxy if n[i] == '0']

        if len(oxy) == 1:
            break


    for i in range(size):
        zeros = sum(1 for n in co2 if n[i] == '0')
        half = len(co2) / 2
        if zeros <= half:
            co2 = [n for n in co2 if n[i] == '0']
        else:
            co2 = [n for n in co2 if n[i] == '1']
        
        if len(co2) == 1:
            break

    oxy = int(oxy[0], base=2)
    co2 = int(co2[0], base=2)

    print(oxy, co2)
    return oxy * co2

if __name__ == '__main__':
    data = parse('day03.txt')
    ans1 = part1(data)
    print(ans1)
    ans2 = part2(data)
    print(ans2)
