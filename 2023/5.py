from aocd import data
import re

lines = data.splitlines()
# lines = open('input.txt', 'r').read().splitlines()
seeds = []
maps = []

def parse():
    global seeds, maps
    seedLine = lines[0].strip().split(':')[1]
    seeds = re.findall(r'\d+', seedLine)
    seeds = [int(i) for i in seeds]
    # print(seeds)
    for i in range(1, len(lines)):
        if lines[i] == '':
            continue
        if ':' in lines[i]:
            maps.append({})
            continue
        curr = maps[-1]
        nums = re.findall(r'\d+', lines[i])
        nums = [int(i) for i in nums]
        curr[nums[1]] = [nums[0], nums[2]]


def part1():
    ans = []
    for i in range(0,len(seeds),2):
        seedStart, seedRange, skip = seeds[i], seeds[i+1], seeds[i+1]
        nextSeed = seedStart
        while nextSeed <= seedStart + seedRange:
            curr = nextSeed
            for mp in maps:
                for k,v in mp.items():
                    if k <= curr < k + v[1]:
                        skip = min(skip, k + v[1] - curr)
                        curr += (v[0] - k)
                        if skip <= 0:
                            skip = 1
                        break
            ans.append(curr)
            # print(nextSeed, skip)
            nextSeed += skip
            skip = seedRange - nextSeed + seedStart
    print(min(ans))

if __name__ == '__main__':
    parse()
    part1()