def get_lines(file: str):    
    with open(file, 'r') as f:
        return f.read().splitlines()

### Part 1
count = 0

for line in get_lines('real_data.txt'):
    assignments = line.split(',')
    elf1 = list(map(int, assignments[0].split('-')))
    elf2 = list(map(int, assignments[1].split('-')))
    print(f'Elf one: {elf1}, Elf two: {elf2}')

    match elf1[0]:
        case e if e == elf2[0]:
            count += 1
        case e if e < elf2[0] and elf1[1] >= elf2[1]:
            count += 1
        case e if e > elf2[0] and elf1[1] <= elf2[1]:
            count += 1

print(count)

### Part 2
count = 0

for line in get_lines('real_data.txt'):
    assignments = line.split(',')
    elf1 = list(map(int, assignments[0].split('-')))
    elf2 = list(map(int, assignments[1].split('-')))
    print(f'Elf one: {elf1}, Elf two: {elf2}')

    if elf1[0] in range(elf2[0], elf2[1] + 1) or elf1[1] in range(elf2[0], elf2[1] + 1) or elf2[0] in range(elf1[0], elf1[1] + 1):
        count += 1

print(count) 