from aocd import get_data
import re
import copy
lines = ["Blueprint 1: Each ore robot costs 4 ore. Each clay robot costs 2 ore. Each obsidian robot costs 3 ore and 14 clay. Each geode robot costs 2 ore and 7 obsidian."]
# lines = ["Blueprint 2:   Each ore robot costs 2 ore.   Each clay robot costs 3 ore.   Each obsidian robot costs 3 ore and 8 clay.   Each geode robot costs 3 ore and 12 obsidian."]

class Requirement:
    def __init__(self, ore, clay, obsdian):
        self.ore_req : int = int(ore)
        self.clay_req : int = int(clay)
        self.obsdian_req : int = int(obsdian)
    
    def __str__(self):
        return f"Ore: {self.ore_req}, Clay: {self.clay_req}, Obsdian: {self.obsdian_req}"

class Blueprint:
    def __init__(self, ore_bot_req, clay_bot_req, obsdian_bot_req, geode_bot_req):
        self.ore_req: Requirement = ore_bot_req
        self.clay_req : Requirement = clay_bot_req
        self.obsdian_req : Requirement = obsdian_bot_req
        self.geode_req : Requirement = geode_bot_req

    def __str__(self):
        return f"Ore: {self.ore_req}, Clay: {self.clay_req}, Obsdian: {self.obsdian_req}, Geode: {self.geode_req}"

class Inventory:
    def __init__(self):
        self.ore = 0
        self.clay = 0
        self.obsdian = 0
        self.geode = 0
        self.ore_bots = 1
        self.clay_bots = 0
        self.obsdian_bots = 0
        self.geode_bots = 0

    def function_bots(self):
        self.ore += self.ore_bots
        self.clay += self.clay_bots
        self.obsdian += self.obsdian_bots
        self.geode += self.geode_bots

    def __str__(self):
        return f"Ore: {self.ore}, Clay: {self.clay}, Obsdian: {self.obsdian}, Geode: {self.geode} bots: ({self.ore_bots}, {self.clay_bots}, {self.obsdian_bots}, {self.geode_bots})"

def parseBlueprint(lines):
    blueprints = []
    for line in lines:
        res = re.findall(r'(\d+)', line)
        ore_bot_req = Requirement(res[1], 0, 0)
        clay_bot_req = Requirement(res[2], 0, 0)
        obsdian_bot_req = Requirement(res[3], res[4], 0)
        geode_bot_req = Requirement(res[5], 0, res[6])
        blueprints.append(Blueprint(ore_bot_req, clay_bot_req, obsdian_bot_req, geode_bot_req))
    return blueprints

cache = {}

def integer_seq_sum(a, b):
    return ((a+b)*(b-a))//2

p1_ans = 0
def max_geodes(CurrInventory: Inventory, blueprint:Blueprint, timeLeft: int) -> int:
    CurrInventory = copy.copy(CurrInventory)
    pre_ore = CurrInventory.ore
    pre_clay = CurrInventory.clay
    pre_obsdian = CurrInventory.obsdian
    pre_geode = CurrInventory.geode
    pre_ore_bots = CurrInventory.ore_bots
    pre_clay_bots = CurrInventory.clay_bots
    pre_obsdian_bots = CurrInventory.obsdian_bots
    global p1_ans
    # print(CurrInventory, "\n", timeLeft, p1_ans)
    if CurrInventory.geode +  integer_seq_sum(CurrInventory.geode_bots, timeLeft+CurrInventory.geode_bots) < p1_ans:
        return 0
    key = (CurrInventory.ore, CurrInventory.clay, CurrInventory.obsdian, CurrInventory.geode, CurrInventory.ore_bots, CurrInventory.clay_bots, CurrInventory.obsdian_bots, CurrInventory.geode_bots, timeLeft)
    if key in cache:
        return cache[key]
    CurrInventory.function_bots()
    if timeLeft == 0:
        return CurrInventory.geode
    else:
        ret = 0
        if pre_ore >= blueprint.geode_req.ore_req and pre_obsdian >= blueprint.geode_req.obsdian_req:
            CurrInventory.ore -= blueprint.geode_req.ore_req
            CurrInventory.obsdian -= blueprint.geode_req.obsdian_req
            CurrInventory.geode_bots += 1
            p1_ans = max(p1_ans, ret)
            ret = max(ret, max_geodes(CurrInventory, blueprint, timeLeft-1))
            CurrInventory.ore += blueprint.geode_req.ore_req
            CurrInventory.obsdian += blueprint.geode_req.obsdian_req
            CurrInventory.geode_bots -= 1
        if CurrInventory.geode_bots >= blueprint.geode_req.ore_req and CurrInventory.obsdian_bots >= blueprint.geode_req.obsdian_req:
            return ret
        if pre_ore >= blueprint.obsdian_req.ore_req and pre_clay >= blueprint.obsdian_req.clay_req:
            CurrInventory.ore -= blueprint.obsdian_req.ore_req
            CurrInventory.clay -= blueprint.obsdian_req.clay_req
            CurrInventory.obsdian_bots += 1
            p1_ans = max(p1_ans, ret)
            ret = max(ret, max_geodes(CurrInventory, blueprint, timeLeft-1))
            CurrInventory.ore += blueprint.obsdian_req.ore_req
            CurrInventory.clay += blueprint.obsdian_req.clay_req
            CurrInventory.obsdian_bots -= 1
        if pre_ore >= blueprint.clay_req.ore_req:
            CurrInventory.ore -= blueprint.clay_req.ore_req
            CurrInventory.clay_bots += 1
            p1_ans = max(p1_ans, ret)
            ret = max(ret, max_geodes(CurrInventory, blueprint, timeLeft-1))
            CurrInventory.clay_bots -= 1
            CurrInventory.ore += blueprint.clay_req.ore_req
        if pre_ore >= blueprint.ore_req.ore_req:
            CurrInventory.ore -= blueprint.ore_req.ore_req
            CurrInventory.ore_bots += 1
            p1_ans = max(p1_ans, ret)
            ret = max(ret, max_geodes(CurrInventory, blueprint, timeLeft-1))
            CurrInventory.ore_bots -= 1
            CurrInventory.ore += blueprint.ore_req.ore_req
        ret = max(ret, max_geodes(CurrInventory, blueprint, timeLeft-1))
        cache[key] = ret
        p1_ans = max(p1_ans, ret)
        return ret



def solve_1():
    bluprints = parseBlueprint([lines[0]])
    for bl in bluprints:
        print(max_geodes(Inventory(),bl, 24))
    

def solve_2():
    blueprint = parseBlueprint(lines)
    return 0

print(solve_1())
print(solve_2())