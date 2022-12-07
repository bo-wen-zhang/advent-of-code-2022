from typing import Optional
#N-ary tree node class
class Node(object):
    def __init__(self, name: str, size: int, parent: Optional['Node']=None) -> None:
        self.name = name
        self.size = size
        self.parent = parent
        self.children = {} #hashmap so it's easier to look up a child node
    def add_child(self, node: 'Node') -> None:
        self.children[node.name] = node        

def create_directory_tree() -> Node:
    with open('input.txt') as input_file:
        lines = input_file.readlines()
    
    file_tree = Node('/', 0)
    current_dir = file_tree
    for line in lines[1:]:
        line = line.strip().split()
        if line[0:2] == ['$', 'cd']:
            current_dir = current_dir.parent if line[2] == '..' else current_dir.children[line[2]]
        elif line == ['$', 'ls']:
            pass
        else:
            size = 0 if line[0] == 'dir' else int(line[0])
            current_dir.add_child(Node(line[1], size, current_dir))
    
    return file_tree

def set_dir_sizes(dir: Node) -> None:
    if not dir.children: #empty dir or a file. only setting size for populated directories
        return dir.size
    dir.size = sum([set_dir_sizes(dir.children[sub_dir]) for sub_dir in dir.children])
    return dir.size

def get_sum_total(dir: Node) -> int:
    if not dir.children: #empty dir or a file. only calculating total of dir sizes.
        return 0
    total = sum([get_sum_total(dir.children[sub_dir]) for sub_dir in dir.children])
    if dir.size > 100000:
        return total
    return total + dir.size

def get_big_enough_arr(dir: Node) -> list[int]:
    if not dir.children:
        return []
    dir_size_arr = []
    for sub_dir in dir.children:
        dir_size_arr.extend(get_big_enough_arr(dir.children[sub_dir]))
    if dir.size >= 1072511:
        dir_size_arr.extend([dir.size])
    return dir_size_arr
    

def solution() -> None:
    #part 1
    file_tree = create_directory_tree()
    set_dir_sizes(file_tree)
    result = get_sum_total(file_tree)
    print(f'Answer to part 1: {result}')
    
    #part 2
    unused_space = 70000000 - file_tree.size
    print(f'Unused space: {unused_space}')
    space_needed = 30000000 - unused_space
    print(f'Space needed to be freed up: {space_needed}')
    dir_size_arr = get_big_enough_arr(file_tree)
    dir_size_arr.sort()
    print(f'Answer to part 2: {dir_size_arr[0]}')

if __name__ == '__main__':
    solution()