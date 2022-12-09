from aocd import lines

class file_directory():
    def __init__(self,name, parent = None):
        self.name = name
        self.size = 0
        self.children = []
        self.files_size = 0
        self.parent = parent
    
    def add_child(self,child):
        self.children.append(child)
    
    def add_file(self,file):
        self.files_size += file
    
    def caluclate_size(self):
        self.size = self.files_size
        for child in self.children:
            self.size += child.caluclate_size()
        return self.size


def directory_with_atmost_100000_size(current_dir):
    count = 0
    if current_dir.size < 100000:
        count += current_dir.size
    for child in current_dir.children:
        count += directory_with_atmost_100000_size(child)
    return count


def solve_1():
    # lines = []
    # with open("2022/input.txt") as f:
    #     lines = f.readlines()
    # lines = [line.strip() for line in lines]
    pwd = []
    current_dir = file_directory("root")
    global head 
    head = current_dir
    for line in lines:
        if line == "$ cd /":
            pwd = []
        elif line == "$ cd ..":
            pwd.pop()
            current_dir = current_dir.parent
        elif line.startswith("$ cd "):
            pwd.append(line[5:])
            new_dir = file_directory(line[5:],current_dir)
            current_dir.add_child(new_dir)
            current_dir = new_dir
        elif line.startswith("$ ls"):
            continue
        else:
            if not line.startswith("dir "):
                current_dir.add_file(int(line.split(" ")[0]))
    head.caluclate_size()
    # print(head.size)
    return directory_with_atmost_100000_size(head)

def find_dir(current_dir, size):
    possible_dirs = []
    if current_dir.size > size:
        possible_dirs.append(current_dir)
    for child in current_dir.children:
        possible_dirs.extend(find_dir(child,size))
    possible_dirs.sort(key = lambda x: x.size)
    return possible_dirs

def solve_2():
    curr_size = head.size
    req_size = 30000000
    total_size = 70000000
    to_delete = req_size - (total_size - curr_size)
    print(to_delete)
    # find directories with size just greater than to_delete
    possible_dirs = find_dir(head,to_delete)
    for dir in possible_dirs:
        if dir.size > to_delete:
            print(dir.size)

    

if __name__ == "__main__":
    solve_1()
    print(solve_2())


