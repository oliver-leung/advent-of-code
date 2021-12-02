def find_sum(nums, sum_):
    seen_nums = set()

    for num1 in nums:
        for num2 in nums:
            if num1 is num2:
                continue
            difference = sum_ - num1 - num2
            if difference in seen_nums and difference is not num1 and difference is not num2:
                return num1, num2, difference
            seen_nums.add(num1)
            seen_nums.add(num2)

with open('day1.txt', 'r') as f:
    data = f.readlines()

data_int = [int(x) for x in data]

print(find_sum(data_int, 2020))