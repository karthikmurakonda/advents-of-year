from aocd import lines, submit

def solve_1():
    ans = 0
    for line in lines:
        firsthalf = line[:len(line)//2]
        secondhalf = line[len(line)//2:]
        for i in range(0,len(firsthalf),3):
            if firsthalf[i] in secondhalf:
                # small alphabet
                if firsthalf[i].islower():
                    ans += ord(firsthalf[i]) - 96
                # capital alphabet
                else:
                    ans += ord(firsthalf[i]) - 64 + 26
                # ans += ord(firsthalf[i]) - ord('a') + 1
                break
    return ans
                

def solve_2():
    ans = 0
    for i in range(0,len(lines),3):
        for j in range(len(lines[i])):
            if lines[i][j]in lines[i+1] and lines[i][j] in lines[i+2]:
                if lines[i][j].islower():
                    ans += ord(lines[i][j]) - 96
                else:
                    ans += ord(lines[i][j]) - 64 + 26
                break
    return ans

if __name__ == "__main__":
    print(solve_1())
    print(solve_2())
    submit(solve_2())