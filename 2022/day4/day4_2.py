import re

pairs = []
duplicates = []

with open("input.txt", "r") as input_file:
    for lines in input_file.readlines():
        stripped = lines.rstrip("\n")
        items = re.split(",|-", stripped)
        items = list(map(lambda a: int(a), items))
        pairs.append(((items[0], items[1]), (items[2], items[3])))

for pair in pairs:
    overlaps = lambda a, b: a[1] >= b[0]
    if overlaps(pair[0], pair[1]) and overlaps(pair[1], pair[0]):
        duplicates.append(pair)

print(len(duplicates))
