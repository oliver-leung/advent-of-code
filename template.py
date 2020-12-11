from typing import List


def parse(filename: str) -> List:
    with open(filename) as f:
        data = f.readlines()

    return data