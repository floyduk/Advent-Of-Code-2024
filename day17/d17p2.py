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

def run_program(A, B, C, program):
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
        
    output = []
    IP = 0
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

    return(output)
    #return(','.join(map(str, output)))

# Read in the input and initialize the A, B, C register values
A, B, C, program, IP = 0, 0, 0, [], 0
for line in input:
    if line == "": continue
    part1, part2 = line.split(": ")
    if part1 == "Register A": A = int(part2)
    if part1 == "Register B": B = int(part2)
    if part1 == "Register C": C = int(part2)
    if part1 == "Program": program = [int(a) for a in part2.split(",")]

# This algorithm is 100% inspired by Cyphase who figured out how multiples of 8 each add an extra output 
# digit. This is deeply deeply clever but I didn't invent it. I *had* figured out that more digits in A caused
# more digits in the output and that likely it was multiples of 8 that caused it since there is mod 8 in the 
# instruction set. I was playing around with multiples of 8 to see if that was what was reliably adding a digit
# to the output. But it was slow going and I looked for hints.
def get_prev_As(A):
    if A == 0: return [1, 2, 3, 4, 5, 6, 7]
    return [A * 8 + x for x in [0, 1, 2, 3, 4, 5, 6, 7]]

A, tail_len = 0, 1
stack = [(a, tail_len) for a in get_prev_As(A)]
possible = []
while stack:
    A, tail_len = stack.pop()
    output = run_program(A, 0, 0, program)  

    # If the output is what we want then record A and carry on but don't add any more searches to the stach
    if output == program:
        possible.append(A)
    # Else if just the last digit is right then go up by a multiple of 8 and start searching all 8 remainders again
    elif output[-tail_len] == program[-tail_len]:
        stack.extend((a, tail_len + 1) for a in reversed(get_prev_As(A)))

# We want the smallest possible answer
print(min(possible))