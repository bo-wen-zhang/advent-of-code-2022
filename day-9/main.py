def part_one_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
    
    head_pos = [0,0]
    tail_pos = [0,0]
    tail_visited = set()
    tail_visited.add((0,0))
    
    for line in lines:
        line = line.strip().split()
        dir = line[0]
        num_of_moves = int(line[1])
        match dir:
            case 'U':
                move = [0, 1]
            case 'D':
                move = [0, -1]
            case 'L':
                move = [-1, 0]
            case 'R':
                move = [1, 0]
        for i in range(num_of_moves):
            last_head_pos = head_pos.copy()
            head_pos[0] = head_pos[0] + move[0]
            head_pos[1] = head_pos[1] + move[1]
            if not adjacent(head_pos, tail_pos):
                tail_pos = last_head_pos
                tail_visited.add((tail_pos[0], tail_pos[1]))
        
    print(len(tail_visited))

def adjacent(head_pos, tail_pos):
    if abs(head_pos[0] - tail_pos[0]) > 1:
        return False
    if abs(head_pos[1] - tail_pos[1]) > 1:
        return False
    return True
    

if __name__ == '__main__':
    part_one_solution()