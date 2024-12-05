from collections import defaultdict
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

valid_orderings = 0
for page_ordering in page_orderings:
    pages = page_ordering.split(",")
    pages[-1] = pages[-1][:-1]
    print(pages)
    if len(pages) > 1:
        fails_if_seen = set()
        boo = True

        for p in pages:
            if p in fails_if_seen:
                boo = False
            for needed in last_before[p]:
                fails_if_seen.add(needed)

        if boo:
            n = int((len(pages) - 1)/2)
            middle_val = pages[n]
            valid_orderings +=  int(middle_val)


print(valid_orderings)
        
        




