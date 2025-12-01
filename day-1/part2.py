with open("input.txt", "r") as file:
    # output - list of rotations strings : ['R68', 'L30']
    rotations = [line.strip() for line in file.readlines()] 

# initial starting position 
current_pos = 50
zero_passed = 0

for rotation in rotations:
    dir = rotation[0]
    step = int(rotation[1:])
    if dir == 'L':
        take_step = -1
    else:
        take_step = 1

    for s in range(step):
        current_pos = (current_pos + take_step) % 100 
        if current_pos == 0:
            zero_passed += 1

print("passed zeros" ,zero_passed)