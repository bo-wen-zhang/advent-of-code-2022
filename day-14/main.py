def get_terrain():
    with open('input.txt') as f:
        data = list(map(lambda x: list(map(lambda y: list(map(lambda z: int(z),y.split(','))),x.strip().split(' -> '))), f.readlines()))
    rocks = set()
    for line in data:
        for i in range(len(line)-1):
            start = line[i]
            end = line[i+1]
            rocks.add(tuple(start))
            rocks.add(tuple(end))
            if start[0] == end[0]:
                low = min(start[1], end[1])
                high = max(start[1], end[1])
                for j in range(low, high+1):
                    rocks.add((start[0],j))
            else:
                low = min(start[0], end[0])
                high = max(start[0], end[0])
                for j in range(low, high+1):
                    rocks.add((j, start[1]))
    return rocks

def part_one():
    rocks = get_terrain()
    sand_to_rest = 0
    floor = max(list(map(lambda x: x[1], rocks)))
    while True:
        current_coords = (500, 0)
        while True:
            if current_coords[1] == floor:
                print(sand_to_rest)
                return sand_to_rest
            directly_below = (current_coords[0], current_coords[1]+1)
            if directly_below not in rocks:
                current_coords = directly_below
                continue
            
            left_below = (current_coords[0]-1, current_coords[1]+1)
            if left_below not in rocks:
                current_coords = left_below
                continue
            
            right_below = (current_coords[0]+1, current_coords[1]+1)
            if right_below not in rocks:
                current_coords = right_below
                continue
            
            rocks.add(current_coords)
            sand_to_rest += 1
            break
        
def part_two():
    rocks = get_terrain()
    sand_to_rest = 0
    floor = max(list(map(lambda x: x[1], rocks))) + 1
    while True:
        current_coords = (500, 0)
        if current_coords not in rocks:      
            while True:
                if current_coords[1] == floor:
                    rocks.add(current_coords)
                    sand_to_rest += 1
                    break
                directly_below = (current_coords[0], current_coords[1]+1)
                if directly_below not in rocks:
                    current_coords = directly_below
                    continue
                
                left_below = (current_coords[0]-1, current_coords[1]+1)
                if left_below not in rocks:
                    current_coords = left_below
                    continue
                
                right_below = (current_coords[0]+1, current_coords[1]+1)
                if right_below not in rocks:
                    current_coords = right_below
                    continue
                
                rocks.add(current_coords)
                sand_to_rest += 1
                break
        else:
            print(sand_to_rest)
            return
                
    
                
if __name__ == '__main__':
    part_one()
    part_two()