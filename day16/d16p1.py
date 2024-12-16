from heapq import heappop, heappush
from math import inf

# open and read the input file into a list of strings
input = open("day16/input.txt", "r").read().split("\n")
max_y, max_x = len(input), len(input[0])

# These are the coordinate change values for each direction
dxdy = [
    (1, 0), (0, 1), (-1, 0), (0, -1)    # E S W N
]

# Return a list of edges from this node to adjascent nodes and their costs
def costs(state):
    pos, dir = state
    (x, y) = pos

    possible_edges = []

    # Try straight ahead
    nx, ny = x+dxdy[dir][0], y+dxdy[dir][1]
    if input[ny][nx] != "#":
        possible_edges.append((1, ((nx,ny), dir))) 

    # Try left
    nd = (dir-1)%4
    nx, ny = x+dxdy[nd][0], y+dxdy[nd][1]
    if input[ny][nx] != "#":
        possible_edges.append((1001, ((nx,ny), nd)))

    # Try right
    nd = (dir+1)%4
    nx, ny = x+dxdy[nd][0], y+dxdy[nd][1]
    if input[ny][nx] != "#":
        possible_edges.append((1001, ((nx,ny), nd)))

    return possible_edges

# This is a pretty standard dijykstra. The costs() function is where the special cases are handled.
def find_shortest_path(start):
    frontier = [(0,  start)]
    distances = {start : 0}

    # Keep searching as long as there are nodes still in our frontier list
    while frontier:
        distance, state = heappop(frontier)
        pos, dir = state
        
        # Trap-door exit if we've reached our target node. First solution to reach it must be the
        # fastest because we order our candidate nodes by cost
        if pos[0] == end_x and pos[1] == end_y:
            return distance

        # Having chosen a node get a list of edges and calculate the cost to each destination node
        for (cost, edge_state) in costs(state):
            # If the calculated cost is less than the previously known cost then update
            if distance + cost < distances.get(edge_state, inf):
                distances[edge_state] = distance + cost
                heappush(frontier, (distance + cost, edge_state))


# Get the start and end locations
start_x, start_y, end_x, end_y = 0, 0, 0, 0
for y in range(0, max_y):
    for x in range(0, max_x):
        if input[y][x] == "S": start_x, start_y = x, y
        if input[y][x] == "E": end_x, end_y = x, y

# Set up the start position and then find the shortest path
start = (start_x, start_y), 0
print(f"Minimum cost: {find_shortest_path(start)}")