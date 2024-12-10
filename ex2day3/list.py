import re

# Read input from file (assuming the input is stored in "text.txt")
with open('text.txt', 'r') as file:
    input_text = file.read()

# Regular expression to match valid mul(X,Y) patterns
mul_pattern = r"mul\((\d+),(\d+)\)"

# Initialize the enabled flag for multiplications (True means enabled)
enabled = True
total = 0

# Search for all occurrences of 'do()', 'don't()', and 'mul(X,Y)'
for match in re.finditer(r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)", input_text):
    if match.group(0) == "do()":
        enabled = True  # Enable future multiplications
    elif match.group(0) == "don't()":
        enabled = False  # Disable future multiplications
    elif match.group(0).startswith("mul("):
        if enabled:
            # Extract numbers from mul(X, Y) and compute the multiplication
            x, y = int(match.group(1)), int(match.group(2))
            total += x * y  # Add the result of the multiplication to total

# Output the result
print(f"Total of enabled multiplications: {total}")
