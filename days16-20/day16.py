import re

def parse(filename: str):
    with open(filename) as f:
        lines = [line.strip() for line in f.readlines()]

    ranges = {}
    for line in lines[:20]:
        line = re.split(r': |-| or ', line)
        nums = [int(x) for x in line[1:]]
        ranges[line[0]] = [(nums[0], nums[1]), (nums[2], nums[3])]

    your_ticket = [int(x) for x in lines[22].split(',')]

    nearby_tickets = []
    for line in lines[25:]:
        nearby_tickets.append([int(x) for x in line.split(',')])

    return ranges, your_ticket, nearby_tickets

def part_1(ranges, nearby_tickets):
    invalids = []
    for ticket in nearby_tickets:
        invalids += get_invalids(ranges, ticket)
    print(sum(invalids))

def get_invalids(ranges, ticket):
    invalids = []
    for num in ticket:
        satisfied = False
        for (lo1, up1), (lo2, up2) in ranges.values():
            if num in range(lo1, up1 + 1) or num in range(lo2, up2 + 1):
                satisfied = True
        if not satisfied:
            invalids.append(num)
    return invalids

def part_2(ranges, your_ticket, nearby_tickets):
    valids = [t for t in nearby_tickets if get_invalids(ranges, t) == []]
    poss = {key: [] for key in ranges.keys()}

    for i in range(len(your_ticket)):
        col = [ticket[i] for ticket in valids]
        for key, ((lo1, up1), (lo2, up2)) in ranges.items():
            if all([num in range(lo1, up1 + 1) or num in range(lo2, up2 + 1) for num in col]):
                poss[key].append(i)

    correct = {key: None for key in ranges.keys()}

    while poss != {}:
        for key, value in poss.items():
            if len(value) == 1:
                correct[key] = value[0]
                poss.pop(key, None)
                for key2, value2 in poss.items():
                    value2.remove(value[0])
                    poss[key2] = value2
                break

    prod = 1
    for key, value in correct.items():
        if 'departure' in key:
            print(key, value)
            prod *= your_ticket[value]
    
    print(prod)


if __name__ == '__main__':
    data = parse('day16.txt')
    part_1(data[0], data[2])
    part_2(*data)