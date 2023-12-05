from aocd import lines,submit

def manhattan_distance(t1,t2):
    return abs(t1[0]-t2[0])+abs(t1[1]-t2[1])

def extremes_on_x(t1, y1 , max_dist):
    if t1[1] - y1 < max_dist:
        return sorted([t1[0]-(max_dist-abs(t1[1]-y1)), t1[0]+(max_dist-abs(t1[1]-y1))])
    return

def inject_range(ranges, new_range):
    for i in range(len(ranges)):
        if ranges[i][0] <= new_range[0] and ranges[i][1] >= new_range[1]:
            return
        elif ranges[i][0] <= new_range[0] and ranges[i][1] >= new_range[0]:
            ranges[i] = [ranges[i][0], new_range[1]]
            return
        elif ranges[i][0] <= new_range[1] and ranges[i][1] >= new_range[1]:
            ranges[i] = [new_range[0], ranges[i][1]]
            return
        elif ranges[i][0] >= new_range[0] and ranges[i][1] <= new_range[1]:
            ranges[i] = new_range
            return
    ranges.append(new_range)
    return

def merge_ranges(ranges):
    ranges = sorted(ranges)
    i = 0
    while i < len(ranges)-1:
        if ranges[i][1] >= ranges[i+1][0]:
            ranges[i] = (ranges[i][0], max(ranges[i][1], ranges[i+1][1]))
            ranges.pop(i+1)
        else:
            i += 1
    return ranges

def solve_1():
#     lines ="""Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""
#     lines = lines.splitlines()
    sources = []
    beacons = []
    for i in lines:
        _, _, s1, s2, _, _, _, _, b1, b2 = i.split(" ")
        s1 = int(s1.strip(',').split("=")[1])
        s2 = int(s2.strip(':').split("=")[1])
        b1 = int(b1.strip(',').split("=")[1])
        b2 = int(b2.strip(':').split("=")[1])
        sources.append((s1,s2))
        beacons.append((b1,b2))
    for y in range(3000000):
        ranges = []
        new_range = []
        for i in range(len(sources)):
            distance = manhattan_distance(sources[i],beacons[i])
            if abs(sources[i][1]-y) < distance:
                new_range = extremes_on_x(sources[i], y, distance)
                inject_range(ranges, new_range)
            elif abs(sources[i][1]-y) == distance:
                new_range = [sources[i][0], sources[i][0]]
                inject_range(ranges, new_range)
        ranges = merge_ranges(ranges)

        count = 0
        for i in ranges:
            count += i[1]-i[0]+1
        y_beacons =set()
        for i in beacons:
            if i[1] == y:
                y_beacons.add(i)
        for i in y_beacons:
            for j in ranges:
                if i[0] >= j[0] and i[0] <= j[1]:
                    count -= 1
                    break
        # print(ranges,y)
        possible_answer = []
        if(ranges[0][1] <= 4000000 or len(ranges) > 1):
            for i in ranges:
                possible_answer.append(i[1])
            # print(possible_answer)
            return min(possible_answer)

            
    return count

    

def solve_2():
    pass

if __name__ == "__main__":
    print(solve_1())
    # print(solve_2())