import re

# open and read the input file into a list of strings
line = open("day3/input.txt", "r").read()

total = 0

# Removes any text between don't() and d() from the input and returns it
# as modified_text. Also returns True or False indicating whether any text
# was removed so that this function can be called multiple times until all
# the don't()/do() sections have been removed.
def remove_dont_sections(text):
    modified_text = re.sub(r"don\'t\(\).*?do\(\)", "", text, flags=re.DOTALL)
    sections_removed = modified_text != text
    return(modified_text, sections_removed)

# Removes any text from the end of the text that starts with a don't() and
# ends at the end of the text
def remove_last_dont_section(text):
    return(re.sub(r"don\'t\(\).*?$", "", text, flags=re.DOTALL))

########
# MAIN #
########

# Remove all sections surrounded by don't() and do()
sections_removed = True
while sections_removed:
    (line, sections_removed) = remove_dont_sections(line)

# Remove any section at the end that starts with a 
# don't() but doesn't have a do() before the end of the input.
line = remove_last_dont_section(line)

# Process all mul(a,b) matches in the remaining string
matches = re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", line)
for match in matches:
    num1, num2 = int(match[0]), int(match[1])
    total += num1 * num2

print(f"Total: {total}")