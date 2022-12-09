from aocd import data,lines

def get_input():
    print(data)

def has_distinct_chars(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i] == s[j]:
                return False
    return True

def solve_1():
    marker = []
    for i in range(3,len(data)):
        if data[i] != data[i-1] and data[i] != data[i-2] and data[i] != data[i-3]:
            if data[i-1] != data[i-2] and data[i-1] != data[i-3]:
                if data[i-2] != data[i-3]:
                    print(i+1)
                    return i+1
    return -1

def solve_2():
    data = "zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw"
    for i in range(13,len(data)):
        if has_distinct_chars(data[i-13:i+1]):
            print(i+1)
            return i+1

if __name__ == "__main__":
    # get_input()
    # print(solve_1())
    print(solve_2())