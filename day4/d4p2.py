# open and read the input file into a list of strings
input = open("day4/input.txt", "r").read().split()

# This is a list of the 4 diagonal directions in (dx, dy) format
directions = [(-1,-1), (1,-1), (-1,1), (1,1)]

# This is a list of strings we will match against later
matching_strings = ["MMSS", "MSMS", "SMSM", "SSMM"]

# A simple function to bounds check the x,y values and if in range
# return the char at that location in the input
def getchar(x,y):
    global maxx, maxy, input
    if 0 <= x < maxx and 0 <= y < maxy:
        return(input[y][x])
    else:
        return("")

# Initialise some variables we'll use
maxy = len(input)
maxx = len(input[0])
matches = 0

# Search the input looking for an A which is the middle of the X
# shape. We ignore the edges because you can't make an X on the 
# edge of the grid. When we find an A we grab the chars in all
# four diagonals and make them into a string. We then compare
# the string with our list of matching strings and if it's in the
# list then we've found an X.
for y in range(1, maxy-1):
    for x in range(1, maxx-1):
        if getchar(x,y) == "A":
            thisstring = ""
            for d in directions:
                thisstring += getchar(x+d[0], y+d[1])

            if thisstring in matching_strings:
                matches += 1

print(f"Matches: {matches}")