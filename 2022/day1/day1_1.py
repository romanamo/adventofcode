with open("input.txt", "r") as input_file:
    lines = list(map(lambda a: a.rstrip("\n"), input_file.readlines()))

    max_sum = 0
    sumz = 0
    for line in lines:
        if line == "":
            if sumz > max_sum:
                max_sum = sumz
            sumz = 0
        else:
            sumz += int(line)
    if sumz > max_sum:
        max_sum = sumz
print(max_sum)