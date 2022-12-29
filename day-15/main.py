import re
import numpy as np

def part_one_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
    
    cannot_contain_beacon = set()
    confirmed_beacons = set()
    for line in lines:
        line = re.split('=|,|:', line.strip())
        #sensor x, y      beacon x, y
        coords = [int(x) for x in [line[1],line[3],line[5],line[7]]]
        man_hat_dist = abs(coords[0]-coords[2]) + abs(coords[1]-coords[3])
        if coords[3] == 2000000:
            confirmed_beacons.add(coords[2])
        if man_hat_dist+coords[1]<2000000 or coords[1]-man_hat_dist>2000000:
            continue
        if coords[1] < 2000000:
            left_over_dist = coords[1] + man_hat_dist - 2000000
        else:
            left_over_dist = 2000000 - (coords[1] - man_hat_dist)
        for i in range(coords[0]-left_over_dist, coords[0]+left_over_dist+1):
            cannot_contain_beacon.add(i)
    
    print(len(cannot_contain_beacon - confirmed_beacons))
    
def part_two_solution():
    with open('input.txt') as f:
        #horrible line of code to read but it was fun to write
        data = list(map(lambda x: list(map(lambda z: int(z[1]),(filter(lambda y: y[0] % 2 == 1,enumerate(re.split('=|,|:', x.strip())))))), f.readlines()))
        for d in data:
            m_h_dist = abs(d[0]-d[2]) + abs(d[1]-d[3])
            d.append(m_h_dist)
        for d in data:
            perimeter_data = []
            p_dist = d[4]+1
            for y in range(p_dist+1):
                diff = p_dist - y
                perimeter_data.append((d[0]+diff,d[1]+y))
                perimeter_data.append((d[0]-diff,d[1]+y))
                perimeter_data.append((d[0]+diff,d[1]-y))
                perimeter_data.append((d[0]-diff,d[1]-y))
            perimeter_data = [(x, y) for (x, y) in perimeter_data if (0 <=x and x <= 4000000) and (0 <= y and y <= 4000000)]
            for (i, j) in perimeter_data:
                for d in data:
                    if (abs(d[0]-i) + abs(d[1]-j)) <= d[4]:
                        break
                else:
                    print(i*4000000+j)
                    return

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()
    