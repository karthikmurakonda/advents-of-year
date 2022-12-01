from copy import deepcopy
from aocd import get_data

def get_next_state(state):
    state = deepcopy(state)
    right_movable = []
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == '>' and state[i][(j+1)%len(state[i])] == '.':
                right_movable.append((i, j))
    for i, j in right_movable:
        state[i][j] = '.'
        state[i][(j+1)%len(state[i])] = '>'
    down_movable = []
    for i in range(len(state)):
        for j in range(len(state[i])):
            if state[i][j] == 'v' and state[(i+1)%len(state)][j] == '.':
                down_movable.append((i, j))
    for i, j in down_movable:
        state[i][j] = '.'
        state[(i+1)%len(state)][j] = 'v'
    return state

def are_same(state1, state2):
    for i in range(len(state1)):
        for j in range(len(state1[i])):
            if state1[i][j] != state2[i][j]:
                return False
    return True

data = get_data(day=25, year=2021).split('\n')

data = [[k for k in data[i]] for i in range(len(data))]

previous_state = deepcopy(data)
# print previous_state in neater format
for i in range(len(previous_state)):
    print(''.join(previous_state[i]))
print()
current_state = get_next_state(previous_state)
ans = 1
while not are_same(previous_state, current_state):
    ans += 1
    previous_state = deepcopy(current_state)
    current_state = get_next_state(previous_state)
    # print(ans)

print(ans)