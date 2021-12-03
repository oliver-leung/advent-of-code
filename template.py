from os.path import join, dirname
from typing import List


def parse(filename: str) -> List:
    with open(join(dirname(__file__), filename)) as f:
        data = [line.strip() for line in f.readlines()]

    return data

if __name__ == '__main__':
    pass