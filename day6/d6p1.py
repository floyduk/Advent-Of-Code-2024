# open and read the input file into a list of strings
input = open("day6/input.txt", "r").read().split()

directions = [(0,-1), (1,0), (0,1), (-1,0)]
dir = 0
guard_x, guard_y = 0, 0
visited_locations = set()
max_x, max_y = len(input[0]), len(input)

# Find the starting location of the guard
for y in range(0, max_y):
    for x in range(0, max_x):
        if input[y][x] == '^':
            guard_x, guard_y = x, y
visited_locations.add((guard_x, guard_y))

# Move the guard along her path until she leaves the area        
next_x, next_y = guard_x + directions[dir][0], guard_y + directions[dir][1]
while 0 <= next_x < max_x and 0 <= next_y < max_y:
    # If guard is facing an obstacle turn right. Otherwise move forward.
    if input[next_y][next_x] == '#':
        dir = (dir+1) % len(directions)
    else:
        guard_x, guard_y = next_x, next_y
        visited_locations.add((guard_x, guard_y))

    # Get the next guard location
    next_x, next_y = guard_x + directions[dir][0], guard_y + directions[dir][1]

# Display the number of visited locations
print(f"Total: {len(visited_locations)}")