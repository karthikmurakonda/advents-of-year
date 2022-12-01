from aocd import get_data

data = get_data(day=8, year=2021).split('\n')

data = [data[i].split(' ') for i in range(len(data))]
ans = 0
for i in range(len(data)):
    decode = 0
    for j in range(-4, 0,1):
        data[i][j] = [data[i][j][k] for k in range(len(data[i][j]))]
        # print(data[i][j])
        print(data[i][j])
        decode = 10 * decode
        if len(data[i][j]) == 2:
            decode += 1
        elif len(data[i][j]) == 3:
            decode += 7
        elif len(data[i][j]) == 4:
            decode += 4
        elif len(data[i][j]) == 7:
            decode += 8
        elif len(data[i][j]) == 6:
            if not 'g' in data[i][j]:
                decode += 9
            elif not 'a' in data[i][j]:
                decode += 6
            elif not 'f' in data[i][j]:
                decode += 0
        else:
            if 'e' in data[i][j]:
                decode += 5
            elif 'g' in data[i][j]:
                decode += 2
            else:
                decode += 3
    ans += decode
         
print(ans)