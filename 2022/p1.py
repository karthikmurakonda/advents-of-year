from aocd import lines, submit

sum_list = []
cur_sum = 0
for i in range(len(lines)):
	if lines[i] == '':
		sum_list.append(cur_sum)
		cur_sum = 0
	else:
		cur_sum += int(lines[i])
sum_list.sort()
submit(sum_list[-1]+sum_list[-2]+sum_list[-3])
