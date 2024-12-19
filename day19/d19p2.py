from functools import cache

# open and read the input file into a list of strings
input = open("day19/input.txt", "r").read().split("\n")
available_towels = [a.strip() for a in input[0].split(",")]
desired_patterns = input[2:]
longest_towel = max([len(a) for a in available_towels])

@cache
def match_towels(p):
    global available_towels
    variations = 0

    # If we get here then we matched the whole pattern
    if len(p) == 0: return(1)

    # Try the first i chars of the wanted pattern (p) looking for available towel matches
    # Try only as far as the longest towel. 
    for i in range(0, min(longest_towel, len(p))):
        if p[:i+1] in available_towels: variations += match_towels(p[i+1:])

    return(variations)

successful = 0
for pattern in desired_patterns:
    #print(f"{pattern}")
    successful += match_towels(pattern)

print(f"Successful: {successful}")