
import re

def parse_mul(mul):
    vals = mul[4:-1].split(",")
    return int(vals[0]) * int(vals[-1])

with open("Day3Input.txt", "r") as file:
    corrupted = file.read()

# do_ind = 0
# while do_ind >= 0:
#     print("foo bar")

pattern = r'mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)'

num_valid = 0
product = 0
matches = re.finditer(pattern, corrupted)
for match in matches:
    start, end = match.span()
    num_valid += 1
    product += parse_mul(match.group())

print(f"Number of valid multiplications: {num_valid}")
print(f"Total Product: {product}")



