from math import inf
from typing import List, Any

from aocd import submit


def solve_1():
    lines: list[str,int,list[str]] = []
    with open("2022/input.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            valve:str = lines[i].split(" ")[1]
            rate:int = int(lines[i].split(" ")[4].strip(";").split("=")[1])
            neighbors:list[str] = []
            for j in range(9, len(lines[i].split(" "))):
                neighbors.append(lines[i].split(" ")[j].strip(",").strip("\n"))
            lines[i] = [valve, rate, neighbors]
    sorted_lines = sorted(lines, key=lambda x: x[0])
    valves = {}
    index = 0
    for i in range(len(sorted_lines)):
        valves[sorted_lines[i][0]] = [index, sorted_lines[i][1], sorted_lines[i][2]]
        index += 1
    distances = []
    for i in range(len(sorted_lines)):
        distances.append([inf] * len(sorted_lines))
    for i in range(len(sorted_lines)):
        distances[i][i] = 0
    for i in range(len(sorted_lines)):
        for j in range(len(sorted_lines)):
            if sorted_lines[i][0] in sorted_lines[j][2]:
                distances[i][j] = 1
    for i in range(len(sorted_lines)):
        for j in range(len(sorted_lines)):
            for k in range(len(sorted_lines)):
                if distances[j][k] > distances[j][i] + distances[i][k]:
                    distances[j][k] = distances[j][i] + distances[i][k]
    
            




def solve_2():
    pass


if __name__ == "__main__":
    print(solve_1())
    print(solve_2())