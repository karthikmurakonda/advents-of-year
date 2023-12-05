from aocd import lines,submit
minx = 100000
maxx = 0
miny = 100000
maxy = 0
grid = []

def transform_coords(x,y):
    return x, y


def placeit(source_x,source_y):
    global grid
    if grid[source_y][source_x] == "o":
        return False
    while source_y < len(grid)-1 and source_x >= 0 and source_x < len(grid[0]):
        if grid[source_y+1][source_x] == " ":
            source_y += 1
        elif source_x>0 and grid[source_y+1][source_x-1] == " ":
            source_x -= 1
            source_y += 1
        elif source_x < len(grid[0])-1 and grid[source_y+1][source_x+1] == " ":
            source_x += 1
            source_y += 1
        else:
            return source_x,source_y
        
    return False


def part1(data):
    global minx,maxx,miny,maxy,grid
    source = [500,0]
    walls = []
    for i in data:
        temp = i.split("->")
        temp = [list(map(int, x.split(","))) for x in temp]
        walls.append(temp)
        minx = min([minx]+[x[0] for x in temp])
        maxx = max([maxx]+[x[0] for x in temp])
        miny = min([miny]+[x[1] for x in temp])
        maxy = max([maxy]+[x[1] for x in temp])

    for i in walls:
        for j in i:
            j[0],j[1] = transform_coords(j[0],j[1])
    source[0],source[1] = transform_coords(source[0],source[1])
    print(walls)
    print(source)

    print(minx,maxx,miny,maxy)
    grid = [[" " for i in range(1000)] for j in range(maxy+3)]
    for i in range(len(walls)):
        for j in range(1,len(walls[i])):
            for k in range(min(walls[i][j-1][0],walls[i][j][0]),max(walls[i][j-1][0],walls[i][j][0])+1):
                grid[walls[i][j][1]][k] = "#"
            for k in range(min(walls[i][j-1][1],walls[i][j][1]),max(walls[i][j-1][1],walls[i][j][1])+1):
                grid[k][walls[i][j][0]] = "#"
    for i in range(1000):
        grid[maxy+2][i] = "#"
    grid[source[1]][source[0]] = "+"
    ans = 0
    while True:
        res = placeit(source[0],source[1])
        if res == False:
            break
        else:
            grid[res[1]][res[0]] = "o"
            ans += 1

    return ans

    # for i in range(len(grid)):
    #     print("".join(grid[i]))
    # return 0


            

def part2(data):
    return 0

data =lines

# submit(part1(data), part="a", day=14, year=2022)
submit(part1(data), part="b", day=14, year=2022)
print(part1(data))
print(part2(data))