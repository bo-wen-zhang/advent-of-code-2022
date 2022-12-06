def solution(size):
    with open('input.txt') as input_file:
        line = input_file.read()
        
    start = 0
    result = -1
    end = start+size
    input_length = len(line)
    while end <= input_length:
        if len(set(line[start:end])) == size: #maybe i can come up with a solution using queues when i have the time
            result = end
            break
        start += 1
        end += 1
    print(result)

if __name__ == '__main__':
    solution(4)  #part 1
    solution(14) #part 2