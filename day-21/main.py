import re
from collections import deque
import copy
def part_one():
    #highly inefficient I think, I can use recursion instead
    with open('input.txt') as f:
        lookup = {}
        queue = deque()
        data = list(map(lambda x: re.split(' |: ', x.strip()), f.readlines()))
        for d in data:
            if len(d) == 2:
                lookup[d[0]] = int(d[1])
            else:
                queue.append(d)
        while 'root' not in lookup:
            current = queue.popleft()
            if current[1] in lookup and current[3] in lookup:
                match current[2]:
                    case '/':
                        lookup[current[0]] = lookup[current[1]] // lookup[current[3]]
                    case '*':
                        lookup[current[0]] = lookup[current[1]] * lookup[current[3]]
                    case '+':
                        lookup[current[0]] = lookup[current[1]] + lookup[current[3]]
                    case '-':
                        lookup[current[0]] = lookup[current[1]] - lookup[current[3]]
            else:
                queue.append(current)
                        
        print(lookup['root'])

if __name__ == '__main__':
    part_one()
