import sympy as solver

# open and read the input file into a list of strings
input = open("day13/input.txt", "r").read().split("\n")

# Credit to Eric Veenendaal for this solution. He put me onto learning
# about sympy. I understand this solution now but I didn't come up with
# it. 
def solve_with_sympy(x1, y1, x2, y2, goal_x, goal_y):
    # Define the symbols
    a, b = solver.symbols('a b')

    # Define the equations
    eq1 = solver.Eq(x1 * a + x2 * b, goal_x)
    eq2 = solver.Eq(y1 * a + y2 * b, goal_y)

    # Solve the system of equations and produce a list of solution values
    solution = solver.solve((eq1, eq2), (a, b))

    # Pick out of the solution values only those that are integers
    if all(isinstance(val, solver.Integer) for val in solution.values()):
        return(int(solution[a]), int(solution[b]))

    return 0,0

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
        machine['Px'] = int(line_bits[1][2: -1])+10000000000000
        machine['Py'] = int(line_bits[2][2:])+10000000000000
machines.append(machine)

total = 0
for m in machines:
    (a, b) = solve_with_sympy(m['Ax'], m['Ay'], m['Bx'],m['By'],m['Px'],m['Py'])
    total += a*3 + b

print(f"Total: {total}")