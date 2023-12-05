from aocd import data

lines = data.splitlines()
last_line = lines[-1]
lines.pop()
print(len(lines))
max_len = 0
for l in lines:
    max_len = max(max_len, len(l))
print(max_len)
print(len(last_line))