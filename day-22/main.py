import collections
import numpy as np
import re

def part_one():
    with open('input.txt') as f:
        data = f.read().split('\n\n')
    tile_map = data[0].split('\n')
    turns = collections.deque(re.split('\d+', data[1])[1:-1])
    steps = collections.deque(map(lambda x: int(x), re.split('R|L', data[1])))
    blocked = set()
    width = max([len(line) for line in tile_map])
    left_wall, right_wall, ceiling, floor = {}, {}, {}, {}
    for y, line in enumerate(tile_map):
        left = 0
        right = len(line)-1
        for each in line:
            if each != ' ':
                break
            left+=1
        for each in line[::-1]:
            if each != ' ':
                break
            right-=1
        left_wall[(y, left)] = (y, right)
        right_wall[(y, right)] = (y, left)
        
        xs = np.where(np.array(list(line))=='#')[0]
        for x in xs:
            blocked.add((y, x))
    for i in range(len(tile_map)):
        diff = width - len(tile_map[i])
        spacer = [' ' for _ in range(diff)]
        tile_map[i] = list(tile_map[i])+spacer
    for x in range(width):
        up = 0
        down = len(tile_map)-1
        for y in range(0, len(tile_map)):
            if tile_map[y][x] != ' ':
                up = y
                break
        for y in range(len(tile_map)-1, -1, -1):
            if tile_map[y][x] != ' ':
                down = y
                break
        ceiling[(up, x)] = (down, x)
        floor[(down, x)] = (up, x)
            
    outer_edge = set().union(left_wall.keys(), right_wall.keys(), ceiling.keys(), floor.keys())
    current_pos = (0,0)
    x = 0
    while tile_map[0][x] != '.':
        x+=1
    c_pos = (0, x)
    d = [(0,1), (1,0), (0,-1), (-1,0)]  #right, down, left, up
    c_d = 0

    while True:
        if steps:
            c_steps = steps.popleft()
            while c_steps > 0:
                next_pos = (c_pos[0]+d[c_d][0],c_pos[1]+d[c_d][1])
                if c_pos in outer_edge:
                    if c_d == 0 and (c_pos in right_wall):   #right
                        next_pos = right_wall[c_pos]
                            
                    elif c_d == 1 and c_pos in floor: #down
                        next_pos = floor[c_pos]
                    elif c_d == 2 and c_pos in left_wall: #left
                        next_pos = left_wall[c_pos]
                    elif c_d == 3 and c_pos in ceiling: #up
                        next_pos = ceiling[c_pos]
                if next_pos in blocked:
                    break
                else:
                    c_pos = next_pos
                c_steps -= 1
        if steps:
            next_dir = turns.popleft()
            if next_dir == 'R':
                c_d = (c_d+1) % 4
            elif next_dir == 'L':
                c_d = (c_d-1) % 4
            else:
                print('direction error')
                return
        if not turns and not steps:
            print(1000*(c_pos[0]+1)+4*(c_pos[1]+1)+c_d)
            return

    
    
if __name__ == '__main__':
    part_one()