# Question 3

# Open the file
text_file = open("sample-file.txt", "r")
lines_in_file = text_file.readlines()
text_file.close()

# Create a dictionary to store the valid lines for duplicate detection
valid_lines = {}

# Create a dictionary to store the lowercase/no white space version of each line
identical_lines = {}

# Find valid lines and fill the dictionary
for i, original_line in enumerate(lines_in_file):
    line_number = i + 1

    # Make the lines lowercase and remove punctuation and empty white space
    cleaned_line = ""
    for character in original_line.lower():
        if ("a" <= character <= "z") or ("0" <= character <= "9"):
            cleaned_line += character

    if cleaned_line == "":
        continue  # Skip all the empty lines

    # Store the normalized version for printing later
    identical_lines[line_number] = cleaned_line

    if cleaned_line in valid_lines:
        valid_lines[cleaned_line].append(line_number)
    else:
        valid_lines[cleaned_line] = [line_number]

# Find the near-duplicate sets. Create a list to store them
near_duplicate_sets = []
for key in valid_lines:
    if len(valid_lines[key]) > 1:
        near_duplicate_sets.append(valid_lines[key])

# Print the number of near-duplicate sets
print("Number of near-duplicate sets:", len(near_duplicate_sets))
print()  # Print so there is an empty line between the outputs

# Print the first two sets with their respective line numbers, identical lines, and the original lines
first_two_sets = near_duplicate_sets[:2]

for i, dup_set in enumerate(first_two_sets):
    print(f"Near-duplicate set {i + 1}:")
    for line_number in dup_set:
        print(f"Line {line_number} -> {identical_lines[line_number]} | Original Line: {lines_in_file[line_number - 1].rstrip()}")
    print()  # Print an empty line between sets