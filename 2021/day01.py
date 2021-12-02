def parse(filename):
    with open(filename) as f:
        return [int(line) for line in f.readlines()]

def part1(data):
    increasing = 0
    for i in range(len(data) - 1):
        if data[i] < data[i+1]:
            increasing += 1
    return increasing

def part2(data):
    fst = data[:-2]
    snd = data[1:-1]
    trd = data[2:]
    triples = zip(fst, snd, trd)
    sums = [sum(triple) for triple in triples]
    return part1(sums)

if __name__=='__main__':
    data = parse('day01.txt')
    ans1 = part1(data)
    print(ans1)
    ans2 = part2(data)
    print(ans2)