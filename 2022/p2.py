from aocd import lines,submit

ans = 0
for line in lines:
	[op,me] = line.split(" ")
	opnum = ord(op)-ord('A')
	menum = ord(me)-ord('X')
	ans += menum * 3
	ans += 1
	if menum == 1:
		ans += opnum
	elif menum == 0:
		ans += (opnum-1)%3
	else:
		ans += (opnum+1)%3
submit(ans)
