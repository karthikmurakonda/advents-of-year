from collections import deque
from aocd import lines


# lines = """Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi"""
# lines = lines.splitlines()

def is_greater(pos1,pos2):
    if(lines[pos1[0]][pos1[1]] == "S" and lines[pos2[0]][pos2[1]] == "a"):
        return True
    elif lines[pos1[0]][pos1[1]] == "z" and lines[pos2[0]][pos2[1]] == "E":
        return True
    if ord(lines[pos1[0]][pos1[1]]) +1 >= ord(lines[pos2[0]][pos2[1]]) and lines[pos2[0]][pos2[1]] != "S" and lines[pos2[0]][pos2[1]] != "E":
        return True
    return False

def is_adjacent(pos1, pos2):
    if pos2[0] >= 0 and pos2[0] < len(lines) and pos2[1] >= 0 and pos2[1] < len(lines[0]):
        if is_greater(pos1,pos2):
            return True
    return False


def solve_1():
    s_pos = [0,0]
    e_pos = [0,0]
    # set s_pos and e_pos
    for i in range(len(lines)):
        for j in range(len(lines[i])):
            if lines[i][j] == 'E':
                e_pos = [i,j]
            elif lines[i][j] == 'S':
                s_pos = [i,j]
    min_distance = int(1e9)
    for on in range(len(lines)):
        s_pos[0] = on
        visited = [[-1 for i in range(len(lines[0]))] for _ in range(len(lines))]
        visited[s_pos[0]][s_pos[1]] = 0
        distance = 0
        q = deque([s_pos])
        while len(q):
            distance += 1
            times = len(q)
            for _ in range(times):
                pos = q.popleft()
                for i in range(-1,2):
                    for j in range(-1,2):
                        if not(i == 0 or j == 0) or i == j:
                            continue
                        new_pos = [pos[0]+i,pos[1]+j]
                        if is_adjacent(pos,new_pos) and visited[new_pos[0]][new_pos[1]] == -1:
                            if new_pos == e_pos:
                                min_distance = min(min_distance,distance)
                            visited[new_pos[0]][new_pos[1]] = distance
                            q.append(new_pos)
    if min_distance != int(1e9):
        return min_distance
    return -1

print(solve_1())