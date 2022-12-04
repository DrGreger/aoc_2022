def get_lines(file: str):    
    with open(file, 'r') as f:
        return f.read().splitlines()

def get_score(item):
    if item.islower():
        return ord(item) - 96
    return ord(item) - 38

def grouper(iterable, n):
    args = [iter(iterable)] * n
    return zip(*args)


### PART 1

t_score = 0

for l in get_lines("real_data.txt"):
    for item in (i for i in l[int(len(l)/2):] if i in l[:int(len(l)/2)]):
        t_score += get_score(item)
        break
print(f'Part 1; The total score is: {t_score}')

### PART 2

t_score = 0

for g in grouper(get_lines("real_data.txt"), 3):
    for item in (i for i in g[0] if i in g[1] and i in g[2]):
        t_score += get_score(item)
        break
print(f'Part 2; The total score for all groups is: {t_score}')