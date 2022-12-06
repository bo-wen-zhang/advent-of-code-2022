#Might be ugly but it works

def part_one_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        
    stacks = [[] for _ in range(9)]
    for line_index in range(8):
        for stack_index, char_index in enumerate(range(1, len(lines[line_index]), 4)):
            if lines[line_index][char_index] != ' ':
                stacks[stack_index].append(lines[line_index][char_index])
    for stack in stacks:
        stack.reverse()
    for line_index in range(10, len(lines)):
        line = lines[line_index].split()
        for i in range(int(line[1])):
            item = stacks[int(line[3]) - 1].pop()
            stacks[int(line[5]) - 1].append(item)

    result = ''
    for stack in stacks:
        result += stack.pop()
    print(result)
    
def part_two_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        
    stacks = [[] for _ in range(9)]
    for line_index in range(8):
        for stack_index, char_index in enumerate(range(1, len(lines[line_index]), 4)):
            if lines[line_index][char_index] != ' ':
                stacks[stack_index].append(lines[line_index][char_index])
    for stack in stacks:
        stack.reverse()
    for line_index in range(10, len(lines)):
        line = lines[line_index].split()
        items = []
        for i in range(int(line[1])):
            item = stacks[int(line[3]) - 1].pop()
            items.append(item)
        items.reverse()
        stacks[int(line[5]) - 1].extend(items)
    result = ''
    for stack in stacks:
        result += stack.pop()
    print(result)
    
if __name__ == '__main__':
    part_one_solution()
    part_two_solution()