from itertools import permutations

# open and read the input file into a list of strings
input = open("day8/input.txt", "r").read().split("\n")

# A couple of super simple functions that simplify the code later
# Written as lambdas for brevity. get_node returns a node based on 
# 2 antennae locations. check_bound returns true if a given location
# is within the map.
get_node = lambda a, b: (b[0] + (b[0] - a[0]), b[1] + (b[1] - a[1]))
check_bound = lambda a: 0 <= a[0] < max_x and 0 <= a[1] < max_y

# Init some useful variables
max_x = len(input[0])
max_y = len(input)
antenae = dict()

# Find all the antennae. Create a dictionary where the antenna frequency
# (the letter or number) is the key and the value is a list of coordinates
# for antennae of that frequency
for y in range(0, max_y):
    for x in range(0, max_x):
        c = input[y][x]
        if c == '.':
            continue
        else:
            if c in antenae.keys():
                antenae[c].append((x,y))
            else:
                antenae[c] = [(x,y)]

# Now iterate the list of frequencies (the keys of the antennae dictionary)
# and using the key value (a list of coordinates) iterate the permutations of 
# those coordinates to find the locations of the nodes. Put the node locations
# in a set to avoid duplicates. 
nodes = set()
for frequencies in antenae.keys():
    # Permutations(x, 2) gives every permutation of 2 items in the list including
    # differently orderded permutations (AB and BA)
    for a in permutations(antenae[frequencies], 2):
        # Get the node location based on this permutation of antennae
        node = get_node(a[0], a[1])

        # If this node is on the map then add it to the list
        if check_bound(node):
            nodes.add(node)

print(f"{len(nodes)} nodes")