# open and read the input file into a list of strings
input = [list(line) for line in open("day6/input.txt", "r").read().split()]

# Move the guard along her path. Return the set of visited locations and True/False
# indicating whether a loop was detected
def guard_path(guard_x, guard_y, dir):
    global input, directions
    visited_locations = set()
    visited_locations.add((guard_x, guard_y, dir))

    next_x, next_y = guard_x + directions[dir][0], guard_y + directions[dir][1]
    while 0 <= next_x < max_x and 0 <= next_y < max_y:
        # If guard is facing an obstacle turn right. Otherwise move forward.
        if input[next_y][next_x] == '#':
            dir = (dir+1) % len(directions)
        else:
            guard_x, guard_y = next_x, next_y
            visited_locations.add((guard_x, guard_y, dir))

        # Get the next guard location
        next_x, next_y = guard_x + directions[dir][0], guard_y + directions[dir][1]

        # If the next location and direction is on the list of visited locations 
        # then we have a loop
        if (next_x, next_y, dir) in visited_locations:
            return(set([(x, y) for x, y, d in visited_locations]), True)
    
    return(set([(x, y) for x, y, d in visited_locations]), False)

# Taking the list of locations that the guard walks from part 1 try putting an
# obstruction in each one (not the starting location) and then run the guard 
# path to see if it loops
def find_possible_new_obstructions(locations, start_x, start_y, dir):
    global input
    locations.remove((start_x, start_y))

    possible_new_obstructions = set()
    for loc in locations:
        input[loc[1]][loc[0]] = "#"

        _, loop_detected = guard_path(start_x, start_y, dir)
        if loop_detected:
            possible_new_obstructions.add((loc[0], loc[1]))

        input[loc[1]][loc[0]] = "."
    
    return(possible_new_obstructions)

########
# MAIN #
########

directions = [(0,-1), (1,0), (0,1), (-1,0)]
max_x, max_y = len(input[0]), len(input)
start_x, start_y = 0, 0

# Find the starting location of the guard
for y in range(0, max_y):
    for x in range(0, max_x):
        if input[y][x] == '^':
            start_x, start_y = x, y            

# Run the guard path
visited_locations, loop_detected = guard_path(start_x, start_y, 0)
print(f"Visited locations: {len(visited_locations)}")

# Look for possible obstructions that create a loop
possible_new_obstructions = find_possible_new_obstructions(visited_locations, start_x, start_y, 0)
print(f"Possible new obstructions: {len(possible_new_obstructions)}")