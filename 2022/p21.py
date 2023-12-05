from aocd import lines

# lines = """root: pppw + sjmn
# dbpl: 5
# cczh: sllz + lgvd
# zczc: 2
# ptdq: humn - dvpt
# dvpt: 3
# lfqf: 4
# humn: 5
# ljgn: 2
# sjmn: drzm * dbpl
# sllz: 4
# pppw: cczh / lfqf
# lgvd: ljgn * ptdq
# drzm: hmdt - zczc
# hmdt: 32"""

# lines = lines.splitlines()

value_monkey_cache = {}

def get_monkey_value(monkey, monkeys):
    if monkey in value_monkey_cache:
        return value_monkey_cache[monkey]
    if type(monkeys[monkey]) == int or type(monkeys[monkey]) == float:
        value_monkey_cache[monkey] = monkeys[monkey]
        return monkeys[monkey]
    else:
        monkey1, monkey2, operator = monkeys[monkey]
        value_monkey_cache[monkey] = operator(get_monkey_value(monkey1, monkeys), get_monkey_value(monkey2, monkeys))
        return value_monkey_cache[monkey]


def part1():
    monkeys = {}
    for line in lines:
        line = line.split()
        if len(line) == 2:
            monkey = line[0][:-1]
            monkeys[monkey] = int(line[1])
        else:
            monkey, monkey1, operator, monkey2 = line
            monkey = monkey[:-1]
            if operator == "+":
                monkeys[monkey] = [monkey1, monkey2, lambda x, y: x + y]
            elif operator == "*":
                monkeys[monkey] = [monkey1, monkey2, lambda x, y: x * y]
            elif operator == "-":
                monkeys[monkey] = [monkey1, monkey2, lambda x, y: x - y]
            elif operator == "/":
                monkeys[monkey] = [monkey1, monkey2, lambda x, y: x / y]
    return get_monkey_value("root", monkeys)


# part is just binary search to find the value of humn
def part2():
    global value_monkey_cache
    monkeys = {}
    for line in lines:
        line = line.split()
        if len(line) == 2:
            monkey = line[0][:-1]
            monkeys[monkey] = int(line[1])
        else:
            monkey, monkey1, operator, monkey2 = line
            monkey = monkey[:-1]
            if operator == "+":
                monkeys[monkey] = [monkey1, monkey2, lambda x, y: x + y]
            elif operator == "*":
                monkeys[monkey] = [monkey1, monkey2, lambda x, y: x * y]
            elif operator == "-":
                monkeys[monkey] = [monkey1, monkey2, lambda x, y: x - y]
            elif operator == "/":
                monkeys[monkey] = [monkey1, monkey2, lambda x, y: x / y]
    monkeys["root"][2] = lambda x, y: x - y
    # humn_guess = 3379022190351
    # monkeys["humn"] = humn_guess
    # print(get_monkey_value("root", monkeys))
    left = 0
    right = 1e32
    monkeys["humn"] = 0
    initial_left = get_monkey_value("root", monkeys)
    print(initial_left)
    value_monkey_cache = {}
    monkeys["humn"] = 1e32
    initial_right = get_monkey_value("root", monkeys)
    print(initial_right)
    value_monkey_cache = {}
    while left < right:
        monkeys["humn"] = (left + right) // 2
        if get_monkey_value("root", monkeys) > 0:
            left = monkeys["humn"]+1
        elif get_monkey_value("root", monkeys) < 0:
            right = monkeys["humn"]-1
        else:
            break
        value_monkey_cache = {}
    return monkeys["humn"]
print(part2())