from aocd import lines

def are_adjacent(co_ord_1, co_ord_2):
    if co_ord_1[0] == co_ord_2[0] and abs(co_ord_1[1] - co_ord_2[1]) == 1:
        return True
    elif co_ord_1[1] == co_ord_2[1] and abs(co_ord_1[0] - co_ord_2[0]) == 1:
        return True
    elif abs(co_ord_1[0] - co_ord_2[0]) == 1 and abs(co_ord_1[1] - co_ord_2[1]) == 1:
        return True
    elif co_ord_1[0] == co_ord_2[0] and co_ord_1[1] == co_ord_2[1]:
        return True
    return False

def get_next(co_ord1, co_ord2):
    ret = co_ord1.copy()
    if co_ord1[0] == co_ord2[0]:
        if co_ord1[1]+ 1 < co_ord2[1]:
            ret[1] += 1
        elif co_ord1[1] - 1 > co_ord2[1]:
            ret[1] -= 1
    elif co_ord1[1] == co_ord2[1]:
        if co_ord1[0]+ 1 < co_ord2[0]:
            ret[0] += 1
        elif co_ord1[0] - 1 > co_ord2[0]:
            ret[0] -= 1
    else:
        if co_ord2[0] < co_ord1[0] and co_ord2[1] < co_ord1[1] and not (co_ord1[0]==co_ord2[0]+1 and co_ord1[1] == co_ord2[1]+1):
            ret[0]-=1
            ret[1]-=1
        elif co_ord2[0] < co_ord1[0] and co_ord2[1] > co_ord1[1] and not (co_ord1[0]==co_ord2[0]+1 and co_ord1[1] == co_ord2[1]-1):
            ret[0]-=1
            ret[1]+=1
        elif co_ord2[0] > co_ord1[0] and co_ord2[1] > co_ord1[1] and not (co_ord1[0]==co_ord2[0]-1 and co_ord1[1] == co_ord2[1]-1):
            ret[0]+=1
            ret[1]+=1
        elif co_ord2[0] > co_ord1[0] and co_ord2[1] < co_ord1[1] and not (co_ord1[0]==co_ord2[0]-1 and co_ord1[1] == co_ord2[1]+1):
            ret[0]+=1
            ret[1]-=1
    return ret

def solve_1():
#     lines = """R 4
# U 4
# L 3
# D 1
# R 4
# D 1
# L 5
# R 2
# """
    # lines = lines.splitlines()
    co_ord = {}
    co_ord['T'] = [0,0]
    co_ord['H'] = [0,0]
    t_visited = {}
    t_visited[tuple(co_ord['T'])] = True
    for line in lines:
        symbol , stes = line[0] , int(line[2:])
        if symbol == "R":
            co_ord['H'][0] += stes
            if not are_adjacent(co_ord['T'], co_ord['H']):
                co_ord['T'][1]  = co_ord['H'][1]
                while co_ord['T'][0] < co_ord['H'][0]-1:
                    co_ord['T'][0] += 1
                    t_visited[tuple(co_ord['T'])] = True
            t_visited[tuple(co_ord['T'])] = True
        elif symbol == "L":
            co_ord['H'][0] -= stes
            if not are_adjacent(co_ord['T'], co_ord['H']):
                co_ord['T'][1]  = co_ord['H'][1]
                while co_ord['T'][0] > co_ord['H'][0]+1:
                    co_ord['T'][0] -= 1
                    t_visited[tuple(co_ord['T'])] = True
            t_visited[tuple(co_ord['T'])] = True
        elif symbol == "U":
            co_ord['H'][1] += stes
            if not are_adjacent(co_ord['T'], co_ord['H']):
                co_ord['T'][0] = co_ord['H'][0]
                while co_ord['T'][1] < co_ord['H'][1]-1:
                    co_ord['T'][1] += 1
                    t_visited[tuple(co_ord['T'])] = True
            t_visited[tuple(co_ord['T'])] = True
        elif symbol == "D":
            co_ord['H'][1] -= stes
            if not are_adjacent(co_ord['T'], co_ord['H']):
                co_ord['T'][0] = co_ord['H'][0]
                while co_ord['T'][1] > co_ord['H'][1]+1:
                    co_ord['T'][1] -= 1
                    t_visited[tuple(co_ord['T'])] = True
            t_visited[tuple(co_ord['T'])] = True
    print(len(t_visited))

def solve_2():
#     lines = """R 5
# U 8
# L 8
# D 3
# R 17
# D 10
# L 25
# U 20"""
#     lines = lines.splitlines()
    co_ord = {}
    for i in range(10):
        co_ord[i] = [0,0]
    t_visited = {}
    t_visited[tuple(co_ord[0])] = True
    for line in lines:
        symbol, num = line.split(" ")
        for _ in range(int(num)):
            if symbol == "R":
                co_ord[9][0]+=1
            elif symbol == "L":
                co_ord[9][0]-=1
            elif symbol == "U":
                co_ord[9][1]+=1
            else:
                co_ord[9][1]-=1
            for i in range(8,-1,-1):
                co_ord[i] = get_next(co_ord1=co_ord[i],co_ord2=co_ord[i+1])
            t_visited[tuple(co_ord[0])] = True
    print(len(t_visited))

if __name__ == "__main__":
    solve_1()
    solve_2()
    # print(get_next([1,1],[1,0]))
