import re

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

if __name__ == '__main__':
    part_one_solution()
    