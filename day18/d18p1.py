from heapq import heappop, heappush
from math import inf

# open and read the input file into a list of strings
input = open("day18/input.txt", "r").read().split("\n")

# These are the coordinate change values for each direction
dxdy = [
    (1, 0), (0, 1), (-1, 0), (0, -1)    # E S W N
]

def char_at(x, y):
    if 0 <= x < max_x and 0 <= y < max_y:
        return("#" if (x, y) in blocks else " ")
    else:
        return("#")
    
# Return a list of edges from this node to adjascent nodes and their costs
def costs(state):
    (x, y) = state

    possible_edges = []

    for d in dxdy:
        nx, ny = x + d[0], y + d[1]
        if char_at(nx, ny) == " ":
            possible_edges.append((1, (nx, ny)))

    return possible_edges

# This is a pretty standard dijykstra. The costs() function is where the special cases are handled.
def find_shortest_path(start):
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
        for (cost, edge_state) in costs(pos):
            # If the calculated cost is less than the previously known cost then update
            if distance + cost < distances.get(edge_state, inf):
                distances[edge_state] = distance + cost
                heappush(frontier, (distance + cost, edge_state))

########
# MAIN #
########

# Interpret input and set up some variables
blocks = [(int(x), int(y)) for (x, y) in [line.split(",") for line in input]][:1024]
max_y, max_x = 71, 71
start_x, start_y, end_x, end_y = 0, 0, max_x-1, max_y-1
print(f"Num blocks: {len(blocks)}")

# Set up the start position and then find the shortest path
start = (start_x, start_y)
print(f"Minimum cost: {find_shortest_path(start)}")