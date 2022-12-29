from collections import deque
import copy
def part_one_solution():
    with open('input.txt') as input_file:
        numbers = [(int(number), i) for i, number in enumerate(input_file.read().split('\n'))]
        queue = deque(numbers)
    length = len(numbers)
    for i in range(length):
        (value, order) = queue.popleft()
        old_index = numbers.index((value, i))
        if value != 0:
            numbers.remove((value, order))
            new_index = (old_index + value) % (length - 1)
            numbers.insert(new_index, (value, order))
        
    index_of_zero = [index for index, item in enumerate(numbers) if item[0] == 0].pop()
    print(index_of_zero)
    print(numbers[(index_of_zero+1000)%length][0]+numbers[(index_of_zero+2000)%length][0]+numbers[(index_of_zero+3000)%length][0])
    
def part_two_solution():
    with open('input.txt') as input_file:
        numbers = [(int(number)*811589153, i) for i, number in enumerate(input_file.read().split('\n'))]
        queue = deque(numbers)
    length = len(numbers)
    for _ in range(10):
        temp_queue = copy.deepcopy(queue)
        for i in range(length):
            (value, order) = temp_queue.popleft()
            old_index = numbers.index((value, i))
            if value != 0:
                numbers.remove((value, order))
                new_index = (old_index + value) % (length - 1)
                numbers.insert(new_index, (value, order))
        
    index_of_zero = [index for index, item in enumerate(numbers) if item[0] == 0].pop()
    print(index_of_zero)
    print(numbers[(index_of_zero+1000)%length][0]+numbers[(index_of_zero+2000)%length][0]+numbers[(index_of_zero+3000)%length][0])
    
if __name__ == '__main__':
    part_one_solution()
    part_two_solution()