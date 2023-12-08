from collections import defaultdict
from aocd import data
import copy

lines = data.splitlines()
# lines = open("input.txt").read().splitlines()

def parse():
    for i in range(len(lines)):
        lines[i] = lines[i].split(" ")
        lines[i][1] = int(lines[i][1])

def most_common(k):
    mp = defaultdict(int)
    for i in range(len(k)):
        mp[k[i]]+=1
    items = list(mp.items())
    items.sort(key=lambda x: (-x[1], x[0]))
    return items[0][0] if items[0][0] != 'J' else items[1][0] if len(items) > 1 else '-'

def type(k):
    comm = most_common(k)
    k = k.replace('J', comm)
    print(k)
    mp = defaultdict(int)
    for i in range(len(k)):
        mp[k[i]]+=1
    if len(mp) == 1:
        return 0
    elif len(mp) == 2:
        if mp[k[0]] == 1 or mp[k[0]] == 4:
            return 1
        else:
            return 2
    elif len(mp) == 3:
        items = list(mp.values())
        items.sort()
        if items[-1] == 3:
            return 3
        else:
            return 4
    elif len(mp) == 4:
        return 5
    else:
        return 6


def replace(k):
    mp = {
        'A': 'Z',
        'K': 'Y',
        'Q': 'X',
        'J': '1',
        'T': 'V'
    }
    for c in k:
        if c in mp:
            k = k.replace(c, mp[c])
    return k

def part1():
    data = copy.deepcopy(lines)
    # for i in data:
    #     print(type(i[0]), i[0])
    s = sorted(data, key=lambda x: (-type(x[0]), replace(x[0])))
    # print(s)
    ans = 0
    for i in range(len(s)):
        ans += (i+1)*s[i][1]
        print(s[i][0], (i+1), s[i][1])
    print(ans)


if __name__ == "__main__":
    parse()
    part1()