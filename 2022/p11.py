from aocd import submit
from collections import deque

factors = [19,2,3,17,13,7,5,11]
mul = 1
for i in factors:
    mul *= i
# mul = 23 * 19 * 13 * 17

class Monkey:
    def __init__(self, initial_list:list[int],divisibility:int, optype:int, opnum:int = None) -> None:
        self.items:deque = deque(initial_list)
        self.divisibility = divisibility
        self.optype = optype
        self.opnum = opnum
        self.inspect_times = 0
        self.true_monkey:Monkey = None
        self.false_monkey:Monkey = None

    def inspect(self):
        for i in range(len(self.items)):
            self.inspect_times+=1
            if self.optype == 0:
                self.items[i] += self.opnum
            elif self.optype == 1:
                self.items[i] *= self.opnum
            else:
                self.items[i] *= self.items[i]
            # self.items[i] = self.items[i]//3
            self.items[i] = self.items[i]%mul
        #     print(self.items[i])
        # print()
    def testnpass(self):
        while len(self.items):
            element = self.items.popleft()
            if element% self.divisibility:
                self.false_monkey.items.append(element)
            else:
                self.true_monkey.items.append(element)

monkeys:list[Monkey] = []

# test

# monkeys.append(Monkey([79, 98],23,1,19))
# monkeys.append(Monkey([54, 65, 75, 74],19,0,6))
# monkeys.append(Monkey([79, 60, 97],13,2))
# monkeys.append(Monkey([74],17,0,3))

monkeys.append(Monkey([74, 73, 57, 77, 74],19,1,11))
monkeys.append(Monkey([99, 77, 79],2,0,8))
monkeys.append(Monkey([64, 67, 50, 96, 89, 82, 82],3,0,1))
monkeys.append(Monkey([88],17,1,7))
monkeys.append(Monkey([80, 66, 98, 83, 70, 63, 57, 66],13,0,4))
monkeys.append(Monkey([81, 93, 90, 61, 62, 64],7,0,7))
monkeys.append(Monkey([69, 97, 88, 93],5,2))
monkeys.append(Monkey([59, 80],11,0,6))

# test

# monkeys[0].true_monkey = monkeys[2]
# monkeys[0].false_monkey = monkeys[3]

# monkeys[1].true_monkey = monkeys[2]
# monkeys[1].false_monkey = monkeys[0]

# monkeys[2].true_monkey = monkeys[1]
# monkeys[2].false_monkey = monkeys[3]

# monkeys[3].true_monkey = monkeys[0]
# monkeys[3].false_monkey = monkeys[1]


monkeys[0].true_monkey = monkeys[6]
monkeys[0].false_monkey = monkeys[7]

monkeys[1].true_monkey = monkeys[6]
monkeys[1].false_monkey = monkeys[0]

monkeys[2].true_monkey = monkeys[5]
monkeys[2].false_monkey = monkeys[3]

monkeys[3].true_monkey = monkeys[5]
monkeys[3].false_monkey = monkeys[4]

monkeys[4].true_monkey = monkeys[0]
monkeys[4].false_monkey = monkeys[1]

monkeys[5].true_monkey = monkeys[1]
monkeys[5].false_monkey = monkeys[4]

monkeys[6].true_monkey = monkeys[7]
monkeys[6].false_monkey = monkeys[2]

monkeys[7].true_monkey = monkeys[2]
monkeys[7].false_monkey = monkeys[3]

for _ in range(10000):
    print(_)
    for i in monkeys:
        i.inspect()
        i.testnpass()
times = []
for i in monkeys:
    times.append(i.inspect_times)
times.sort()
submit(times[-2]*times[-1])







