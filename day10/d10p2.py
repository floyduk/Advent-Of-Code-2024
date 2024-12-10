# open and read the input file into a list of strings
input = open("day10/input.txt", "r").read().split()

# This is the list of all 4 directions in (dx, dy) format
directions = [(1,0), (0,1), (-1, 0), (0,-1)]

# For bounds checking
max_x = len(input[0])
max_y = len(input)

# Bounds checked function to get the char at a grid location
def get_char(x,y):
    if 0 <= x < max_x and 0 <= y < max_y:
        if input[y][x] == ".": return(-1)
        else: return(int(input[y][x]))
    else: return(-1)
    
# Recursive function to search for the trailheads. Records the location
# and exits when it # reaches a 9. Yes keeping the list of reachable
# nines as a global is ugly. Sue me.
def find_trailheads(x,y,c):
    result = 0
    for d in directions:
        if c == 8:
            if get_char(x + d[0], y + d[1]) == 9:
                result += 1
        else:
            if get_char(x + d[0], y + d[1]) == c + 1:
                result += find_trailheads(x + d[0], y + d[1], c + 1)
    
    return(result)

########
# MAIN #
########

# Search the map looking for 0s (trailheads) and then call the recursive
# function to find the rating of each trailhead which is the number of 
# possible routes to a 9 from this trailhead.
rating_total = 0
for y in range(0, max_y):
    for x in range(0, max_x):
        if get_char(x, y) == 0:
            rating_total += find_trailheads(x, y, 0)

print(f"Rating Total: {rating_total}")