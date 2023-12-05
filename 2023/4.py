from aocd import data
import re
lines = data.splitlines()
# lines = open('input.txt', 'r').read().splitlines()
def part1():
    ans = 0
    for line in lines :
        line = line.strip().split(':')[1]
        winning = re.findall(r'\d+', line.split('|')[0])
        haves = re.findall(r'\d+', line.split('|')[1])
        curr = 0
        for i in winning:
            if i in haves:
                if curr == 0:
                    curr = 1
                else:
                    curr *= 2
        print(curr)
        ans += curr
    print(ans)

def part2():
    ans = 0
    dp = [1 for i in range(len(lines))]
    for i, line in enumerate(lines):
        line = line.strip().split(':')[1]
        winning = re.findall(r'\d+', line.split('|')[0])
        haves = re.findall(r'\d+', line.split('|')[1])
        curr = 0
        for num in winning:
            if num in haves:
                curr += 1
        for k in range(i+1, i+curr+1):
            dp[k] += dp[i]
    # print(dp)
    print(sum(dp))

# part1()
part2()
