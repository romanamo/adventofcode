group_packs = []

with open("input.txt", "r") as input_file:
    lines = list(map(lambda a: a.rstrip("\n"), input_file.readlines()))
    for i in range(0, len(lines), 3):
        group_packs.append((lines[i], lines[i+1], lines[i+2]))


items = []
for pack in group_packs:
    for c in pack[0]:
        if c in pack[1] and c in pack[2]:
            items.append(c)
            break

added = sum([ord(c) - 96 if c.islower() else ord(c) - 64 + 26 for c in items])
print(added)
