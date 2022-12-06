total_list = []

with open("input.txt", "r") as input_file:
    lines = list(map(lambda a: a.rstrip("\n"), input_file.readlines()))

    sumz = 0
    for line in lines:
        if line == "":
            total_list.append(sumz)
            sumz = 0
        else:
            sumz += int(line)
    total_list.append(sumz)

added = sum(sorted(total_list, reverse=True)[0:3])
print(added)
