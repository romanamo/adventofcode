table = [[] for i in range(0, 9)]
operation = []

with open("input.txt", "r") as input_file:
    tot_lines = input_file.readlines()
    for line in tot_lines[0:8]:
        i = 1
        while i < len(line):
            if line[i] != " ":
                table[int((i - 1) / 4)].append(line[i])
            i += 4

    for line in tot_lines[10:]:
        moves = line.split(" ")
        operation.append((int(moves[1]), int(moves[3]), int(moves[5][:-1])))

for stack in table:
    stack.reverse()

for op in operation:
    crates = []
    for i in range(op[0]):
        crates.append(*table[op[1] - 1][-1:])
        table[op[1] - 1].pop()
    crates.reverse()
    table[op[2] - 1].extend(crates)

unpack = "".join([stack[-1:][0] for stack in table])
print(unpack)