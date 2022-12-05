from aocd import data,lines
stacks = [[] for i in range(9)]

def get_input():
    """
    parse input into a list of lists. each list is a stack of numbers in a vertical column
    stack input: (space separated)
            [H]         [S]         [D]
        [S] [C]         [C]     [Q] [L]
        [C] [R] [Z]     [R]     [H] [Z]
        [G] [N] [H] [S] [B]     [R] [F]
    [D] [T] [Q] [F] [Q] [Z]     [Z] [N]
    [Z] [W] [F] [N] [F] [W] [J] [V] [G]
    [T] [R] [B] [C] [L] [P] [F] [L] [H]
    [H] [Q] [P] [L] [G] [V] [Z] [D] [B]
    """
    for i in range(8):
        for j in range(9):
            if lines[i][4*j+1] != ' ':
                stacks[j].append(lines[i][4*j+1])
    for i in range(9):
        stacks[i].reverse()
    # print(stacks)

# print(lines)
def solve_1():
    for i in range(10,len(lines)):
        line = lines[i].split(' ')
        n = int(line[1])
        s = int(line[3])
        d = int(line[5])
        for j in range(n):
            print(n,s,d)
            stacks[d-1].append(stacks[s-1].pop())
    # print top card of each stack
    for stack in stacks:
        if len(stack) > 0:
            print(stack[-1],end='')
    print()

def solve_2():
    for i in range(10,len(lines)):
        line = lines[i].split(' ')
        n = int(line[1])
        s = int(line[3])
        d = int(line[5])
        temp_stack = []
        for j in range(n):
            temp_stack.append(stacks[s-1].pop())
        for j in range(n):
            stacks[d-1].append(temp_stack.pop())
    # print top card of each stack
    for stack in stacks:
        if len(stack) > 0:
            print(stack[-1],end='')
    print()

if __name__ == "__main__":
    get_input()
    # print(solve_1())
    print(solve_2())