from aocd import data
# find number of integers in the input that are greater than their previous number
count = 0
for i in range(len(data)):
    if i == 0:
        continue
    elif data[i] > data[i-1]:
        count += 1
print(count)
