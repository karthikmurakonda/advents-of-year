from aocd import get_data
import re
data = get_data(day=4,year=2021)
# split data with empty line
data = data.split('\n\n')
numbers = data[0]
data.remove(data[0])
data = [x.split('\n') for x in data]
data = [[x.split(' ') for x in y] for y in data]

# remove '' from data
data = [[[x for x in y if x != ''] for y in z] for z in data]
print(data)
markings = [[ [0 for i in range(5)] ,[0 for i in range(5)] ] for k in range(len(data))]
numbers = numbers.split(',')
print(numbers)
for i in numbers:
    for board in range(len(data)):
        for row in range(len(data[board])):
            for col in range(len(data[board][row])):
                if data[board][row][col] == str(i):
                    markings[board][0][row] += 1
                    markings[board][1][col] += 1
                    if markings[board][0][row] == 5 or markings[board][1][col] == 5:
                        # find the sum of all unmarked numbers
                        sum = 0
                        marked = numbers[0:numbers.index(i)+1]
                        for uk in range(len(data[board])):
                            for j in data[board][uk]:
                                if j not in marked:
                                    sum += int(j)
                        print(i)
                        print(data[board])
                        print(sum)
                        print(markings[board])
                        print(int(i) * (sum))
                        exit()
           
