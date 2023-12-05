from aocd import lines
import sys

sys.setrecursionlimit(10000)

# lines = """2,2,2
# 1,2,2
# 3,2,2
# 2,1,2
# 2,3,2
# 2,2,1
# 2,2,3
# 2,2,4
# 2,2,6
# 1,2,5
# 3,2,5
# 2,1,5
# 2,3,5"""

# lines = lines.splitlines()

def solve_1():
    grid_3d = [[[False for _ in range(20)] for _ in range(20)] for _ in range(20)]
    sides_uncovered = 0
    for line in lines:
        x, y, z = map(int, line.split(','))
        grid_3d[x][y][z] = True
        sides_uncovered += 6
        if x > 0 and grid_3d[x-1][y][z]:
            sides_uncovered -= 2
        if x < 19 and grid_3d[x+1][y][z]:
            sides_uncovered -= 2
        if y > 0 and grid_3d[x][y-1][z]:
            sides_uncovered -= 2
        if y < 19 and grid_3d[x][y+1][z]:
            sides_uncovered -= 2
        if z > 0 and grid_3d[x][y][z-1]:
            sides_uncovered -= 2
        if z < 19 and grid_3d[x][y][z+1]:
            sides_uncovered -= 2
    return sides_uncovered

def solve_2():
    grid_3d = [[[False for _ in range(21)] for _ in range(21)] for _ in range(21)]
    sides_uncovered = 0
    for line in lines:
        x, y, z = map(int, line.split(','))
        grid_3d[x][y][z] = True
    visited = [[[False for _ in range(21)] for _ in range(21)] for _ in range(21)]
    def bfs(x, y, z):
        if x < 0 or x > 20 or y < 0 or y > 20 or z < 0 or z > 20 or visited[x][y][z] or grid_3d[x][y][z]:
            return
        visited[x][y][z] = True
        bfs(x-1, y, z)
        bfs(x+1, y, z)
        bfs(x, y-1, z)
        bfs(x, y+1, z)
        bfs(x, y, z-1)
        bfs(x, y, z+1)
    bfs(0, 0, 0)
    for x in range(21):
        for y in range(21):
            for z in range(21):
                if grid_3d[x][y][z]:
                    if x == 0:
                        sides_uncovered += 1
                    if y == 0:
                        sides_uncovered += 1
                    if z == 0:
                        sides_uncovered += 1
                    if x > 0 and visited[x-1][y][z]:
                        sides_uncovered += 1
                    if x < 20 and visited[x+1][y][z]:
                        sides_uncovered += 1
                    if y > 0 and visited[x][y-1][z]:
                        sides_uncovered += 1
                    if y < 20 and visited[x][y+1][z]:
                        sides_uncovered += 1
                    if z > 0 and visited[x][y][z-1]:
                        sides_uncovered += 1
                    if z < 20 and visited[x][y][z+1]:
                        sides_uncovered += 1
    return sides_uncovered

print(solve_1())
print(solve_2())