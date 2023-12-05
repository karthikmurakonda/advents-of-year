from aocd import data


rocks = [[[0,0],[0,1],[0,2],[0,3]],
        [[0,0],[1,-1],[1,0],[1,1]],
        [[0,0],[1,0],[2,0],[2,-1],[2,-2]],
        [[0,0],[1,0],[2,0],[3,0]],
        [[0,0],[1,0],[0,1],[1,1]]]


def rock_to_grid(rock):
    max_y = 0
    for i in range(len(rock)):
        if rock[i][0] > max_y:
            max_y = rock[i][0]
    grid = [[False for _ in range(max_y+1)] for _ in range(max_y+1)]
    for i in range(len(rock)):
        grid[rock[i][0]][rock[i][1]] = True
    return grid


def solve_1():
    grid = [[False for _ in range(7)] for _ in range(4)]
    for i in range(len(rocks)):
    


def solve_2():
    pass

if __name__ == "__main__":
    print(solve_1())
    print(solve_2())