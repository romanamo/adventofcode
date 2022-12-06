guide_resolve = {("A", "X"): 1, ("B", "Y"): 2, ("C", "Z"): 3}
beats = {1: 3, 2: 1, 3: 2}
r_beats = dict([(val, key) for key, val in beats.items()])


def resolve(s: str):
    for key in guide_resolve.keys():
        if s == key[0] or s == key[1]:
            return guide_resolve[key]


def fight(you, enemy):
    e = resolve(enemy)
    if you == "Z":
        return r_beats[e] + 6
    if you == "X":
        return beats[e]
    else:
        return e + 3

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
