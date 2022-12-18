from collections import deque

def part_one_solution():
    (three_d_matrix, axis_max) = prepare_matrix()
    sides_exposed = 0
    
    for x, row in enumerate(three_d_matrix):
        for y, col in enumerate(row):
            for z, cube in enumerate(col):
                if cube:
                    if x == 0:
                        sides_exposed += 1
                    elif not three_d_matrix[x-1][y][z]:
                        sides_exposed += 1
                    if x == axis_max[0]:
                        sides_exposed += 1
                    elif not three_d_matrix[x+1][y][z]:
                        sides_exposed += 1
                    if y == 0:
                        sides_exposed += 1
                    elif not three_d_matrix[x][y-1][z]:
                        sides_exposed += 1
                    if y == axis_max[1]:
                        sides_exposed += 1
                    elif not three_d_matrix[x][y+1][z]:
                        sides_exposed += 1
                    if z == 0:
                        sides_exposed += 1
                    elif not three_d_matrix[x][y][z-1]:
                        sides_exposed += 1
                    if z == axis_max[2]:
                        sides_exposed += 1
                    elif not three_d_matrix[x][y][z+1]:
                        sides_exposed += 1
                        
    print(sides_exposed)
    
def prepare_matrix():
    with open('input.txt') as input_file:
        lines = input_file.readlines()

    axis_max = [0,0,0]
    
    for i in range(len(lines)):
        lines[i] = lines[i].strip().split(',')
        for j in range(len(lines[i])):
            lines[i][j] = int(lines[i][j])
            if lines[i][j] > axis_max[j]:
                axis_max[j] = lines[i][j]
    
    #three_d_matrix[x][y][z]
    three_d_matrix = [[[False for _ in range(axis_max[2]+1)] for _ in range(axis_max[1]+1)] for _ in range(axis_max[0]+1)]
    for [x,y,z] in lines:
        three_d_matrix[x][y][z] = True
    
    return (three_d_matrix, axis_max)    
  
#part two is very slow, it performs a bfs for each side to check if there is a path which takes it to the perimeter of the matrix (exposed to air)  
def part_two_solution():
    (three_d_matrix, axis_max) = prepare_matrix()
    sides_exposed = 0
    
    for x, row in enumerate(three_d_matrix):
        for y, col in enumerate(row):
            for z, cube in enumerate(col):
                if cube:
                    if x == 0:
                        sides_exposed += 1
                    elif not three_d_matrix[x-1][y][z]:
                        if exposed(three_d_matrix, [x-1, y, z], axis_max):
                            sides_exposed += 1
                    if x == axis_max[0]:
                        sides_exposed += 1
                    elif not three_d_matrix[x+1][y][z]:
                        if exposed(three_d_matrix, [x+1, y, z], axis_max):
                            sides_exposed += 1
                    if y == 0:
                        sides_exposed += 1
                    elif not three_d_matrix[x][y-1][z]:
                        if exposed(three_d_matrix, [x, y-1, z], axis_max):
                            sides_exposed += 1
                    if y == axis_max[1]:
                        sides_exposed += 1
                    elif not three_d_matrix[x][y+1][z]:
                        if exposed(three_d_matrix, [x, y+1, z], axis_max):
                            sides_exposed += 1
                    if z == 0:
                        sides_exposed += 1
                    elif not three_d_matrix[x][y][z-1]:
                        if exposed(three_d_matrix, [x, y, z-1], axis_max):
                            sides_exposed += 1
                    if z == axis_max[2]:
                        sides_exposed += 1
                    elif not three_d_matrix[x][y][z+1]:
                        if exposed(three_d_matrix, [x, y, z+1], axis_max):
                            sides_exposed += 1
                        
    print(sides_exposed)
    
def exposed(three_d_matrix, current, axis_max):
    queue = deque()
    queue.append(current)
    discovered = [[[False for _ in range(axis_max[2]+1)] for _ in range(axis_max[1]+1)] for _ in range(axis_max[0]+1)]
    discovered[current[0]][current[1]][current[2]] = True
    return bfs(three_d_matrix, queue, discovered, axis_max)
    
def bfs(three_d_matrix, queue, discovered, axis_max):
    while queue:
        [x,y,z] = queue.popleft()
        
        if x == 0 or y == 0 or z == 0 or x == axis_max[0] or y == axis_max[1] or z == axis_max[2]:
            return True
        for [a,b,c] in get_adjacent(x, y, z):
            if not three_d_matrix[a][b][c] and not discovered[a][b][c]:
                discovered[a][b][c] = True
                queue.append([a,b,c])
        
    return False
    
def get_adjacent(x, y, z):
    return [[x+1,y,z],[x-1,y,z],[x,y+1,z],[x,y-1,z],[x,y,z+1],[x,y,z-1]]
    
if __name__ == '__main__':
    part_one_solution()
    part_two_solution()