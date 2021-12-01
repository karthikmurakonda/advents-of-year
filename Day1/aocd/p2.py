from aocd import get_data
data = get_data(day=1, year=2021).splitlines()
sum_arr = []
count = 0
for i in range(len(data)):
    if i>= 2:
        sum_arr.append(data[i] + data[i-1] + data[i-2])
for i in range(len(sum_arr)):
    if sum_arr[i] > sum_arr[i-1]:
        count+=1
print(count)