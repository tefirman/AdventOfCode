
import pandas as pd

# df = pd.read_csv('Day2Input.txt', sep=r'\s+', names=[f'reading{ind}' for ind in range(5)], header=None)
# Not all reports are the same length... Pandas dataframe won't work...

# Defining "safe" logic
def check_safe(report: list):
    diffs = [report[ind + 1] - report[ind] for ind in range(len(report) - 1)]
    increasing = all([diff_val >= 1 and diff_val <= 3 for diff_val in diffs])
    decreasing = all([diff_val <= -1 and diff_val >= -3 for diff_val in diffs])
    return increasing or decreasing

# Parsing input data
with open("Day2Input.txt","r") as file:
    reports = file.read().split("\n")[:-1]

# Looping through reports
num_safe = 0
for ind in range(len(reports)):
    report = [int(val) for val in reports[ind].split()]
    if check_safe(report):
        num_safe += 1
    else: # Applying dampener
        for ind in range(len(report)):
            dampened = report.copy()
            dampened.pop(ind)
            if check_safe(dampened):
                print(report)
                print(dampened)
                num_safe += 1
                break

# Printing final results
print(f"# of safe reports: {num_safe}")

