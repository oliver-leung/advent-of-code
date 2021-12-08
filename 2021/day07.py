from os.path import join, dirname
from typing import List
from statistics import median, mean
import numpy as np


def parse(filename: str) -> List:
    with open(join(dirname(__file__), filename)) as f:
        data = f.readline().strip().split(',')
        data = [int(x) for x in data]

    return data


if __name__ == '__main__':
    x = np.array(parse('day07.txt'))
    print(sum(abs(x - median(x))))
    
    def fuel(d): return d*(d+1)/2
    print(min(sum(fuel(abs(x - np.floor(mean(x))))),
            sum(fuel(abs(x - np.ceil(mean(x)))))))
