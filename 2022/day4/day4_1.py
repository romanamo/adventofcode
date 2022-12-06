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
    contains = lambda a, b: a[0] <= b[0] <= b[1] <= a[1]
    if contains(pair[0], pair[1]) or contains(pair[1], pair[0]):
        duplicates.append(pair)

print(len(duplicates))
