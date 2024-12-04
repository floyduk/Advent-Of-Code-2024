# open and read the input file into a list of strings
input = open("day4/input.txt", "r").read().split()

# This is the list of all 8 directions in (dx, dy) format
directions = [(1,0), (1,1), (0,1), (-1,1), (-1, 0), (-1,-1), (0,-1), (1,-1)]

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
matchstring = "XMAS"
matches = 0

# Search every char in the input looking for an X. When we find one
# we search in all 8 directions 1 char at a time comparing the char
# we find witht the next char in our matchstring "XMAS". break out of
# the for loop if a char doesn't match but if we get to the last char
# then add one to matches
for y in range(0, maxy):
    for x in range(0, maxx):
        if getchar(x,y) == "X":
            for d in directions:
                thisx, thisy = x, y
                for i in range(1,4):
                    thisx += d[0]
                    thisy += d[1]
                    if getchar(thisx, thisy) != matchstring[i]:
                        break
                    elif i == 3:
                        matches += 1

print(f"Matches: {matches}")