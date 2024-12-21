from heapq import heappop, heappush
from math import inf

# open and read the input file into a list of strings
input = open("day20/input.txt", "r").read().split("\n")
max_x, max_y = len(input[0]), len(input)

# These are the coordinate change values for each direction
dxdy = [
    (1, 0), (0, 1), (-1, 0), (0, -1)    # E S W N
]

# Get the char at a location with bounds checking
def char_at(x, y):
    if 0 <= x < max_x and 0 <= y < max_y:
        return(input[y][x])
    else:
        return("#")
    
# Return a list of edges from this node to adjascent nodes and their costs
shortest_path = []
def costs(state, cheat, track_path):
    (x, y) = state
    (cx, cy), (cdx, cdy) = cheat
    possible_edges = []

    # Keep track of the shortest path
    if track_path:
        shortest_path.append((x,y))

    # If we're at the cheat spot then add an edge for the cheat
    if (x, y) == (cx, cy):
        possible_edges.append((2, (cdx, cdy)))

    # Add an edge for every ordinal direction where there isn't a wall
    for d in dxdy:
        nx, ny = x + d[0], y + d[1]
        if char_at(nx, ny) != "#":
            possible_edges.append((1, (nx, ny)))

    return possible_edges

# This is a pretty standard dijykstra. The costs() function is where the special cases are handled.
def find_shortest_path(start, cheat, track_path = False):
    frontier = [(0,  start)]
    distances = {start : 0}

    # Keep searching as long as there are nodes still in our frontier list
    while frontier:
        distance, pos = heappop(frontier)
        
        # Trap-door exit if we've reached our target node. First solution to reach it must be the
        # fastest because we order our candidate nodes by cost
        if pos[0] == end_x and pos[1] == end_y:
            return distance

        # Having chosen a node get a list of edges and calculate the cost to each destination node
        for (cost, edge_state) in costs(pos, cheat, track_path):
            # If the calculated cost is less than the previously known cost then update
            if distance + cost < distances.get(edge_state, inf):
                distances[edge_state] = distance + cost
                heappush(frontier, (distance + cost, edge_state))

# Return the manhattan distance between two points
def manhattan_distance(x1,y1,x2,y2):
    return(abs(x1-x2) + abs(y1-y2))

# Find start and end
for y in range(0, max_y):
    for x in range(0, max_x):
        if char_at(x, y) == "S": start_x, start_y = x, y
        if char_at(x, y) == "E": end_x, end_y = x, y

# Get the shortest path
find_shortest_path((start_x, start_y), [(0,0),(0,0)], True)
shortest_path.append((end_x, end_y))

# Start and end points of the cheat are all we're interested in and they must be on the shortest (only) path.
# So we can just pick a point on the path (i) and then look ahead from that point for points (j) that are within
# glitch range as a manhattan distance. PLUS we're only interested in points that are a minimum target_saving
# range so we can always look at least that many steps ahead. For part 1 I just re-ran my dijkstra with the 
# cheat in an an extra 2-cost edge to get the modified path length and calculate the savings. This works but is
# very slow. Had to find a better way for part 2.
target_saving = 100
cheats_count = 0
for i in range(0, len(shortest_path)):
    if i % 100 == 0: print(f"{i}/{len(shortest_path)}")
    (x,y) = shortest_path[i]
    for j in range(i+target_saving, len(shortest_path)):
        (ex, ey) = shortest_path[j]
        glitch_distance = manhattan_distance(x, y, ex, ey)
        if glitch_distance <= 2:
            saving = len(shortest_path) - find_shortest_path((start_x, start_y), [(x, y), (ex, ey)], False)
            if saving >= target_saving:
                cheats_count += 1

print(f"Routes that save {target_saving} picoseconds or more: {cheats_count}")