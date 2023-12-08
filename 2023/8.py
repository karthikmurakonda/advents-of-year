from math import lcm
from aocd import data

lines = data.splitlines()
# lines = open("input.txt").read().splitlines()

instructions = []
docs = {}

def parse():
    for c in lines[0]:
        instructions.append(c)
    for i in range(2,len(lines)):
        splited = lines[i].split(" = ")
        docs[splited[0]] = splited[1].split(", ")
        for j in range(len(docs[splited[0]])):
            docs[splited[0]][j] = docs[splited[0]][j].strip('(')
            docs[splited[0]][j] = docs[splited[0]][j].strip(')')

def part1():
    ans = 0
    curr = 'AAA'
    while curr != 'ZZZ':
        # print(instructions[ans%len(instructions)] )
        if instructions[ans%len(instructions)] == 'L':
            curr = docs[curr][0]
        elif instructions[ans%len(instructions)] == 'R':
            curr = docs[curr][1]
        ans += 1
    print(ans)

def getInit(lst):
    ret = []
    for i in lst:
        if i[-1] == 'A':
            ret.append(i)
    return ret

def checkCurr(curr):
    if not curr.endswith('Z'):
            return False
    return True

def part2():
    curr = getInit(docs.keys())
    totals = []
    for c in curr:
        ans = 0
        while not checkCurr(c):
            if instructions[ans%len(instructions)] == 'L':
                c = docs[c][0]
            elif instructions[ans%len(instructions)] == 'R':
                c = docs[c][1]
            ans += 1
        totals.append(ans)
    # lcm of totals
    print(lcm(*totals))


    

if __name__ == "__main__":
    parse()
    # part1()
    part2()
    # print(instructions)
    # print(docs)