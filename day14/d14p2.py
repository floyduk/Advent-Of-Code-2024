# open and read the input file into a list of strings
input = open("day14/input.txt", "r").read().split("\n")

# Returns true if this robot has 8 robots around it
def is_clustered(x, y):
    is_in_robots_pos = lambda x, y: [x, y] in robots_pos
    if  is_in_robots_pos(x-1, y) and \
        is_in_robots_pos(x+1, y) and \
        is_in_robots_pos(x, y-1) and \
        is_in_robots_pos(x, y+1) and \
        is_in_robots_pos(x+1, y+1) and \
        is_in_robots_pos(x+1, y-1) and \
        is_in_robots_pos(x-1, y+1) and \
        is_in_robots_pos(x-1, y-1):
        return(True)
    return(False)

# Iterate the input and create a list of robots where each robot is a 
# tuple of start_x, start_y, velocity_x, velocity_t
robots_pos = []
robots_vel = []
for line in input:
    pos, vel = line.split(" ")
    robots_pos.append([int(a) for a in pos[2:].split(",")])
    robots_vel.append([int(a) for a in vel[2:].split(",")])

# Run forever moving all the robots one step one by one and each step
# checking if there are 8 robots surrounding this one making a cluster
# of 9 in a square. That's our signal that we've formed the christmas
# tree and our cue to stop and print the solution
max_x, max_y, steps = 101, 103, 0
while True:
    steps += 1

    for i in range(0, len(robots_pos)):
        # Get the next robot data
        pos, vel = robots_pos[i], robots_vel[i]

        # Calculate end position for this robot
        pos[0] = (pos[0] + vel[0])%max_x
        pos[1] = (pos[1] + vel[1])%max_y

        # Check for cluster. If one is found stop and print the answer.
        if is_clustered(pos[0], pos[1]):
            print(f"Steps: {steps}")
            exit(0)