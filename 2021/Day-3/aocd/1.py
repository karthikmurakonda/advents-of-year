# open in input.txt
with open('input.txt', 'r') as f:
    a = ""
    b = ""
    # break each line into a list of str
    lines = []
    for line in f:
        lines.append(line)
    for i in range(len(lines[0])-1):
        tempa = ""
        for line in lines:
            tempa += line[i]
        # count 0 and 1
        if tempa.count("0") > tempa.count("1"):
            a += "0"
            b += "1"
        else:
            a += "1"
            b += "0"
print(a)
print(b)