from typing import List
import math

def navigate_step(x, y, point, act, num):
    if act == 'N':
        y += num
    elif act == 'S':
        y -= num
    elif act == 'E':
        x += num
    elif act == 'W':
        x -= num
    elif act == 'L':
        point = (point + num) % 360
    elif act == 'R':
        point = (point - num) % 360
    elif act == 'F':
        point_rad = point * math.pi / 180
        x += math.cos(point_rad) * num
        y += math.sin(point_rad) * num

    return round(x), round(y), point

def navigate(dirs):
    state = (0, 0, 0)
    for direction in dirs:
        state = navigate_step(*state, *direction)
        # print(state)
    return state


def navigate_step_2(x, y, act, num, way_x, way_y):
    if act == 'N':
        way_y += num
    elif act == 'S':
        way_y -= num
    elif act == 'E':
        way_x += num
    elif act == 'W':
        way_x -= num
    elif act == 'L':
        num_rad = num * math.pi / 180
        new_way_x = way_x * math.cos(num_rad) - way_y * math.sin(num_rad)
        new_way_y = way_x * math.sin(num_rad) + way_y * math.cos(num_rad)
        way_x, way_y = new_way_x, new_way_y
    elif act == 'R':
        num_rad = -num * math.pi / 180
        new_way_x = way_x * math.cos(num_rad) - way_y * math.sin(num_rad)
        new_way_y = way_x * math.sin(num_rad) + (way_y * math.cos(num_rad))
        way_x, way_y = new_way_x, new_way_y

    elif act == 'F':
        x += way_x * num
        y += way_y * num

    return (round(x), round(y)), (round(way_x), round(way_y))

def navigate_2(dirs):
    state = (0, 0)
    waypt = (10, 1)
    for direction in dirs:
        state, waypt = navigate_step_2(*state, *direction, *waypt)
        # print(state, waypt)
    return state



def parse(filename: str) -> List:
    with open(filename) as f:
        data = [line.strip() for line in f.readlines()]

    data = [(line[:1], int(line[1:])) for line in data]
    return data

if __name__ == '__main__':
    dirs = parse('day12.txt')
    x, y, _ = navigate(dirs)
    # print(abs(x) + abs(y))

    x, y = navigate_2(dirs)
    print(abs(x) + abs(y))