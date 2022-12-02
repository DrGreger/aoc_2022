def get_lines(file: str):    
    with open(file, 'r') as f:
        return f.read().splitlines()

score = 0
i = 0
lines = get_lines("real_input.txt")
for line in lines:
    p1 = ord(line.split()[0]) - 64
    p2 = ord(line.split()[1]) - 64 - 23

    match p1 - p2:
        case -1 | 2: # p2 is bigger, I won
            score += 6 + p2
            i += 1
        case 0: # it's a draw
            score += 3 + p2
            i += 1
        case 1 | -2 : # p2 is smaller, I lost
            score += p2
            i += 1
    
print(f'part 1; score: {score}, total rounds: {i}')

score_2 = 0
i = 0

for line in lines:
    p1 = ord(line.split()[0]) - 64
    p2 = ord(line.split()[1]) - 64 - 23

    match p2:
        case 1: # i need to loose
            score_2 += 0 + (p1 + 2)%4 + int((p1 + 2)/4)
            i += 1
        case 2: # it's a draw
            score_2 += 3 + p1
            i += 1
        case 3 : # i need to win
            score_2 += 6 + (p1 + 1)%4 + int((p1 + 1)/4)
            i += 1

print(f'part 1; score: {score_2}, total rounds: {i}')