with open("input.txt", "r") as file:
    # output - list of rotations strings : ['R68', 'L30']
    rotations = [line.strip() for line in file.readlines()] 

# initial starting position 
current_pos = 50
zero_counter = 0

for rotation in rotations:
    dir = rotation[0]
    step = int(rotation[1:])
    if dir == 'L':
        step = -step

    current_pos = (current_pos + step) % 100

    if (current_pos == 0):
        zero_counter += 1

print("zero count" ,zero_counter)