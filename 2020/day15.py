def part_1(nums):
    last, c = nums[-1], {n: i+1 for i, n in enumerate(nums)}
    for i in range(len(nums), 30000000):
        c[last], last = i, i - c.get(last, i)
    return last

def parse(filename: str):
    with open(filename) as f:
        data = [line.strip().split(',') for line in f.readlines()][0]

    return [int(x) for x in data]

if __name__ == '__main__':
    data = parse('day15.txt')
    print('Part 1:', part_1(data))