import string

def part_one_solution(alphabet):
    
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
                
        print(f'Part 1: Total priority is: {total_priority}')

def part_two_solution(alphabet):
    
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        num_of_groups = len(lines) // 3
        total_priority = 0
        for i in range(num_of_groups):
            first_rucksack = set(lines[i*3].strip())
            second_rucksack = set(lines[i*3+1].strip())
            third_rucksack = set(lines[i*3+2].strip())
            (badge,) = first_rucksack & second_rucksack & third_rucksack
            total_priority += alphabet.index(badge) + 1
        
        print(f'Part 2: Total priority is: {total_priority}')

def main():
    alphabet = list(string.ascii_letters)
    part_one_solution(alphabet)
    part_two_solution(alphabet)

if __name__ == '__main__':
    main()
    