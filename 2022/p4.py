from aocd import data,lines

# print(lines)
def solve_1():
    ans = 0
    for line in lines:
        range1 = line.split(',')[0]
        range2 = line.split(',')[1]
        range1 = range1.split('-')
        range2 = range2.split('-')
        range1 = [int(range1[0]),int(range1[1])]
        range2 = [int(range2[0]),int(range2[1])]
        # check if one range is in the other
        if range1[0] >= range2[0] and range1[1] <= range2[1]:
            ans += 1
        elif range2[0] >= range1[0] and range2[1] <= range1[1]:
            ans += 1
    return ans
def solve_2():
    ans = 0
    for line in lines:
        range1 = line.split(',')[0]
        range2 = line.split(',')[1]
        range1 = range1.split('-')
        range2 = range2.split('-')
        range1 = [int(range1[0]),int(range1[1])]
        range2 = [int(range2[0]),int(range2[1])]
        # check if ranges overlap
        if range1[0] <= range2[0] and range1[1] >= range2[0]:
            ans += 1
        elif range2[0] <= range1[0] and range2[1] >= range1[0]:
            ans += 1
    return ans

if __name__ == "__main__":
    print(solve_1())
    print(solve_2())