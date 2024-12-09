# open and read the input file into a single string
input = open("day9/input.txt", "r").read()

# We will start out with a list of files and spaces and then as we defrag we'll remove 
# from both files and spaces and append to moved_files
files = []
spaces = []
moved_files = []

# iterate the chars in the string and create from it a list of files and a list of spaces
# keeping track of the block number and file_id as we go
block = 0
is_file = True
file_id = 0
for c in input:
    size = int(c)
    if is_file:
        if size > 0:
            files.append((block, size, file_id))
            file_id += 1
    else:
        if size > 0:
            spaces.append((block, size))
    block += size
    is_file = not is_file

# Iterate through the list of spaces filling them up using files from the end of the drive
while len(spaces):
    # Grab data about the first space and the last file
    (free_start_block, free_size) = spaces[0]
    (last_file_start, last_file_size, last_file_id) = files[-1]

    if last_file_start < free_start_block:
        # We've finished defragging so remove this space entry
        del spaces[0]
    elif last_file_size < free_size:
        # Last file is smaller than the available space so reduce the size of the first
        # space, delete the last file and then append the entire moved file to the
        # end of moved_files
        spaces[0] = (free_start_block + last_file_size, free_size - last_file_size)
        del files[-1]
        moved_files.append((free_start_block, last_file_size, last_file_id))
    elif last_file_size == free_size:
        # Last file is the same size as the available space so remove the last file
        # and the first space and then append the entire file to moved_files
        del spaces[0]
        del files[-1]
        moved_files.append((free_start_block, last_file_size, last_file_id))
    else:
        # Last file is bigger than the available space so reduce the size of the
        # last file, remove the first space and then append the moved part of this
        # file to moved_files
        files[-1] = (last_file_start, last_file_size - free_size, last_file_id)
        del spaces[0]
        moved_files.append((free_start_block, free_size, last_file_id))

# Calculate the checksum by summing the products of block number and file ID
checksum = 0
for file in files + moved_files:
    for i in range(file[0], file[0] + file[1]):
        checksum += file[2] * i

print(f"Checksum: {checksum}")
