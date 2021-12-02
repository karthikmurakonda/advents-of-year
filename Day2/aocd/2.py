with open('input.txt', 'r') as f:
    data = f.read()
    # each line has up/down or forward and a number
    # split lines into a list of lists
    data = data.split('\n')
    # see the string up/down or forward and convert to int
    # then add to list of lists
    aim = 0
    ver = 0
    hor = 0
    for i in range(len(data)):
        ans = data[i].split(' ')
        if ans[0] == 'up':
            aim -= int(ans[1])
        elif ans[0] == 'down':
            aim += int(ans[1])
        elif ans[0] == 'forward':
            hor += int(ans[1])
            ver += aim*int(ans[1])
print(ver*hor)