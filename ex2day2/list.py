def is_safe(report):
    # Check if a report is strictly increasing or strictly decreasing
    increasing = all(report[i+1] >= report[i] for i in range(len(report)-1))
    decreasing = all(report[i+1] <= report[i] for i in range(len(report)-1))
    
    # Check if differences between adjacent levels are between 1 and 3
    for i in range(len(report)-1):
        if not (1 <= abs(report[i+1] - report[i]) <= 3):
            return False
    
    return increasing or decreasing

def is_safe_with_removal(report):
    # Check if removing one level results in a safe report
    for i in range(len(report)):
        # Remove the i-th element and check if the rest is safe
        new_report = report[:i] + report[i+1:]
        if is_safe(new_report):
            return True
    return False

def count_safe_reports(file_path):
    safe_count = 0
    
    # Read data from the file
    with open(file_path, 'r') as f:
        reports = [list(map(int, line.split())) for line in f.readlines()]
    
    for report in reports:
        if is_safe(report) or is_safe_with_removal(report):
            safe_count += 1
    
    return safe_count

# File path to your input data
file_path = 'text.txt'

# Run the function to count safe reports
safe_reports = count_safe_reports(file_path)
print(safe_reports)
