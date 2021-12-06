from aocd import get_data

data = get_data(day=6, year=2021).split('\n')

p=[0]*9
for f in data[0].split(','):p[int(f)]+=1
def ans(t):
    for i in range(t):
        p=p[1:7]+[p[0]+p[7],p[8],p[0]]
    print(sum(p))
ans(81)
ans(256)


