# open and read the input file into a list of strings
input = open("day15/input.txt", "r").read().split("\n")

# directions dict
d = {"^": (0, -1), "v": (0, 1), "<": (-1, 0), ">": (1, 0)}

# map_adjustment
remap = {"#": "##", ".": "..", "O": "[]", "@": "@."}

# Return the origin of the box if location contains either half of a box
def is_box(loc):
    if loc in boxes: return(loc)
    if (loc[0]-1, loc[1]) in boxes: return((loc[0]-1, loc[1]))
    return(False)

# Read in the input file
map, moves, reading_map = [], "", True
for line in input:
    if reading_map:
        if line == "":
            reading_map = False
        else:
            newline = ""
            for c in line:
                newline += remap[c]
            map.append(newline)
    else:
        moves += line

max_x = len(map[0])
max_y = len(map)

# Get the locations of the boxes, the walls and the robot
boxes, walls, robot_x, robot_y = [], [], 0, 0
for y in range(0, max_y):
    for x in range(0, max_x):
        if map[y][x] == "[": boxes.append((x, y))
        elif map[y][x] == "#": walls.append((x, y))
        elif map[y][x] == "@": robot_x, robot_y = x, y

# Iterate the list of moves moving the robot
for m in moves:
    destination = (robot_x + d[m][0], robot_y + d[m][1])
    if destination in walls:
        # there is a wall in the way - do nothing
        pass
    elif is_box(destination):
        # there is a box in the way - try to push boxes
        if m in "<>":
            # Sideways push
            lookahead = (destination[0] + (2*d[m][0]), destination[1])
            # Make a list of boxes we've collected as part of this push
            collected_boxes = [is_box(destination)]
            
            # Keep looking further ahead until we find a wall or a space
            while is_box(lookahead):
                collected_boxes.append(is_box(lookahead))
                lookahead = (lookahead[0] + (2*d[m][0]), lookahead[1])

            # Check if we found a wall at the end of our line of boxes
            if lookahead in walls:
                # Boxes up to the wall. Do nothing
                pass
            else:
                # There is a space behind the boxes. Push everything
                # First move all the boxes we collected
                for box in collected_boxes:
                    boxes.remove(box)                    
                    boxes.append((box[0]+d[m][0], box[1]))
                # Then move the robot
                (robot_x, robot_y) = destination
        else:
            # Vertical push

            # Make a set of boxes we've collected as part of this push
            new_collected_boxes = set([is_box(destination)])
            collected_boxes = set([is_box(destination)])

            # Look ahead at the spaces above or below BOTH location in the double
            # width box. Collect any new boxes we find. If we find any walls then
            # stop this push entirely.
            wall_blocking = False

            while new_collected_boxes and not wall_blocking:
                # We're going to lookahead from the newly collected boxes
                lookahead_boxes = new_collected_boxes
                new_collected_boxes = set()
                for box in lookahead_boxes:
                    # These are the 2 locations we need to lookahead at
                    lookahead1 = (box[0], box[1]+d[m][1])
                    lookahead2 = (box[0]+1, box[1]+d[m][1])

                    # Look ahead at those 2 location looking for boxes or walls
                    if lookahead1 in walls or lookahead2 in walls:
                        # There is a wall blocking this push
                        wall_blocking = True
                    if is_box(lookahead1):
                        # New box found - add it to the collection
                        new_collected_boxes.add(is_box(lookahead1))
                    if is_box(lookahead2):
                        # New box found - add it to the collection
                        new_collected_boxes.add(is_box(lookahead2))

                # Add newly collected boxes to our collected boxes set
                for box in new_collected_boxes:
                    collected_boxes.add(box)

            # If we've exited the while then we didn't collect any new boxes during 
            # our look ahead. So as long as no walls were detected we can move all 
            # the boxes we collected
            if not wall_blocking:
                for box in collected_boxes:
                    boxes.remove(box)                    
                    boxes.append((box[0], box[1]+d[m][1]))
                # Then move the robot
                (robot_x, robot_y) = destination
    else:
        # There's nothing in the way so move
        (robot_x, robot_y) = destination

print(sum([(y*100) + x for x, y in boxes]))