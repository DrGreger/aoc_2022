file1 = open('real_data.txt', 'r')
Lines = file1.readlines()

def part_one():
    high_cal = 0
    calories = 0
    i = 0

    for line in Lines:
        i += 1
        if line.strip('\n'):
            calories += int(line.strip('\n'))

        else: 
            if calories > high_cal:
                high_cal=calories
                high_i = i
                
            calories = 0

    print(f"{high_cal} \n{high_i}")

def part_two():
    high_cal = [0, 0 , 0]
    calories = 0
    i = 0

    for line in Lines:
        i += 1
        if line.strip('\n'):
            calories += int(line.strip('\n'))

        else: 
            if calories > high_cal[2]:
                if calories > high_cal[1]:
                    if calories > high_cal[0]:
                        high_cal = [calories, high_cal[0], high_cal[1]]
                    else:
                        high_cal = [high_cal[0], calories, high_cal[1]]
                else:
                    high_cal = [high_cal[0], high_cal[1], calories]

            calories = 0

    print(f"{high_cal} sum: {sum(high_cal)}")


if __name__ ==  "__main__":
    # part_one()
    part_two()