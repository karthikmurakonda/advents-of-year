from aocd import lines, submit

def get_clsoing_index(line, start):
    """
    Get the index of the closing bracket
    line: string
    start: int
    answer: int
    """
    answer = start
    while line[answer] != "]":
        if line[answer] == "[":
            answer = get_clsoing_index(line, answer+1)
        answer += 1
    return answer

def parse_line(line):
    """
    Parse a line of input
    line: string
    answer: list
    """
    int_buffer = ""
    answer = []
    i = 0
    while i < len(line):
        if line[i] == "[":
            answer.append(parse_line(line[i+1:get_clsoing_index(line, i+1)]))
            i = get_clsoing_index(line, i+1)
        elif line[i] == ",":
            if int_buffer != "":
                answer.append(int(int_buffer))
            int_buffer = ""
        else:
            int_buffer += line[i]
        i += 1
    if int_buffer != "":
        answer.append(int(int_buffer))
    return answer


def compare(left, right):
    """
    Compare two lists
    left: list
    right: list
    answer: int
    """
    ans = None
    for i in range(min(len(left), len(right))):
        if type(left[i]) == list and type(right[i]) == list:
            ans = compare(left[i], right[i])
            if ans != None:
                return ans
        elif type(left[i]) == list:
            ans = compare(left[i], [right[i]])
            if ans != None:
                return ans
        elif type(right[i]) == list:
            ans = compare([left[i]], right[i])
            if ans != None:
                return ans
        else:
            if left[i] > right[i]:
                return False
            elif left[i] < right[i]:
                return True
    if len(left) > len(right):
        return False
    elif len(left) < len(right):
        return True
    return ans


    


def solve_1():
#     lines = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]
# """
#     lines = lines.splitlines()
    signal_data = []
    ans = 0
    num = 0
    for line in lines:
        # line = line.strip('[').strip(']')
        if line != "":
            signal_data.append(parse_line(line)[0])
        else:
            num += 1
            # compare signal_data
            left = signal_data[0]
            right = signal_data[1]
            if compare(left, right):
                ans += num
                print(num)
            signal_data = []
    return ans


def solve_2():
#     lines = """[1,1,3,1,1]
# [1,1,5,1,1]

# [[1],[2,3,4]]
# [[1],4]

# [9]
# [[8,7,6]]

# [[4,4],4,4]
# [[4,4],4,4,4]

# [7,7,7,7]
# [7,7,7]

# []
# [3]

# [[[]]]
# [[]]

# [1,[2,[3,[4,[5,6,7]]]],8,9]
# [1,[2,[3,[4,[5,6,0]]]],8,9]
# """
    global lines
    # lines = lines.splitlines()
    lines = [line for line in lines if line != ""]
    parsed_lines = [parse_line(line)[0] for line in lines]
    parsed_lines.append([[2]])
    parsed_lines.append([[6]])
    
    # sort according to the compare function
    i = 0
    j = 1
    while i < len(parsed_lines):
        while j < len(parsed_lines):
            if compare(parsed_lines[i], parsed_lines[j]):
                parsed_lines[i], parsed_lines[j] = parsed_lines[j], parsed_lines[i]
            j += 1
        i += 1
        j = i + 1
    
    print(parsed_lines)

    # search for the first [[2]] and [[6]]
    index1 = 0
    index2 = 0
    for i in range(len(parsed_lines)):
        if parsed_lines[i] == [[2]]:
            index1 = i
        if parsed_lines[i] == [[6]]:
            index2 = i
    index1 = len(parsed_lines) - index1
    index2 = len(parsed_lines) - index2
    print(index1, index2)
    return index1 * index2
    

if __name__ == "__main__":
    # print(parse_line("[[[6],[],[[]],[5,4,6,9]],[[[9,0,10],[7,2,7]],8,9,0,[[2,9,1,3,5],1,[],10,[]]],[9]]")[0])
    print(solve_1())
    print(solve_2())
    # submit(solve_1(), part="a", day=13, year=2022)
    # submit(solve_2(), part="b", day=13, year=2022)