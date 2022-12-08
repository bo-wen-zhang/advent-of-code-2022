def part_one_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip()

    visible_arr = [[False for _ in range(len(lines[0]))] for _ in range(len(lines))]
    print(visible_arr.count(True))
    visible_arr[0] = [True for _ in visible_arr[0]]
    visible_arr[-1] = [True for _ in visible_arr[-1]]

    #each row, checking each item from left to right
    for y in range(1, len(lines)-1):
        curr_max = lines[y][0]
        visible_arr[y][0] = True
        for x in range(1, len(lines[i])):
            if lines[y][x] > curr_max:
                visible_arr[y][x] = True
                curr_max = lines[y][x]
    
    #each row, checking each item from right to left
    for y in range(1, len(lines)-1):
        curr_max = lines[y][-1]
        visible_arr[y][-1] = True
        for x in range(len(lines[y])-2, 0, -1):
            if lines[y][x] > curr_max:
                visible_arr[y][x] = True
                curr_max = lines[y][x]

    #each column, from top to bottom
    for x in range(1, len(lines[0])-1):
        curr_max = lines[0][x]
        for y in range(1, len(lines)):
            if lines[y][x] > curr_max:
                visible_arr[y][x] = True
                curr_max = lines[y][x]

    #each column, from bottom to top
    for x in range(1, len(lines[0])-1):
        curr_max = lines[-1][x]
        for y in range(len(lines)-2, 0, -1):
            if lines[y][x] > curr_max:
                visible_arr[y][x] = True
                curr_max = lines[y][x]

    print(sum(x.count(True) for x in visible_arr))

def part_two_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
    
    for i in range(len(lines)):
        lines[i] = lines[i].strip()
    
    highest_score = 0
    #check each item apart from the perimeter
    for x in range(1, len(lines[0])-1):
        for y in range(1, len(lines)-1):
            scenic_score = 1
            dir_score = 0
            x_copy = x
            #check the items to the left
            while x_copy > 0:
                dir_score += 1
                if lines[y][x_copy-1] >= lines[y][x]:
                    break
                x_copy -= 1
            scenic_score *= dir_score
            dir_score = 0
            x_copy = x
            #check the items to the right
            while x_copy < len(lines[0])-1:
                dir_score += 1
                if lines[y][x_copy+1] >= lines[y][x]:
                    break
                x_copy += 1
            scenic_score *= dir_score
            dir_score = 0
            y_copy = y
            #check the items aboves
            while y_copy > 0:
                dir_score += 1
                if lines[y_copy-1][x] >= lines[y][x]:
                    break
                y_copy -= 1
            scenic_score *= dir_score
            dir_score = 0
            y_copy = y
            #check the items below
            while y_copy < len(lines)-1:
                dir_score += 1
                if lines[y_copy+1][x] >= lines[y][x]:
                    break
                y_copy += 1
            scenic_score *= dir_score
            if scenic_score > highest_score:
                highest_score = scenic_score
    print(highest_score)

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()