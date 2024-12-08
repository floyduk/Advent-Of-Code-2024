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
print(f"max_x {max_x} max_y {max_y}")
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
# those coordinates to find the locations of the nodes. When a valid node is 
# add that node to the list of antennae so that we go around again moving
# outward until we hit the edge of the map.Put the node locations as we find
# them into a set to avoid duplicates. 
nodes = set()
for frequencies in antenae.keys():
    for a in permutations(antenae[frequencies], 2):
        # Add the locations of the antennae to the node list since they are
        # always nodes as well
        nodes.add(a[0])
        nodes.add(a[1])

        # permutations gives a tuple but we want to modify it so make it a list
        al = list(a)

        # While there are items left on the list keep moving out finding nodes
        while len(al) > 0:
            node = get_node(al[0], al[1])
            if check_bound(node):
                # If this node is on the map then add it to the nodes list AND 
                # the antennae list (al), then chop off the first item and go 
                # around this loop again.
                nodes.add(node)
                al.append(node)
                al = al[1:]
            else:
                # Once we hit the edge of the map clear the list to stop the loop
                al = []

print(f"{len(nodes)} nodes")