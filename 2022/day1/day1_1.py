with open("input.txt", "r") as input_file:
    lines = list(map(lambda a: a.rstrip("\n"), input_file.readlines()))

    max_sum = 0
    sum = 0
    for line in lines:
        if line == "":
            if sum > max_sum:
                max_sum = sum
            sum = 0
        else:
            sum += int(line)

print(max_sum)