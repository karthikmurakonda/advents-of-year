from aocd import get_data
lines = get_data(day=20, year=2022).splitlines()
# lines = []
# with open("input.txt") as f:
#     lines = f.readlines()
lines = [811589153*int(x.strip()) for x in lines]

def part1():
    old = [(i, x) for i, x in enumerate(lines)]
    new = [(i, x) for i, x in enumerate(lines)]
    # print(new)
    for _ in range(10):
        for i in range(len(lines)):
            new_ind = new.index((i, lines[i]))
            to_ind = lines[i]%(len(new)-1)
            to_ind += new_ind
            if to_ind >= len(new):
                to_ind = to_ind - len(new) + 1
            elif to_ind < 0:
                to_ind = len(new) - to_ind -1
            # print(to_ind)
            new.remove((i, lines[i]))
            new.insert(to_ind, (i, lines[i]))
            # print(new)
        lines_zero_ind = lines.index(0)
        zero_ind = new.index((lines_zero_ind, 0))
    
    print(new[(zero_ind + 1000) % len(new)][1])
    print(new[(zero_ind + 2000) % len(new)][1] )
    print(new[(zero_ind + 3000) % len(new)][1] )
    # sum = new[(zero_ind + 1000) % len(new)][0] + new[(zero_ind + 2000) % len(new)][0] + new[(zero_ind + 3000) % len(new)][0]
    sum = new[(zero_ind + 1000) % len(new)][1] + new[(zero_ind + 2000) % len(new)][1] + new[(zero_ind + 3000) % len(new)][1]
    print(sum)


if __name__ == "__main__":
    part1()
