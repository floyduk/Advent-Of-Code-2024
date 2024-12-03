import re

# open and read the input file into a list of strings
line = open("day3/input.txt", "r").read()

# Process all mul(a,b) matches in the string
total = 0
matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
for match in matches:
    num1, num2 = int(match[0]), int(match[1])
    total += num1 * num2

print(f"Total: {total}")