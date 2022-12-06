guide_resolve = {("A", "X"): (1, 3), ("B", "Y"): (2, 1), ("C", "Z"): (3, 2)}


def resolve(s: str):
    for key in guide_resolve.keys():
        if s == key[0] or s == key[1]:
            return guide_resolve[key]


def fight(you, enemy):
    you = resolve(you)
    enemy = resolve(enemy)
    if you[1] == enemy[0]:
        return you[0] + 6
    elif enemy[1] == you[0]:
        return you[0]
    return you[0] + 3


scores = []
moves = []

with open("input.txt", "r") as input_file:
    lines = list(map(lambda a: a.rstrip("\n"), input_file.readlines()))
    for line in lines:
        parts = line.split(" ")
        moves.append((parts[0], parts[1]))

for move in moves:
    scores.append(fight(move[1], move[0]))

print(sum(scores))
