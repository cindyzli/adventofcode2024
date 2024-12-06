from collections import defaultdict
import random 
with open("day5/input.txt", "r") as file:
    lines = file.readlines()


last_before = defaultdict(list)
page_orderings = []
for line in lines:
    if "|" in line:
        l = line.split("|")
        last_before[l[1][:-1]].append(l[0])
    else:
        page_orderings.append(line)

bad_lines = []
for page_ordering in page_orderings:
    pages = page_ordering.split(",")
    if '\n' in pages[-1]:
        pages[-1] = pages[-1][:-1]
    if len(pages) > 1:
        fails_if_seen = set()
        boo = True

        for p in pages:
            if p in fails_if_seen:
                boo = False
            for needed in last_before[p]:
                fails_if_seen.add(needed)

        if not boo:
            bad_lines.append(pages)

middle_total = 0

for line in bad_lines:
    new_line = [0 for _ in range(len(line))]
    for i, l in enumerate(line):
        counter = 0
        for x in last_before[l]:
            if x in line:
                counter+= 1
        new_line[counter] = l
    middle_total += int(new_line[len(new_line)//2])


print(middle_total)


    



        