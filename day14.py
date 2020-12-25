from typing import Any, List
import re

def part_1(insns, mem_max):
    mem = [0] * (mem_max + 1)
    mask_or = 0
    mask_and = 0
    for ins in insns:
        if ins[0] == 'mask':
            mask_or = int(ins[1].replace('X', '0'), 2)
            mask_and = int(ins[1].replace('X', '1'), 2)
        elif ins[0] == 'mem':
            mem[ins[1]] = (ins[2] | mask_or) & mask_and
    return sum(mem)

def parse(filename: str):
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]

    insns = []
    for line in data:
        line = re.split(r'\[|\]* = ', line)
        if line[0] == 'mem':
            line = [line[0], int(line[1]), int(line[2])]
        insns.append(line)

    mem_max = max([ins[1] for ins in insns if ins[0] == 'mem'])

    return insns, mem_max

if __name__ == '__main__':
    data = parse('day14.txt')
    print(part_1(*data))