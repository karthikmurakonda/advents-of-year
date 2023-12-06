from math import sqrt
from aocd import data
import re

lines = data.splitlines()
# lines = open('input.txt', 'r').read().splitlines()

times = re.findall(r'\d+', lines[0])
distances = re.findall(r'\d+', lines[1])

p2time = ""
p2distance = ""
for i in range(len(times)):
    p2time += times[i]
    p2distance += distances[i]
p2time = int(p2time)
p2distance = int(p2distance)

times = [int(i) for i in times]
distances = [int(i) for i in distances]



def part1():
    ans = 1
    for i in range(len(times)):
        curr = 0
        for j in range(1,times[i]):
            if  j * (times[i] - j) > distances[i]:
                # print(j)
                curr += 1
        ans *= curr
        # print()
    print(ans)

def part2():
    ans = 0

    delta =  sqrt(p2time**2 - 4 * p2distance)
    x1 = (p2time + delta) / 2
    x2 = (p2time - delta) / 2
    x1 = int(x1)
    x2 = int(x2)
    # print(x1, x2)
    print(x1 - x2)

part1()
part2()
