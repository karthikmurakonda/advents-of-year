def recfuncO2(lines,i):
    zeroes = []
    ones = []
    if len(lines) == 1:
        return lines[0]
    for line in lines:
        if line[i] == '0':
            zeroes.append(line)
        else:
            ones.append(line)
    if len(zeroes) > len(ones):
        return recfuncO2(zeroes, i+1)
    else:
        return recfuncO2(ones, i+1)

def recfuncCo2(lines,i):
    zeroes = []
    ones = []
    if len(lines) == 1:
        return lines[0]
    for line in lines:
        if line[i] == '0':
            zeroes.append(line)
        else:
            ones.append(line)
    if len(zeroes) > len(ones):
        return recfuncCo2(ones, i+1)
    else:
        return recfuncCo2(zeroes, i+1)

with open('input.txt', 'r') as f:
    lines = []
    for line in f:
        lines.append(line)
    print(recfuncO2(lines,0))
    print(recfuncCo2(lines,0))