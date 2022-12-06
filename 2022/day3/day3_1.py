splitted_lines = []

with open("input.txt", "r") as input_file:
    for lines in input_file.readlines():
        stripped = lines.rstrip("\n")
        splitted_lines.append((stripped[:int(len(stripped) / 2)], stripped[int(len(stripped) / 2):]))

items = []

for rucksack in splitted_lines:
    for c in rucksack[0]:
        if c in rucksack[1]:
            items.append(c)
            break

added = sum([ord(c)-96 if c.islower() else ord(c)-64+26 for c in items])
print(added)