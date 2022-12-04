import re

def part_one_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        contained_pairs = 0
        for line in lines:
            ranges = get_ranges(line)
            if ranges[0] <= ranges[2] and ranges[1] >= ranges[3]:
                contained_pairs += 1

            elif ranges[2] <= ranges[0] and ranges[3] >= ranges[1]:
                contained_pairs += 1
            
        print(contained_pairs)

def part_two_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        overlapping_pairs = 0
        for line in lines:
            ranges = get_ranges(line)
            if ranges[1] < ranges[2]:
                continue
            elif ranges[3] < ranges[0]:
                continue
            else:
                overlapping_pairs += 1
        
        print(overlapping_pairs)

#Splits the input line and cast into a list of numbers
def get_ranges(line):
    return [int(x) for x in re.split('[,-]', line.strip())]

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()