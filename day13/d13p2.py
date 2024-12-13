import sympy as solver

# open and read the input file into a list of strings
input = open("day13/input.txt", "r").read().split("\n")

# Credit to Eric Veenendaal for this solution. He put me onto learning
# about sympy. I understand this solution now but I didn't come up with
# it. 
def solve_with_sympy(ax, ay, bx, by, px, py):
    # Define the symbols
    a, b = solver.symbols('a b')

    # Define the equations
    eq1 = solver.Eq(ax * a + bx * b, px)
    eq2 = solver.Eq(ay * a + by * b, py)

    # Solve the system of equations and produce a list of solution values
    solution = solver.solve((eq1, eq2), (a, b))

    # Pick out of the solution values only those that are integers
    if all(isinstance(val, solver.Integer) for val in solution.values()):
        return(int(solution[a]), int(solution[b]))

    return 0,0

# Credit to Phaul for this solution which is algebraic. He solved for the
# two equations and you get these neat equations for a and b. The numbers just
# drop out. The only extra work is to ensure that you only return the solutions
# that are whole numbers. Those that give decimals are the unsolvable machines.
def solve_with_algebra(ax, ay, bx, by, px, py):
    b = (py*ax - px*ay) / (by*ax - bx*ay)
    a = (py - by*b)/ay
    if a.is_integer() and b.is_integer():
        return(int(a),int(b))
    else:
        return(0,0)

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
    (a, b) = solve_with_algebra(m['Ax'], m['Ay'], m['Bx'],m['By'],m['Px'],m['Py'])
    total += a*3 + b

print(f"Total with algebra: {total}")

total = 0
for m in machines:
    (a, b) = solve_with_sympy(m['Ax'], m['Ay'], m['Bx'],m['By'],m['Px'],m['Py'])
    total += a*3 + b

print(f"Total with sympy: {total}")