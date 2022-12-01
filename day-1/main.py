def part_one():
    with open('input.txt') as input_file:
        current_total = 0
        max_calories = 0
        lines = input_file.readlines()
        for line in lines:
            if line.strip():
                current_total += int(line)
            else:
                if current_total > max_calories:
                    max_calories = current_total
                current_total = 0
        print(f'The Elf with the most calories has {max(max_calories, current_total)} calories.')

def part_two():
    with open('input.txt') as input_file:
        lines = input_file.readlines()
        elves = [0]
        for line in lines:
            if line.strip() == '':
                elves.append(0)
            else:
                elves[-1] = elves[-1] + int(line)

        total = 0
        for _ in range(3):
            max_value = max(elves)
            total += max_value
            del elves[elves.index(max_value)]
        print(f'The top three Elves are carrying {total} calories in total.')

if __name__ == "__main__":
    part_one()
    part_two()