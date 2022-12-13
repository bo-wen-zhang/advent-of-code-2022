from typing import Optional

#N-ary tree node class
class Node(object):
    def __init__(self, name: str, val: int, parent: Optional['Node']=None) -> None:
        self.name = name
        self.val = val
        self.parent = parent
        self.children = []
    def add_child(self, node: 'Node') -> None:
        self.children.append(node)  
        
     
#my solution is basically build a pair of trees using the input text
#then traverse the two trees
def part_one_solution() -> None:
    with open('input.txt') as input_file:
        lines = input_file.readlines()
    
    lines = [y for line in lines if (y:=line.strip()) != '']
    total = 0
    pair_index = 1
    for i in range(0, len(lines), 2):
        left_tree = build_tree(lines[i])
        right_tree = build_tree(lines[i+1])
        rightorder = right_order(left_tree, right_tree)
        if rightorder:
            total += pair_index
        pair_index += 1
        
    print(total)

#returns None if it just needs to move onto the next values
def right_order(left_input: Node, right_input: Node) -> bool:
    if left_input.children == [] and right_input.children == []:
        return None
    if left_input.children == []:
        return True
    if right_input.children == []:
        return False
    for i in range(min(len(left_input.children), len(right_input.children))):
        left_tree = left_input.children[i]
        right_tree = right_input.children[i]
        if left_tree.name == 'leaf' and right_tree.name == 'leaf':
            if left_tree.val < right_tree.val:
                return True
            if left_tree.val > right_tree.val:
                return False
        elif left_tree.name == 'leaf' and right_tree.name == 'list':
            left_tree.add_child(Node('leaf', left_tree.val, left_tree))
            left_tree.name = 'list'
            left_tree.val = 0
        elif left_tree.name == 'list' and right_tree.name == 'leaf':
            right_tree.add_child(Node('leaf', right_tree.val, right_tree))
            right_tree.name = 'list'
            right_tree.val = 0
        if left_tree.name == 'list' and right_tree.name == 'list':
            rightorder = right_order(left_tree, right_tree)
            if rightorder:
                return True
            if rightorder == False:
                return False

    if len(left_input.children) < len(right_input.children):
        return True
    elif len(left_input.children) > len(right_input.children):
        return False
    return None

def build_tree(line: str) -> Node:
    current_num_str = ''
    tree = Node('list', 0)
    current_node = tree
    for i in range(0, len(line)):
        if line[i] == '[':
            newListNode = Node('list', 0, current_node)
            current_node.add_child(newListNode)
            current_node = current_node.children[-1]
        elif line[i] == ']':
            if current_num_str != '':
                current_node.add_child(Node('leaf', int(current_num_str), current_node))
                current_num_str = ''
            current_node = current_node.parent
        elif line[i] == ',':
            if current_num_str != '':
                current_node.add_child(Node('leaf', int(current_num_str), current_node))
                current_num_str = ''
        else:
            current_num_str += line[i]
    return tree
    
    
if __name__ == '__main__':
    part_one_solution()