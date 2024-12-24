
import numpy as np

with open("Day4Input.txt","r") as file:
    grid = np.array([list(row) for row in file.read().split("\n")[:-1]])

keyword = "XMAS"
rows = "\n".join(["".join(row) for row in grid])
right = rows.count(keyword)
left = rows.count(keyword[::-1])
cols = "\n".join(["".join(col) for col in grid.T])
down = cols.count(keyword)
up = cols.count(keyword[::-1])

print(f"Right matches: {right}")
print(f"Left matches: {left}")
print(f"Down matches: {down}")
print(f"Up matches: {up}")

matches = right + left + down + up

down_right = 0
down_left = 0
up_right = 0
up_left = 0
for row in range(grid.shape[0]):
    for col in range(grid.shape[1]):
        diags = [""]*len(keyword)
        for offset in range(len(keyword)):
            if row + offset < grid.shape[0] and col + offset < grid.shape[1]:
                diags[0] += grid[row + offset,col + offset]
            if row + offset < grid.shape[0] and col - offset >= 0:
                diags[1] += grid[row + offset,col - offset]
            if row - offset >= 0 and col + offset < grid.shape[1]:
                diags[2] += grid[row - offset,col + offset]
            if row - offset >= 0 and col - offset >= 0:
                diags[3] += grid[row - offset,col - offset]
        if diags[0] == keyword:
            # print(f"Down-right: {row}, {col}")
            down_right += 1
        if diags[1] == keyword:
            # print(f"Down-left: {row}, {col}")
            down_left += 1
        if diags[2] == keyword:
            # print(f"Up-right: {row}, {col}")
            up_right += 1
        if diags[3] == keyword:
            # print(f"Up-left: {row}, {col}")
            up_left += 1
        matches += diags.count(keyword)

print(f"Down Right matches: {down_right}")
print(f"Down Left matches: {down_left}")
print(f"Up Right matches: {up_right}")
print(f"Up Left matches: {up_left}")

print(f"{keyword} matches: {matches}")

# Part Two: X-MAS

# rows_a,cols_a = np.where(grid[1:-1,1:-1] == "A")
# rows_a += 1
# cols_a += 1

# print(rows_a)
# print(cols_a)

def check_x(grid, row, col):
    if grid[row,col] == "A":
        checks = [grid[row - 1,col - 1] == "M" and grid[row + 1,col + 1] == "S",
        grid[row - 1,col + 1] == "M" and grid[row + 1,col - 1] == "S",
        grid[row + 1,col - 1] == "M" and grid[row - 1,col + 1] == "S",
        grid[row + 1,col + 1] == "M" and grid[row - 1,col - 1] == "S"]
        if sum(checks) == 2:
            return True
    return False

num_x = 0
for row in range(1,grid.shape[0] - 1):
    for col in range(1,grid.shape[1] - 1):
        if check_x(grid, row, col):
            num_x += 1

print(f"X-MAS matches: {num_x}")

