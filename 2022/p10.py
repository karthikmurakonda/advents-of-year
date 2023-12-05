from aocd import lines,data

def solve_1():
    clockx = [1]
    for i in range(len(lines)):
        if lines[i][0] == "a":
            value = int(lines[i].split(" ")[1])
            clockx.append(clockx[-1])
            clockx.append(clockx[-1]+value)
        else:
            clockx.append(clockx[-1])
    sum = 0
    for i in range(6):
        sum += clockx[20+40*i-1]*(20+40*i)
    print(sum)

def solve_2():
    clockx = [1]
    for i in range(len(lines)):
        if lines[i][0] == "a":
            value = int(lines[i].split(" ")[1])
            clockx.append(clockx[-1])
            clockx.append(clockx[-1]+value)
        else:
            clockx.append(clockx[-1])
    crt_screen = [['.' for i in range(40)] for i in range(6)]
    for i in range(len(clockx)):
        if(abs(clockx[i]-(i%40))<=1):
            crt_screen[i//40][i%40] = '#'
    for i in crt_screen:
        print(i)




solve_2()