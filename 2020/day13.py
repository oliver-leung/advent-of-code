def part_1(early_time, bus_ids):
    wait_times = [bus_id - (early_time % bus_id) for bus_id in bus_ids]
    idx = wait_times.index(min(wait_times))
    return bus_ids[idx] * wait_times[idx]

def part_2(bus_ids_offset):
    cur = 100000000000000
    step = 1
    while True:
        for bus_id, offset in bus_ids_offset:
            if (cur + offset) % bus_id == 0:
                step *= bus_id
                bus_ids_offset.remove((bus_id, offset))
            else:
                break
        if all([(cur + offset) % bus_id == 0 for bus_id, offset in bus_ids_offset]):
            return cur
        cur += step

def parse(filename: str):
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]
    
    early_time = int(data[0])
    bus_ids_offset = [x for x in data[1].split(',')]
    bus_ids_offset = zip(bus_ids_offset, range(len(bus_ids_offset)))
    bus_ids_offset = [(int(bus_id), num) for bus_id, num in bus_ids_offset if bus_id != 'x']

    bus_ids = [x[0] for x in bus_ids_offset]

    return early_time, bus_ids, bus_ids_offset

if __name__ == '__main__':
    data = parse('day13.txt')
    print('Part 1:', part_1(*data[:2]))
    print('Part 2:', part_2(data[2]))