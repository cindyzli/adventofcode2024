import re

with open("day3/input.txt", "r") as file:
    lines = file.readlines()
str_lines = ','.join(lines)
# array_of_lines = [line.strip() for line in lines]


matches = re.findall(r"mul\(\d+,\d+\)|do\(\)|don't\(\)", str_lines)
print(matches)

ongoing = 0
should_do = True
for match in matches:
    if match == "don't()":
        should_do = False
    elif match == "do()":
        should_do = True
    else:
        if should_do:
            s = re.findall(r"\d+,\d+", match)
            vals = s[0].split(",")
            num1 = int(vals[0])
            num2 = int(vals[1])
            ongoing += num1 * num2
    
print(ongoing)


