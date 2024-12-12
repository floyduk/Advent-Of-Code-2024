# open and read the input file into a list of strings
input = open("day12/input.txt", "r").read().split()

# This is the list of all 4 directions in (dx, dy) format
directions = [(1,0), (0,1), (-1, 0), (0,-1)]

# For bounds checking
max_x = len(input[0])
max_y = len(input)

# Regions contains a list of sets. Each item in the list 
# is a region and each item is a set containing the list 
# of locations for that region. Visited is a list of locations
# we've already looked at.
regions = []
visited = set()

# Sinple function to return a char for the given coordinates with bounds checking
def get_char_at(x,y):
    if 0 <= x < max_x and 0 <= y < max_y:
        return(input[y][x])
    else:
        return(".")
    
# Find the regions by doing a flood fill from a given coordinate
def flood_fill(x: int, y: int):
    result = {(x, y)}                   # The resulting set of coordinates in this reguib
    visited.add((x, y))                 # Start with the given coordinates
    still_to_visit = [(x, y)]           # A growing list of adjascent locations we still need to visit
    starting_char = get_char_at(x, y)   # The char at the starting location that we're looking for nearby

    # Take the coordinates one by one from the list of still to visit until it's empty
    while still_to_visit:
        (x, y) = still_to_visit.pop(0)

        # Look around this location for adjascent locations with the same char. When we find one we add it
        # to the global visited list, the local still to visit list and the result set to return at the end
        for d in directions:
            if (x+d[0], y+d[1]) not in visited and get_char_at(x+d[0], y+d[1]) == starting_char:
                visited.add((x+d[0], y+d[1]))
                result.add((x+d[0], y+d[1]))
                still_to_visit.append((x+d[0], y+d[1]))

    # Return the resulting list
    return(result)

# Find the perimeter of the region by taking each location in the region, which has 4 sides and then subtracting
# one for any sides with an adjascent location in the region.
def perimeter_of(region):
    perimeter = 0
    for space in region:
        sides = 4               # obvs
        (x, y) = space
        # Look in all 4 directions. Any directions that are also in the region remove one side from this location
        for d in directions:
            if (x+d[0], y+d[1]) in region:
                sides -= 1
        perimeter += sides
    return(perimeter)

########
# MAIN #
########
   
# Search all locations in the input skipping over any that have already been visited by a flood fill. Any that
# haven't MUST be part of a new region
for y in range(0, max_y):
    for x in range(0, max_x):
        if (x, y) not in visited:
            regions.append(flood_fill(x,y))
            
total = 0
for region in regions:
    print(f"Area: {len(region)} Perimeter: {perimeter_of(region)}")
    total += len(region) * perimeter_of(region)

print(f"Total: {total}")
            