# open and read the input file into a list of strings
input = open("day14/input.txt", "r").read().split("\n")

# Iterate the input and create a list of robots where each robot is a 
# tuple of start_x, start_y, velocity_x, velocity_t
robots = []
for line in input:
    pos, vel = line.split(" ")
    start_x, start_y = pos[2:].split(",")
    vel_x, vel_y = vel[2:].split(",")
    robots.append((int(start_x), int(start_y), int(vel_x), int(vel_y)))

print(robots)

# Calculate the end positions for all the robots
q1, q2, q3, q4 = 0, 0, 0, 0
max_x, max_y, steps = 101, 103, 100
for (start_x, start_y, vel_x, vel_y) in robots:
    # Calculate end position for this robot
    start_x = (start_x + (steps*vel_x))%max_x
    start_y = (start_y + (steps*vel_y))%max_y

    # Figure out which quadrant this robot ends in
    if start_x < max_x // 2 and start_y < max_y // 2: q1 += 1 
    elif start_x > max_x // 2 and start_y < max_y // 2: q2 += 1 
    elif start_x < max_x // 2 and start_y > max_y // 2: q3 += 1 
    elif start_x > max_x // 2 and start_y > max_y // 2: q4 += 1 

print(f"Total: {q1*q2*q3*q4}")