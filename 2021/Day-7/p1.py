from aocd import get_data

data = get_data(day=7, year=2021)

data = data.split(',')
data = [int(i) for i in data]

minimum = min(data)
maximum = max(data)

def get_fuel(final_position):
    fuel = 0
    for i in range(len(data)):
        fuel +=  abs(final_position - data[i]) * (abs(final_position - data[i])+1)//2
    return fuel

position = minimum
# Find the minimum position by binary search


print(get_fuel(position))
