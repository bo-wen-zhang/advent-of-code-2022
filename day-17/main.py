from collections import deque
from copy import deepcopy
import sys
from itertools import islice

def part_one_solution():
    with open('input.txt') as input_file:
        jet_pattern = input_file.readline().strip()
        
    slab = Rock('-', [[' ', ' ', '@', '@', '@', '@', ' ']])
    cross = Rock('+', [
        [' ', ' ', ' ', '@', ' ', ' ', ' '],
        [' ', ' ', '@', '@', '@', ' ', ' '],
        [' ', ' ', ' ', '@', ' ', ' ', ' ']
    ])
    reverse_L = Rock('⅃', [
        [' ', ' ', ' ', ' ', '@', ' ', ' '],
        [' ', ' ', ' ', ' ', '@', ' ', ' '],
        [' ', ' ', '@', '@', '@', ' ', ' '], 
    ])
    column = Rock('|', [
        [' ', ' ', '@', ' ', ' ', ' ', ' '],
        [' ', ' ', '@', ' ', ' ', ' ', ' '],
        [' ', ' ', '@', ' ', ' ', ' ', ' '],
        [' ', ' ', '@', ' ', ' ', ' ', ' ']
    ])
    square = Rock('□', [
        [' ', ' ', '@', '@', ' ', ' ', ' '],
        [' ', ' ', '@', '@', ' ', ' ', ' ']
    ])
    
    rock_collection = [slab, cross, reverse_L, column, square]
    current_rock_idx, jet_pattern_idx, number_of_fallen_rocks = 0, 0, 0
    vertical_chamber = deque([[' ' for _ in range(7)] for _ in range(3)])
    while number_of_fallen_rocks < 2022:
        vertical_chamber.extendleft(reversed(deepcopy(rock_collection[current_rock_idx].initial_placement)))
        current_rock_coords = deepcopy(rock_collection[current_rock_idx].coords_of_parts)

        #while falling downwards
        while True:
            # move horizontal to jet pattern
            if jet_pattern[jet_pattern_idx] == '>':
                move_right(vertical_chamber, current_rock_coords)
            elif jet_pattern[jet_pattern_idx] == '<':
                move_left(vertical_chamber, current_rock_coords)
            jet_pattern_idx = (jet_pattern_idx + 1) % len(jet_pattern)
            # move downward
            if not move_down(vertical_chamber, current_rock_coords):
                break
        
        clear_empty_top(vertical_chamber)
        vertical_chamber.extendleft([[' ' for _ in range(7)] for _ in range(3)])

        current_rock_idx = (current_rock_idx + 1) % len(rock_collection)
        number_of_fallen_rocks += 1
             
    clear_empty_top(vertical_chamber)
    print(len(vertical_chamber))
    # for i in vertical_chamber:
    #     print(''.join(i))

def clear_empty_top(vertical_chamber):
    while vertical_chamber[0] == [' ', ' ', ' ', ' ', ' ', ' ', ' ']:
        vertical_chamber.popleft()
    
def move_left(vertical_chamber: list[list[str]], current_rock_coords: list[list[int]]):
    for (y, x) in current_rock_coords:
        if x-1 < 0:
            return
        elif vertical_chamber[y][x-1] == '#':
            return
    move(vertical_chamber, current_rock_coords, 1, -1)
            
def move_right(vertical_chamber: list[list[str]], current_rock_coords: list[list[int]]):
    for (y, x) in current_rock_coords:
        if x+1 > 6:
            return
        elif vertical_chamber[y][x+1] == '#':
            return
    move(vertical_chamber, current_rock_coords, 1, 1)
            
def move_down(vertical_chamber: list[list[str]], current_rock_coords: list[list[int]]):
    for (y, x) in current_rock_coords:
        if y+1 > len(vertical_chamber) - 1:
            set_still(vertical_chamber, current_rock_coords)
            return False
        elif vertical_chamber[y+1][x] == '#':
            set_still(vertical_chamber, current_rock_coords)
            return False
    move(vertical_chamber, current_rock_coords, 0, 1)
    return True

def set_still(vertical_chamber, current_rock_coords):
    for val in current_rock_coords:
        vertical_chamber[val[0]][val[1]] = '#'

def move(vertical_chamber, current_rock_coords, axis, dir):
    for i, val in enumerate(current_rock_coords):
        vertical_chamber[val[0]][val[1]] = ' '
    for i, val in enumerate(current_rock_coords):
        current_rock_coords[i][axis] = current_rock_coords[i][axis] + dir
        vertical_chamber[current_rock_coords[i][0]][current_rock_coords[i][1]] = '@'
        
class Rock:
    def __init__(self, name: str, initial_placement: list[list[str]]):
        self.name = name
        self.initial_placement = initial_placement
        self.coords_of_parts = get_2d_indexes(self.initial_placement, '@')

def get_2d_indexes(rock: list[list[str]], target: str) -> list[list[int, int]]:
    arr = []
    for idx_r, row in enumerate(rock):
        for idx_i, item in enumerate(row):
            if item == target:
                arr.append([idx_r, idx_i])
    return arr     

def part_two_solution():
    with open('input.txt') as input_file:
        jet_pattern = input_file.readline().strip()
        
    slab = Rock('-', [[' ', ' ', '@', '@', '@', '@', ' ']])
    cross = Rock('+', [
        [' ', ' ', ' ', '@', ' ', ' ', ' '],
        [' ', ' ', '@', '@', '@', ' ', ' '],
        [' ', ' ', ' ', '@', ' ', ' ', ' ']
    ])
    reverse_L = Rock('⅃', [
        [' ', ' ', ' ', ' ', '@', ' ', ' '],
        [' ', ' ', ' ', ' ', '@', ' ', ' '],
        [' ', ' ', '@', '@', '@', ' ', ' '], 
    ])
    column = Rock('|', [
        [' ', ' ', '@', ' ', ' ', ' ', ' '],
        [' ', ' ', '@', ' ', ' ', ' ', ' '],
        [' ', ' ', '@', ' ', ' ', ' ', ' '],
        [' ', ' ', '@', ' ', ' ', ' ', ' ']
    ])
    square = Rock('□', [
        [' ', ' ', '@', '@', ' ', ' ', ' '],
        [' ', ' ', '@', '@', ' ', ' ', ' ']
    ])
    state_dict = {}
    rock_collection = [slab, cross, reverse_L, column, square]
    current_rock_idx, jet_pattern_idx, number_of_fallen_rocks = 0, 0, 0
    vertical_chamber = deque([[' ' for _ in range(7)] for _ in range(3)])
    length_so_far = 0
    rock_remaining = 0
    cycles = 0
    length_diff = 0
    while number_of_fallen_rocks < 1000000000000:
        vertical_chamber.extendleft(reversed(deepcopy(rock_collection[current_rock_idx].initial_placement)))
        current_rock_coords = deepcopy(rock_collection[current_rock_idx].coords_of_parts)

        #while falling downwards
        while True:
            # move horizontal to jet pattern
            if jet_pattern[jet_pattern_idx] == '>':
                move_right(vertical_chamber, current_rock_coords)
            elif jet_pattern[jet_pattern_idx] == '<':
                move_left(vertical_chamber, current_rock_coords)
            
            jet_pattern_idx = (jet_pattern_idx + 1) % len(jet_pattern)
            # move downward
            if not move_down(vertical_chamber, current_rock_coords):
                break
        
        current_rock_idx = (current_rock_idx + 1) % len(rock_collection)
        number_of_fallen_rocks += 1
        
        clear_empty_top(vertical_chamber)
        
        if (jet_pattern_idx, current_rock_idx) in state_dict and vertical_chamber[0] == ['#', '#', '#', '#', '#', '#', '#']:
            print("rocks fallen so far: ", number_of_fallen_rocks)
            (past_length, fallen) = state_dict[(jet_pattern_idx, current_rock_idx)]
            length_diff = len(vertical_chamber) - past_length
            length_so_far = len(vertical_chamber)
            print("rocks fallen before", fallen)
            print(f'current length: {len(vertical_chamber)} || past length {past_length} || diff in length: {length_diff}')
            cycles = (1000000000000-number_of_fallen_rocks) // (number_of_fallen_rocks-fallen)
            print(f'number of cycles to be repeated: {cycles}')
            rock_remaining = (1000000000000-number_of_fallen_rocks) % (number_of_fallen_rocks-fallen)
            print(f'number of rocks left over to add after all the cycles: {rock_remaining}')
            break
        elif vertical_chamber[0] == ['#', '#', '#', '#', '#', '#', '#']:
            state_dict[(jet_pattern_idx, current_rock_idx)] = (len(vertical_chamber), number_of_fallen_rocks)
        
        vertical_chamber.extendleft([[' ' for _ in range(7)] for _ in range(3)])
    
    #reset
    vertical_chamber = deque()
    vertical_chamber.extendleft([[' ' for _ in range(7)] for _ in range(3)])
    
    for i in range(rock_remaining):
        vertical_chamber.extendleft(reversed(deepcopy(rock_collection[current_rock_idx].initial_placement)))
        current_rock_coords = deepcopy(rock_collection[current_rock_idx].coords_of_parts)

        while True:
            if jet_pattern[jet_pattern_idx] == '>':
                move_right(vertical_chamber, current_rock_coords)
            elif jet_pattern[jet_pattern_idx] == '<':
                move_left(vertical_chamber, current_rock_coords)
            jet_pattern_idx = (jet_pattern_idx + 1) % len(jet_pattern)
            if not move_down(vertical_chamber, current_rock_coords):
                break
        
        clear_empty_top(vertical_chamber)
        vertical_chamber.extendleft([[' ' for _ in range(7)] for _ in range(3)])
        current_rock_idx = (current_rock_idx + 1) % len(rock_collection)
        number_of_fallen_rocks += 1
             
    clear_empty_top(vertical_chamber)
    print(len(vertical_chamber)+(cycles*length_diff)+length_so_far)

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()