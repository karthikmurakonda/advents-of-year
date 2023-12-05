from collections import defaultdict
from aocd import data

lines = data.splitlines()
lines = open('input.txt', 'r').read().splitlines()

def condition(i, j, input_data):
    if i > 0 and (input_data[i - 1][j] != '' and isinstance(input_data[i - 1][j], str)):
        return True
    if i < len(input_data) - 1 and (input_data[i + 1][j] != '' and isinstance(input_data[i + 1][j], str)):
        return True
    if j > 0 and (input_data[i][j - 1] != '' and isinstance(input_data[i][j - 1], str)):
        return True
    if j < len(input_data[0]) - 1 and (input_data[i][j + 1] != '' and isinstance(input_data[i][j + 1], str)):
        return True
    # diagonal
    if i > 0 and j > 0 and (input_data[i - 1][j - 1] != '' and isinstance(input_data[i - 1][j - 1], str)):
        return True
    if i > 0 and j < len(input_data[0]) - 1 and (input_data[i - 1][j + 1] != '' and isinstance(input_data[i - 1][j + 1], str)):
        return True
    if i < len(input_data) - 1 and j > 0 and (input_data[i + 1][j - 1] != '' and isinstance(input_data[i + 1][j - 1], str)):
        return True
    if i < len(input_data) - 1 and j < len(input_data[0]) - 1 and (input_data[i + 1][j + 1] != '' and isinstance(input_data[i + 1][j + 1], str)):
        return True
    return False


def parse_data(lines):
    input_data = []
    for line in lines:
        curr = []
        for c in line:
            if c == '.':
                curr.append('')
            elif c.isnumeric():
                curr.append(int(c))
            else:
                curr.append(c)
        input_data.append(curr)
    return input_data

def part1():
    input_data = parse_data(lines)
    # print(input_data)
    ans = 0
    for i in range(len(input_data)):
        curr_bool = False
        curr_num = 0
        for j in range(len(input_data[0])):
            if input_data[i][j] == '' or isinstance(input_data[i][j], str):
                if curr_bool:
                    # print(curr_num)
                    ans += curr_num
                curr_bool = False
                curr_num = 0
            elif isinstance(input_data[i][j], int):
                curr_num = curr_num*10 + input_data[i][j]
                if condition(i, j, input_data):
                    curr_bool = True
        if curr_bool:
            # print(curr_num)
            ans += curr_num
    return ans

def get_star_neighbors(i, j, input_data):
    neighbor_stars = []
    # horizontal
    if i > 0 and input_data[i - 1][j] == '*':
        neighbor_stars.append((i - 1, j))
    if i < len(input_data) - 1 and input_data[i + 1][j] == '*':
        neighbor_stars.append((i + 1, j))
    if j > 0 and input_data[i][j - 1] == '*':
        neighbor_stars.append((i, j - 1))
    if j < len(input_data[0]) - 1 and input_data[i][j + 1] == '*':
        neighbor_stars.append((i, j + 1))
    # diagonal
    if i > 0 and j > 0 and input_data[i - 1][j - 1] == '*':
        neighbor_stars.append((i - 1, j - 1))
    if i > 0 and j < len(input_data[0]) - 1 and input_data[i - 1][j + 1] == '*':
        neighbor_stars.append((i - 1, j + 1))
    if i < len(input_data) - 1 and j > 0 and input_data[i + 1][j - 1] == '*':
        neighbor_stars.append((i + 1, j - 1))
    if i < len(input_data) - 1 and j < len(input_data[0]) - 1 and input_data[i + 1][j + 1] == '*':
        neighbor_stars.append((i + 1, j + 1))
    return neighbor_stars

def part2():
    input_data = parse_data(lines)
    # print(input_data)
    ans = 0
    star_map = defaultdict(list)
    for i in range(len(input_data)):
        curr_bool = False
        curr_num = 0
        stars_set = set()
        for j in range(len(input_data[0])):
            if input_data[i][j] == '' or isinstance(input_data[i][j], str):
                for star in stars_set:
                    star_map[star].append(curr_num)
                stars_set = set()
                curr_num = 0
            elif isinstance(input_data[i][j], int):
                for star in get_star_neighbors(i, j, input_data):
                    stars_set.add(star)
                curr_num = curr_num*10 + input_data[i][j]
        for star in stars_set:
            star_map[star].append(curr_num)
    for star in star_map:
        if len(star_map[star]) == 2:
            ans += star_map[star][0] * star_map[star][1]
    return ans

print(part1())
print(part2())

            