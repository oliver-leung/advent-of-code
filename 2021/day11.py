from os.path import join, dirname
from typing import List
import sys
import numpy as np


def parse(filename: str) -> List:
    with open(join(dirname(__file__), filename)) as f:
        data = [list(line.strip()) for line in f.readlines()]
        data = np.array(data)
        data = data.astype(int)

    return np.array(data)

def flash(data, x, y):
    data_range = range(len(data))
    for i in (-1, 0, 1):
        for j in (-1, 0, 1):
            x_i = x + i
            y_j = y + j
            if (i, j) == (0, 0):
                data[x_i, y_j] = -1
            elif x_i in data_range and y_j in data_range and data[x_i, y_j] != -1:
                data[x + i, y + j] += 1
    return data

def part1(data: List, steps: int) -> int:
    flashes = 0
    for i in range(steps):
        data += 1
        while np.any(data > 9):
            flashable = np.stack(np.where(data > 9)).T
            flashes += len(flashable)
            for x, y in flashable:
                data = flash(data, x, y)
        data = np.where(data == -1, 0, data)
    return flashes
    

def part2(data: List) -> int:
    flashes = 0
    i = 0
    while True:
        data += 1
        i += 1
        while np.any(data > 9):
            flashable = np.stack(np.where(data > 9)).T
            flashes += len(flashable)
            for x, y in flashable:
                data = flash(data, x, y)
        if np.count_nonzero(data == -1) == data.size:
            print(data)
            return i + 1  # Not sure why this is + 1
        data = np.where(data == -1, 0, data)
    return flashes

if __name__ == '__main__':
    input = 'input.txt'
    data = parse(input)
    print(part1(data, 100))
    print(part2(data))
