from collections import deque
import sys

def get_input_grid():
    grid = []
    
    with open('input.txt') as input_file:
        lines = input_file.readlines()
    
    for line in lines:
        row = [int(ord(char)) for char in list(line.strip())]
        grid.append(row)
        
    start = get_2d_index(grid, ord('S'))
    end = get_2d_index(grid, ord('E'))
    grid[start[0]][start[1]] = ord('a')
    grid[end[0]][end[1]] = ord('z')
    return (grid, start, end)

def part_one_solution():
    (grid, start, end) = get_input_grid()
    discovered = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    queue = deque()
    queue.append((start, 0))
    discovered = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
    discovered[start[0]][start[1]] = True
    print(bfs_explore_part_one(grid, discovered, queue, end))

def part_two_solution():
    (grid, _, end) = get_input_grid()
    shortest = sys.maxsize
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 97:
                queue = deque()
                queue.append(([i, j], 0))
                discovered = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
                discovered[i][j] = True
                if (s:=bfs_explore_part_two(grid, discovered, queue, end, shortest)) < shortest:
                    shortest = s
    print(shortest)
    
def get_2d_index(arr: list[list[str]], target: str) -> tuple[int, int]:
    for index, val in enumerate(arr):
        if target in val:
            return [index, val.index(target)]
    return [-1, -1]

def get_adjacents(grid, curr_pos):
    movements = [[1,0], [-1,0] ,[0,1], [0,-1]]
    adjacent_coords = [(y, x) for m in movements if 163 > (x:=curr_pos[1] + m[1]) > -1 and 41 > (y:=curr_pos[0] + m[0]) > -1]
    adjacent_coords = [[y, x] for (y, x) in adjacent_coords if grid[y][x] <= grid[curr_pos[0]][curr_pos[1]] + 1]
    return adjacent_coords
    
def bfs_explore_part_one(grid, discovered, queue, end):
    while queue:
        (current, length) = queue.popleft()
        if current == end:
            return length
        for adj in get_adjacents(grid, current):
            if not discovered[adj[0]][adj[1]]:
                discovered[adj[0]][adj[1]] = True
                queue.append((adj, length+1))
    return -1  
    
def bfs_explore_part_two(grid, discovered, queue, end, shortest_len):
    while queue:
        (current, length) = queue.popleft()
        if current == end:
            return length
        #abandon if the current path is taking longer than the fastest path so far
        if shortest_len <= length:
            return shortest_len 
        for adj in get_adjacents(grid, current):
            if not discovered[adj[0]][adj[1]]:
                discovered[adj[0]][adj[1]] = True
                queue.append((adj, length+1))
    return sys.maxsize

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()