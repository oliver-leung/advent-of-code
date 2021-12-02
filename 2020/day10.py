from typing import List

def diffs(jolts: List[int]) -> List[int]:
    ans = [0] * 4
    prevs = [0] + jolts
    curs = jolts + [jolts[-1] + 3]
    for prev, cur in list(zip(prevs, curs)):
        ans[cur - prev] += 1
    return ans

def arrangements(jolts: List[int]) -> int:
    dp = [1]
    for i in range(1, len(jolts)):
        ans = 0
        for j in range(i):
            if jolts[j] + 3 >= jolts[i]:
                ans += dp[j]
        dp.append(ans)
    return dp[-1]

def parse(filename: str) -> List[int]:
    with open(filename) as f:
        data = f.readlines()

    jolts = [int(x) for x in data]
    jolts.sort()
    return jolts

jolts = parse('day10.txt')
differences = diffs(jolts)
print(differences[1] * differences[3])
print(arrangements([0] + jolts + [jolts[-1] + 3]))