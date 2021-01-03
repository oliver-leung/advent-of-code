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

def get_mem_writes(mask, mem):
    addrs = [mem]
    for i in range(36):
        new_addrs = []
        for addr in addrs:
            new_addr = addr.copy()
            if mask[i] == '1':
                new_addr[i] = '1'
                new_addrs.append(new_addr)
            elif mask[i] == 'X':
                new_addr[i] = '0'
                new_addrs.append(new_addr)
                new_addr = new_addr.copy()
                new_addr[i] = '1'
                new_addrs.append(new_addr)
            else:
                new_addrs.append(new_addr)
        addrs = new_addrs
    addrs = [int(''.join(addr), 2) for addr in addrs]
    # print(addrs)
    return addrs

def part_2(insns, mem_max):
    mem = {}
    mask = [0] * 36

    for ins in insns:
        if ins[0] == 'mask':
            mask = ins[1]
        elif ins[0] == 'mem':
            mem_writes = get_mem_writes(mask, ins[1])
            # print(mem_writes)
            for addr in mem_writes:
                mem[addr] = ins[2]

    return sum(mem.values())

def parse_2(filename: str):
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]

    insns = []
    for line in data:
        line = re.split(r'\[|\]* = ', line)

        if line[0] == 'mem':
            addr = list(bin(int(line[1])))[2:]
            addr_extend = (['0'] * (36 - len(addr))) + addr
            line = [line[0], addr_extend, int(line[2])]
        elif line[0] == 'mask':
            mask = list(line[1])
            line = [line[0], mask]
        insns.append(line)
    
    mem_max = max([int(''.join(ins[1]), 2) for ins in insns if ins[0] == 'mem'])
    return insns, 0

if __name__ == '__main__':
    data = parse('day14.txt')
    print(part_1(*data))
    data = parse_2('day14.txt')
    # print(data)
    print(part_2(*data))