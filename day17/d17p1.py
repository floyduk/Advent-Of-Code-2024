# open and read the input file into a list of strings
input = open("day17/input.txt", "r").read().split("\n")

# Function to handle combo operators and return the literal value or register value
def combo_operator(operand):
    if operand <= 3:
        return operand
    elif operand == 4:
        return A
    elif operand == 5:
        return B
    elif operand == 6:
        return C
    else:
        print(f"ERROR: Operand = {operand}")

# Read in the input and initialize the A, B, C register values
A, B, C, program, IP = 0, 0, 0, [], 0
for line in input:
    if line == "": continue
    part1, part2 = line.split(": ")
    if part1 == "Register A": A = int(part2)
    if part1 == "Register B": B = int(part2)
    if part1 == "Register C": C = int(part2)
    if part1 == "Program": program = [int(a) for a in part2.split(",")]

output = []
jumpbacks = 0
while True:
    instruction, operand = program[IP], program[IP+1]

    if instruction == 0:                # adv
        A = A // pow(2, combo_operator(operand))
    elif instruction == 1:              # bxl
        B = B ^ operand
    elif instruction == 2:              # bst
        B = combo_operator(operand) % 8
    elif instruction == 3:              # jnz
        if A != 0: IP = operand - 2
    elif instruction == 4:              # bxc
        B = B ^ C
    elif instruction == 5:              # out
        output.append(combo_operator(operand) % 8)
    elif instruction == 6:              # bdv
        B = A // pow(2, combo_operator(operand))
    elif instruction == 7:              # cdv
        C = A // pow(2, combo_operator(operand))
    
    IP += 2
    if IP >= len(program):              # HALT on reading past the end of program
        break

print("Program: ", ','.join(map(str, program)))
print("Output:  ", ','.join(map(str, output)))