from heapq import heappop, heappush
from math import inf

# open and read the input file into a list of strings
input = open("day16/input.txt", "r").read().split("\n")
max_y, max_x = len(input), len(input[0])

# These are the coordinate change values for each direction
dxdy = [
    (1, 0), (0, 1), (-1, 0), (0, -1)    # E S W N
]

# Return a list of edges from this node to adjascent nodes and their costs. Also added path tracking to 
# the state.
def costs(state):
    pos, dir, path = state
    (x, y) = pos

    possible_edges = []

    # Try straight ahead
    nx, ny = x+dxdy[dir][0], y+dxdy[dir][1]
    if input[ny][nx] != "#":
        possible_edges.append((1, ((nx,ny), dir, path + "^"))) 

    # Try left
    nd = (dir-1)%4
    nx, ny = x+dxdy[nd][0], y+dxdy[nd][1]
    if input[ny][nx] != "#":
        possible_edges.append((1001, ((nx,ny), nd, path + "<")))

    # Try right
    nd = (dir+1)%4
    nx, ny = x+dxdy[nd][0], y+dxdy[nd][1]
    if input[ny][nx] != "#":
        possible_edges.append((1001, ((nx,ny), nd, path + ">")))

    return possible_edges

# This is a pretty standard dijykstra. The costs() function is where the special cases are handled.
shortest_paths = []
shortest_path = inf
def find_shortest_path(start):
    global shortest_path, shortest_paths

    frontier = [(0,  start)]
    distances = {start : 0}

    # Keep searching as long as there are nodes still in our frontier list
    while frontier:
        distance, state = heappop(frontier)
        pos, dir, path = state

        # If this path is longer than the shortest path then we're not interested in it
        if distance > shortest_path:
            break
        
        # When we reach the end check if this is the shortest path and if so add it to the shortest
        # paths list. There will be many equally short paths.
        if pos[0] == end_x and pos[1] == end_y:
            print("path found")
            if distance <= shortest_path:
                print(f"shortest path found {distance}")
                shortest_path = distance
                shortest_paths.append(path)

        # Having chosen a node get a list of edges and calculate the cost to each destination node. Note
        # the <= in there. We ARE interested in edges that are equal distance or shorter than previous
        # edges because we want ALL the shortest paths not just the shortest one. Small modification here
        # to our distances dict because using edge_state as a index didn't work if I included the path. 
        # So I just index on location and direction.
        for (cost, edge_state) in costs(state):
            # If the calculated cost is less than the previously known cost then update
            if distance + cost <= distances.get((edge_state[0], edge_state[1]), inf):
                distances[(edge_state[0], edge_state[1])] = distance + cost
                heappush(frontier, (distance + cost, edge_state))


# Get the start and end locations
start_x, start_y, end_x, end_y = 0, 0, 0, 0
for y in range(0, max_y):
    for x in range(0, max_x):
        if input[y][x] == "S": start_x, start_y = x, y
        if input[y][x] == "E": end_x, end_y = x, y

# Set up the start position then find the shortest paths - all of em!
start = (start_x, start_y), 0, ""
find_shortest_path(start)

# Run all the paths we found keeping track of the locations on the map that they pass through. Add all 
# locations to a set to avoid duplicates.
locs = set()
locs.add((start_x, start_y))
locs.add((end_x, end_y))
for p in shortest_paths:
    (x, y), d = (start_x, start_y), 0 # Initialize each path run with the start location and east direction
    for c in p:
        if c == "^": # move forward
            (x, y) = (x+dxdy[d][0], y+dxdy[d][1])
        elif c == ">": # turn right and move forward
            d = (d+1)%4
            (x, y) = (x+dxdy[d][0], y+dxdy[d][1])
        elif c == "<": # turn left and move forward
            d = (d-1)%4
            (x, y) = (x+dxdy[d][0], y+dxdy[d][1])
        locs.add((x, y))

# The number of locations we passed through with all the shortest paths is the solution
print(f"Minimum cost: {shortest_path}")
print(len(shortest_paths), " shortest paths found")
print(f"Unique locations in all shortest paths: {len(locs)}")