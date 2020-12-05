from functools import reduce
import operator

def count_trees(trees):
    width = len(trees[0])
    col, count = 0, 0

    for row in trees:
        if row[col]:
            count += 1
        col += 3
        col = col % width

    return count

def count_trees_2(trees):
    width = len(trees[0])
    height = len(trees)
    
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    count = [0] * len(slopes)

    for num, (dy, dx) in enumerate(slopes):
        row, col = 0, 0
        while row < height:

            if trees[row][col]:
                count[num] += 1
            row += dx
            col += dy
            col %= width

    return count


def parse():
    with open('day3.txt') as f:
        data = f.readlines()

    ans = []
    is_tree = lambda x : x == '#'
    for line in data:
        bools = [is_tree(c) for c in line.strip()]
        ans.append(bools)

    return ans

trees = parse()
print(count_trees(trees))
print(reduce(operator.mul, count_trees_2(trees)))