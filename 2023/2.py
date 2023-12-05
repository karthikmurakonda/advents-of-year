from collections import defaultdict
from aocd import data
import re

lines = data.splitlines()
# lines = open('input.txt', 'r').read().splitlines()

def parseLines(lines) :
    ans = 0
    for line in lines :
        temp = line.split(':')[1]
        id = re.findall(r'\d+', line.split(':')[0])
        find = temp.split(';')
        mp = defaultdict(int)
        for i in range(len(find)) :
            balls = re.findall(r'\d+ (?:red|blue|green)', find[i])
            for ball in balls :
                num = int(ball.split(' ')[0])
                color = ball.split(' ')[1]
                mp[color] = max(mp[color], num)
        # if mp['red'] > 12 or mp['green'] > 13 or mp['blue'] > 14 :
        #     continue
        # else:
        #     print(id[0])
        #     ans += int(id[0])
        mul = 1
        for k, v in mp.items() :
            mul *= v
        ans += mul
        
    return ans


print(parseLines(lines))
