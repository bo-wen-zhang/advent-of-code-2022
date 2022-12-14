def part_one_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        
    cycles_of_interest = set()
    for each in [20, 60, 100, 140, 180, 220]:
        cycles_of_interest.add(each)
    x_register = 1
    current_cycle = 1
    total_sig_strength = 0
    for line in lines:
        line = line.strip().split()
        if line[0] == 'noop':
            if current_cycle in cycles_of_interest:
                total_sig_strength += current_cycle * x_register
            current_cycle += 1
        if line[0] == 'addx':
            if current_cycle in cycles_of_interest:
                total_sig_strength += current_cycle * x_register
            current_cycle += 1
            if current_cycle in cycles_of_interest:
                total_sig_strength += current_cycle * x_register
            current_cycle += 1
            x_register += int(line[1])
    print(total_sig_strength)
                 
def part_two_solution():
    with open('input.txt') as input_file:
        lines = input_file.readlines()

    crt_screen = [[' ' for _ in range(40)] for _ in range(6)]
    current_position = [0,0]
    x_register = 1
    for line in lines:
        line = line.strip().split()
        if line[0] == 'noop':
            cycle(x_register, current_position, crt_screen)
        if line[0] == 'addx':
            cycle(x_register, current_position, crt_screen)
            cycle(x_register, current_position, crt_screen)
            x_register += int(line[1])
            
    for each in crt_screen:
        print(''.join(each))
        
def cycle(x_register, current_position, crt_screen):
    if abs(x_register - current_position[1]) < 2:
        crt_screen[current_position[0]][current_position[1]] = '#'
    increment_pos(current_position)
 
def increment_pos(current_position):
    if current_position[1] == 39:
        current_position[1] = 0
        current_position[0] += 1
    else:
        current_position[1] += 1               

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()