# open and read the input file into a list of strings
input = open("day13/input.txt", "r").read().split("\n")

# Max button presses of 100 means we can just try all values of a, calculate the required 
# integer value of b based on a. # Return the first that gives the right answer.
def brute_force_solve(ax, ay, bx, by, px, py):
    for a in range(0, 101):
        b = (px - (a*ax)) // bx
        if (a * ax) + (b * bx) == px and (a * ay) + (b * by) == py:
            return(a, b)
    return(0, 0)

# Parse the input into machines list. Each machine is a dict.
machine = dict()
machines = []
for line in input:
    line_bits = line.split()
    if line == "":
        machines.append(machine)
        machine = dict()
    elif line_bits[0] == "Button":
        button = line_bits[1][0]
        machine[button + "x"] = int(line_bits[2][2:-1])
        machine[button + "y"] = int(line_bits[3][2:])
    elif line_bits[0] == "Prize:":
        machine['Px'] = int(line_bits[1][2: -1])
        machine['Py'] = int(line_bits[2][2:])
machines.append(machine)

# Solve each machine one by one.
total = 0
for m in machines:
    (a, b) = brute_force_solve(m['Ax'], m['Ay'], m['Bx'],m['By'],m['Px'],m['Py'])
    total += a*3 + b

print(f"Total: {total}")