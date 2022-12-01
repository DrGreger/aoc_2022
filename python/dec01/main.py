def get_lines(file: str):    
    with open(file, 'r') as f:
        return f.read().splitlines()

def backpacks_as_lists(lines):
    pack_list = [[]]
    pack_list.extend([] for x in lines if not x or pack_list[-1].append(int(x)))
    return pack_list

def part_one(file: str):
    bp_list = backpacks_as_lists(get_lines(file))
    res = sorted(map(sum, bp_list), reverse=True)[0]
    print(f'Higest count: {res}')

def part_two(file):
    bp_list = backpacks_as_lists(get_lines(file))
    res = sum(sorted(map(sum, bp_list), reverse=True)[:3])
    print(f'Total count for three highest: {res}')


if __name__ ==  "__main__":
    part_one('real_data.txt')
    part_two('real_data.txt')