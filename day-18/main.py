def part_one_solution():
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
    
if __name__ == '__main__':
    part_one_solution()