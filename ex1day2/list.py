def is_safe(report):
    # Check if levels are either increasing or decreasing
    is_increasing = all(report[i] <= report[i+1] for i in range(len(report) - 1))
    is_decreasing = all(report[i] >= report[i+1] for i in range(len(report) - 1))
    
    if not (is_increasing or is_decreasing):
        return False
    
    # Check if the difference between adjacent levels is between 1 and 3
    for i in range(len(report) - 1):
        if not (1 <= abs(report[i] - report[i+1]) <= 3):
            return False
    
    return True

# Read input (assuming 'text.txt' contains the puzzle input)
with open('text.txt') as file:
    reports = [list(map(int, line.strip().split())) for line in file]

# Count the number of safe reports
safe_count = sum(1 for report in reports if is_safe(report))

print(safe_count)
