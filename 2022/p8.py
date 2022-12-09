from aocd import lines

def solve_1():
    nums = []
    for line in lines:
        nums.append([])
        for i in range(0,len(line)):
            nums[-1].append(int(line[i]))

    visible = [[False for i in range(len(nums[0]))] for j in range(len(nums))]

    # left to right
    for i in range(1,len(nums)-1):
        max_lr = nums[i][0]
        for j in range(1,len(nums[0])-1):
            if nums[i][j] > max_lr:
                visible[i][j] = True
                max_lr = nums[i][j]

    # right to left
    for i in range(1,len(nums)-1):
        max_rl = nums[i][-1]
        for j in range(len(nums[0])-2,0,-1):
            if nums[i][j] > max_rl:
                visible[i][j] = True
                max_rl = nums[i][j]

    # top to bottom
    for j in range(1,len(nums[0])-1):
        max_tb = nums[0][j]
        for i in range(1,len(nums)-1):
            if nums[i][j] > max_tb:
                visible[i][j] = True
                max_tb = nums[i][j]

    # bottom to top
    for j in range(1,len(nums[0])-1):
        max_bt = nums[-1][j]
        for i in range(len(nums)-2,0,-1):
            if nums[i][j] > max_bt:
                visible[i][j] = True
                max_bt = nums[i][j]
    
    count = 0
    for i in range(1,len(nums)-1):
        for j in range(1,len(nums[0])-1):
            if visible[i][j]:
                count += 1
    count += 2*(len(nums)-2) + 2*(len(nums[0]))
    return count


def solve_2():

#     data = """30373
# 25512
# 65332
# 33549
# 35390
# """
#     lines = data.splitlines()
    nums = []
    for line in lines:
        nums.append([])
        for i in range(0,len(line)):
            nums[-1].append(int(line[i]))

    max_scenic_score = 0
    for i in range(0,len(nums)):
        for j in range(0,len(nums[0])):
            scenic_score_x = 0
            # left
            pos_x = i -1
            pos_y = j
            flag = True
            while pos_x >= 0 and flag:
                if nums[pos_x][pos_y] < nums[i][j]:
                    scenic_score_x += 1
                else:
                    scenic_score_x += 1
                    flag = False
                pos_x -= 1
            # right
            pos_x = i + 1
            pos_y = j
            flag = True
            scenic_score_y = 0
            while pos_x < len(nums) and flag:
                if nums[pos_x][pos_y] < nums[i][j]:
                    scenic_score_y += 1
                else:
                    scenic_score_y += 1
                    flag = False
                pos_x += 1
            # top
            pos_x = i
            pos_y = j -1
            flag = True
            scenic_score_top = 0
            while pos_y >= 0 and flag:
                if nums[pos_x][pos_y] < nums[i][j]:
                    scenic_score_top += 1
                else:
                    scenic_score_top += 1
                    flag = False
                pos_y -= 1
            # bottom
            pos_x = i
            pos_y = j + 1
            flag = True
            scenic_score_bottom = 0
            while pos_y < len(nums[0]) and flag:
                if nums[pos_x][pos_y] < nums[i][j]:
                    scenic_score_bottom += 1
                else:
                    scenic_score_bottom += 1
                    flag = False
                pos_y += 1
            scenic_score = scenic_score_x * scenic_score_y * scenic_score_top * scenic_score_bottom
            # print(scenic_score)
            if scenic_score > max_scenic_score:
                max_scenic_score = scenic_score
    return max_scenic_score
            
                

print(solve_1())
print(solve_2())