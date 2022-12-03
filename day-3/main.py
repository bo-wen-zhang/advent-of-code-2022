import string

def part_one_solution():
    alphabet = list(string.ascii_letters)
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        total_priority = 0
        for line in lines:
            line = line.strip()
            midpoint = len(line) // 2
            first_compartment = set(line[:midpoint])
            second_compartment = set(line[midpoint:])
            intersection = first_compartment & second_compartment
            for item in intersection:
                total_priority += alphabet.index(item) + 1
                
        print(f'Total priority is: {total_priority}')

def part_two_solution():
    pass

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()