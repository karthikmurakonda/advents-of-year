n = int(input())

timemap = {}
for i in range(n):
    x,y, t, s = input().split()
    x = int(x)
    y = int(y)
    t = int(t)
    s = int(s)
    if t in timemap:
        timemap[t].append((x,y,s))
    else:
        timemap[t] = [(x,y,s)]

max_score = {}

for timei in timemap:
    max_score[timei] = max([i[2] for i in timemap[timei]])

for timei in timemap:
    for timej in timemap:
        if timej <= timei:
            continue
        for i in timemap[timei]:
            for j in timemap[timej]:
                if abs(i[0]-j[0]) + abs(i[1]-j[1]) <= timej - timei:
                    max_score[timej] = max(max_score[timej], i[2]+j[2])
                    
print(max(max_score.items(), key=lambda x: x[1])[1])