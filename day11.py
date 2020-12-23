from typing import List, Tuple, Dict
from collections import Counter
import copy
from pprint import PrettyPrinter

pprint = PrettyPrinter().pprint

def get_vis_seats(seats, row, col):
    vis_seats = []
    rows = range(len(seats))
    cols = range(len(seats[0]))
    for d_row in (-1, 0, 1):
        for d_col in (-1, 0, 1):
            if d_row == d_col == 0:
                continue
            
            cur_row = row + d_row
            cur_col = col + d_col

            while cur_row in rows and cur_col in cols:
                if seats[cur_row][cur_col] != '.':
                    vis_seats.append(seats[cur_row][cur_col])
                    continue
                cur_row += d_row
                cur_col += d_col

    return vis_seats

def get_vis_seats_dict(seats):
    vis_seats = {}
    rows = range(len(seats))
    cols = range(len(seats[0]))
    for row in rows:
        for col in cols:
            vis_seats_lst = []

            for d_row in (-1, 0, 1):
                for d_col in (-1, 0, 1):
                    if d_row == d_col == 0:
                        continue
                    
                    cur_row = row + d_row
                    cur_col = col + d_col

                    while cur_row in rows and cur_col in cols:
                        if seats[cur_row][cur_col] != '.':
                            vis_seats_lst.append((cur_row, cur_col))
                            break
                        cur_row += d_row
                        cur_col += d_col

            vis_seats[(row, col)] = vis_seats_lst

    return vis_seats

def get_adj_seats(seats, row, col):
    adj_seats = []
    rows = range(len(seats))
    cols = range(len(seats[0]))
    for d_row in (-1, 0, 1):
        for d_col in (-1, 0, 1):
            if d_row == d_col == 0:
                continue
            if row + d_row in rows and col + d_col in cols:
                adj_seats.append(seats[row + d_row][col + d_col])
    return adj_seats

def step(old_seats: List[List[str]]):
    new_seats = copy.deepcopy(old_seats)
    for row in range(len(old_seats)):
        for col in range(len(old_seats[0])):
            adj_seats = Counter(get_adj_seats(old_seats, row, col))
            if old_seats[row][col] == 'L' and adj_seats['#'] == 0:
                new_seats[row][col] = '#'
            elif old_seats[row][col] == '#' and adj_seats['#'] >= 4:
                new_seats[row][col] = 'L'
    return new_seats

def step_2(old_seats: List[List[str]], vis_seats: Dict):
    new_seats = copy.deepcopy(old_seats)
    for seat, vis_seat_lst in vis_seats.items():
        # if seat == (7, 9):
            # print(vis_seat_lst)
        ctr = []
        for vis_seat in vis_seat_lst:
            ctr.append(old_seats[vis_seat[0]][vis_seat[1]])
        ctr = Counter(ctr)
        if old_seats[seat[0]][seat[1]] == 'L' and ctr['#'] == 0:
            new_seats[seat[0]][seat[1]] = '#'
        elif old_seats[seat[0]][seat[1]] == '#' and ctr['#'] >= 5:
            new_seats[seat[0]][seat[1]] = 'L'

    return new_seats

def parse(filename: str) -> List[List[str]]:
    with open(filename) as f:
        data = [list(line.strip()) for line in f.readlines()]

    return data

if __name__ == '__main__':
    old_seats = parse('day11.txt')
    vis_seats = get_vis_seats_dict(old_seats)
    new_seats = step_2(old_seats, vis_seats)
    # pprint([''.join(row) for row in new_seats])
    while old_seats != new_seats:
        old_seats = new_seats
        new_seats = step_2(old_seats, vis_seats)
        # pprint([''.join(row) for row in new_seats])
        
    print(sum(row.count('#') for row in new_seats))
