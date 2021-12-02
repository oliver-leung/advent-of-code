import os


def parse(filename: str) -> list:
    with open(os.path.join(os.path.dirname(__file__), filename)) as f:
        lines = [line.strip().split() for line in f.readlines()]
        data = [(a, int(b)) for a, b in lines]
        return data

def part1(data: list) -> tuple:
    horiz = 0
    depth = 0

    for com, x in data:
        if com == 'forward':
            horiz += x
        elif com == 'down':
            depth += x
        elif com == 'up':
            depth -= x
    
    return horiz, depth


def part2(data: list) -> tuple:
    horiz = 0
    depth = 0
    aim = 0

    for com, x in data:
        if com == 'forward':
            horiz += x
            depth += aim * x
        elif com == 'down':
            aim += x
        elif com == 'up':
            aim -= x

    return horiz, depth

if __name__=='__main__':
    data = parse('day02.txt')
    horiz, depth = part1(data)
    print("Part 1:", horiz * depth)
    horiz, depth = part2(data)
    print("Part 2:", horiz * depth)
