def part_one_solution():
    #rock, paper, scissors // rock, paper, scissors
    lookup = {'A': 1, 'B': 2, 'C': 3, 'X': 1, 'Y': 2, 'Z': 3}
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        total = 0
        for line in lines:
            opp_move = lookup[line[0]]
            my_move = lookup[line[2]]
            total += my_move
            if my_move == opp_move:
                total += 3
            elif my_move == opp_move + 1 or my_move == opp_move - 2:
                total += 6
        print(f'Solution to part 1: {total}')
                
def part_two_solution():
    #A,B,C -> index of points for move // X,Y,Z -> points for lose, draw, win
    input_lookup = {'A': 0, 'B': 1, 'C': 2, 'X': 0, 'Y': 3, 'Z': 6}
    point_array = [1,2,3]
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        total = 0
        for line in lines:
            opp_move = input_lookup[line[0]]
            outcome = input_lookup[line[2]]
            total += outcome
            if outcome == 3:
                total += point_array[opp_move]
            elif outcome == 6:
                total += point_array[(opp_move + 1) % 3]
            else: #outcome == 0
                total += point_array[(opp_move - 1) % 3]
        print(f'Solution to part 2: {total}')
                

if __name__ == "__main__":
    part_one_solution()
    part_two_solution()