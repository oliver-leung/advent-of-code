from typing import List, Tuple


def contains_sum(target: int, nums: List[int]) -> bool:
    seen = set()
    for num in nums:
        if target - num in seen:
            return True
        else:
            seen.add(num)

    return False

def find_first(nums: List[int]) -> int:
    for i in range(25, len(nums)):
        if not contains_sum(nums[i], nums[i-25: i]):
            return nums[i]

    return 0

def find_range(target: int, nums: List[int]) -> Tuple[int, int]:
    first, last = 0, 1
    while last < len(nums):
        sum_ = sum(nums[first: last + 1])
        if sum_ < target:
            last += 1
        elif sum_ > target:
            first += 1
        else:
            min_ = min(nums[first: last + 1])
            max_ = max(nums[first: last + 1])
            return min_, max_
    return 0, 0

def parse(filename: str) -> List[int]:
    with open(filename) as f:
        data = f.readlines()

    return [int(x) for x in data]

nums = parse('day9.txt')
targ = find_first(nums)
print(targ)
print(sum(find_range(targ, nums)))