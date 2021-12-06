from os.path import join, dirname
from typing import List
from collections import Counter, defaultdict
from time import time


def parse(filename: str) -> List:
    with open(join(dirname(__file__), filename)) as f:
        data = f.readline().strip().split(',')
        data = [int(x) for x in data]

    return defaultdict(int, Counter(data))

def step_states(states):
    new_states = defaultdict(int)
    for i in range(1, 9):
        new_states[i - 1] += states[i]
    new_states[6] += states[0]
    new_states[8] = states[0]

    return new_states

def iterate(data: List, n) -> int:
    for i in range(n):
        data = step_states(data)

    return sum(data.values())

if __name__ == '__main__':
    data = parse('day06.txt')
    start_time = time()
    print(iterate(data, 80))
    print(iterate(data, 256))
    print('took', time() - start_time, 'seconds')
