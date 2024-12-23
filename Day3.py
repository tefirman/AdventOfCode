
import re

def parse_mul(mul):
    vals = mul[4:-1].split(",")
    return int(vals[0]) * int(vals[-1])

with open("Day3Input.txt", "r") as file:
    corrupted = file.read()

do_ind = 0
dont_ind = 0
filtered = ""
while do_ind >= 0:
    dont_ind = corrupted.find("don't()",do_ind)
    filtered += corrupted[do_ind:dont_ind]
    do_ind = corrupted.find("do()",dont_ind)    

pattern = r'mul\([1-9][0-9]{0,2},[1-9][0-9]{0,2}\)'

num_valid = 0
product = 0
matches = re.finditer(pattern, filtered)
for match in matches:
    start, end = match.span()
    num_valid += 1
    product += parse_mul(match.group())

print(f"Number of valid multiplications: {num_valid}")
print(f"Total Product: {product}")



