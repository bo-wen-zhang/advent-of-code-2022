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
            head_pos[0] = head_pos[0] + move[0]
            head_pos[1] = head_pos[1] + move[1]
            if not adjacent(head_pos, tail_pos):
                tail_visited.add((tail_pos[0], tail_pos[1]))

        
    print(len(tail_visited))

def adjacent(head_pos, tail_pos):
    h_diff = abs(head_pos[0] - tail_pos[0])
    v_diff = abs(head_pos[1] - tail_pos[1])
    if h_diff < 2 and v_diff < 2:
        return True
    if h_diff > 1 and v_diff > 1:
        moveHorizontal(head_pos, tail_pos)
        moveVertical(head_pos, tail_pos)
    elif h_diff > 1:
        moveHorizontal(head_pos, tail_pos)
        tail_pos[1] = head_pos[1]
    elif v_diff > 1:
        moveVertical(head_pos, tail_pos)
        tail_pos[0] = head_pos[0]
    return False

def moveHorizontal(head_pos, tail_pos):
    if head_pos[0] > tail_pos[0]:
        tail_pos[0] += 1
    else:
        tail_pos[0] -= 1

def moveVertical(head_pos, tail_pos):
    if head_pos[1] > tail_pos[1]:
        tail_pos[1] += 1
    else:
        tail_pos[1] -= 1
    
    
def part_two_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        
    knots = [[0,0] for _ in range(10)]
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
            knots[0][0] = knots[0][0] + move[0]
            knots[0][1] = knots[0][1] + move[1]
            for i in range(1, 9):
                adjacent(knots[i-1], knots[i])
            if not adjacent(knots[8], knots[9]):
                tail_visited.add((knots[9][0], knots[9][1]))
            
    print(len(tail_visited))
    

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()