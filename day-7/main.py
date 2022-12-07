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

def part_one_solution() -> None:
    file_tree = create_directory_tree()
    set_dir_sizes(file_tree)
    result = get_sum_total(file_tree)
    print(result) 


if __name__ == '__main__':
    part_one_solution()