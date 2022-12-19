import sys

def part_one_solution():
    monkey_list = set_up_monkeys()
    
    for i in range(20):
        for monkey in monkey_list:
            monkey.play()
    
    monkey_list.sort(reverse=True)

    print(monkey_list[0].num_inspections * monkey_list[1].num_inspections)
    
#had to look up how do perform modular arithmetic
def part_two_solution():
    monkey_list = set_up_monkeys()
    
    super_mod = 1
    for monkey in monkey_list:
        super_mod *= monkey.test
        
    for i in range(10000):
        for monkey in monkey_list:
            monkey.play(super_mod)
    
    monkey_list.sort(reverse=True)

    print(monkey_list[0].num_inspections * monkey_list[1].num_inspections)        
 
def set_up_monkeys():
    with open('input.txt') as input_file:
        lines = [line.strip() for line in input_file.readlines()]
    monkey_list = []

    for i in range(0, len(lines), 7):
        starting_items = [int(each) for each in lines[i+1].split(':')[1].strip().split(',')]
        op = lines[i+2].split('=')[1].strip()
        test = int(lines[i+3].split('by ')[1])
        throw_to_indexes = [int(lines[i+4].split('monkey ')[1]), int(lines[i+5].split('monkey ')[1])]
        monkey_list.append(Monkey(starting_items, op, test, throw_to_indexes))
    for monkey in monkey_list:
        monkey.set_connected_monkeys(monkey_list)
    
    return monkey_list    
        
class Monkey():
    def __init__(self, starting_items, op, test, throw_to_indexes):
        self.items = starting_items
        self.op = op
        self.test = test
        self.throw_to_indexes = throw_to_indexes
        self.num_inspections = 0
        self.true_monkey = None
        self.false_monkey = None
        
    def set_connected_monkeys(self, monkey_list):
        self.true_monkey = monkey_list[self.throw_to_indexes[0]]
        self.false_monkey = monkey_list[self.throw_to_indexes[1]]
    
    def play(self, super_mod=None):
        for index, old in enumerate(self.items):
            self.num_inspections += 1
            self.items[index] = eval(''.join(self.op))
            if not super_mod:
                self.items[index] = self.items[index] // 3
            else:
                self.items[index] = self.items[index] % super_mod
            if self.items[index] % self.test == 0:
                self.true_monkey.items.append(self.items[index])
            else:
                self.false_monkey.items.append(self.items[index])
        self.items = []

    def __gt__(self, other):
        return True if other.num_inspections < self.num_inspections else False

if __name__ == '__main__':
    part_one_solution()
    part_two_solution()