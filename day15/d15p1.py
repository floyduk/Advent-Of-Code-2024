# open and read the input file into a list of strings
input = open("day15/input.txt", "r").read().split("\n")

# directions dict
d = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

# Read in the input file
map, moves, reading_map = [], "", True
for line in input:
    if reading_map:
        if line == "":
            reading_map = False
        else:
            map.append(line)
    else:
        moves += line

max_x = len(map[0])
max_y = len(map)

# Get the locations of the boxes, the walls and the robot
boxes, walls, robot_x, robot_y = [], [], 0, 0
for y in range(0, max_y):
    for x in range(0, max_x):
        if map[y][x] == "O": boxes.append((x, y))
        elif map[y][x] == "#": walls.append((x, y))
        elif map[y][x] == "@": robot_x, robot_y = x, y

# Iterate the list of moves moving the robot
for m in moves:
    destination = (robot_x + d[m][0], robot_y + d[m][1])
    if destination in walls:
        # there is a wall in the way - do nothing
        pass
    elif destination in boxes:
        # there is a box in the way - try to push boxes
        lookahead = (destination[0] + d[m][0], destination[1] + d[m][1])
        while lookahead in boxes:
            lookahead = (lookahead[0] + d[m][0], lookahead[1] + d[m][1])
        if lookahead in walls:
            # Boxes up to the wall. Do nothing
            pass
        else:
            # There is a space behind the boxes. Push everything
            boxes.remove(destination)
            boxes.append(lookahead)
            (robot_x, robot_y) = destination
    else:
        # There's nothing in the way so move
        (robot_x, robot_y) = destination

print(sum([(y*100) + x for x, y in boxes]))