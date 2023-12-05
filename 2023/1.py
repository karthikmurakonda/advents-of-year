from aocd import data

lines = data.splitlines()
# with open("input.txt", "r") as f :
#     lines = f.readlines()
ans = 0
mp = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

def isnumber(s) :
    # print(s)
    for k in mp.keys() :
        if s.startswith(k) :
            return True, mp[k]

for i in range(len(lines)) :
    cal = 0
    for j in range(len(lines[i])) :
        if isnumber(lines[i][j:]):
            cal += isnumber(lines[i][j:])[1]*10
            break
        if lines[i][j].isnumeric() :
            cal += int(lines[i][j])*10
            break
    for j in reversed(range(len(lines[i]))) :
        if isnumber(lines[i][j:]):
            cal += isnumber(lines[i][j:])[1]
            break
        if lines[i][j].isnumeric() :
            cal += int(lines[i][j])
            break
    print(cal)
    ans += cal

# for line in lines :
#     cal = 0 
#     for c in line :
#         if c.isnumeric() :
#             cal += int(c)*10
#             break
#     for c in reversed(line) :
#         if c.isnumeric() :
#             cal += int(c)
#             break
#     print(line, cal)
#     ans += cal
    # print(cal)
print(ans)
    