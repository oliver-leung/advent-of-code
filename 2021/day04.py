from os.path import join, dirname
from typing import List
from pprint import pprint


def parse(filename: str):
    with open(join(dirname(__file__), filename)) as f:
        data = [line.strip() for line in f.readlines()]

    draws = [int(n) for n in data[0].split(',')]

    boards = []
    for line in data[1:]:
        if line == '':
            boards.append([])
        else:
            boards[-1].append([int(n) for n in line.split()])

    return draws, boards


def replace(board: List[List[int]], m: int):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == m:
                board[i][j] = 'drawn'

    return board

def sum(board: List[List[int]]) -> int:
    sum = 0
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] != 'drawn':
                sum += board[i][j]
    return sum

def bingo(board: List[List[int]]) -> bool:
    for i in range(len(board)):
        if all(board[i][j] == 'drawn' for j in range(len(board[i]))):
            return True
        if all(board[j][i] == 'drawn' for j in range(len(board[i]))):
            return True
    if all(board[i][i] == 'drawn' for i in range(len(board))):
        return True
    if all(board[i][len(board) - i - 1] == 'drawn' for i in range(len(board))):
        return True
    return False

def part1(draws, boards):
    for m in draws:
        for board in boards:
            board = replace(board, m)
            if bingo(board):
                return sum(board) * m

def part2(draws, boards):
    for m in draws:
        for board in boards:
            board = replace(board, m)
        new_boards = [board for board in boards if not bingo(board)]

        if len(new_boards) == 0:
            return sum(boards[0]) * m
            
        boards = new_boards

if __name__ == '__main__':
    draws, boards = parse('day04.txt')
    print(part1(draws, boards))
    print(part2(draws, boards))
    