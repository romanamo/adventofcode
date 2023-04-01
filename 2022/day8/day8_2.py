with open("input.txt", "r") as input_file:
    tree_matrix = [[int(item) for item in list(line)] for line in input_file.read().splitlines()]
    total = list()
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    for y in range(len(tree_matrix)):
        for x in range(len(tree_matrix[y])):
            scenic = list()
            for dir in directions:
                view = 1
                pos = [x + dir[0], y + dir[1]]
                while 0 <= pos[0] + dir[0] < len(tree_matrix[y]) and 0 <= pos[1] + dir[1] < len(tree_matrix) and \
                        tree_matrix[y][x] > tree_matrix[pos[1]][pos[0]]:
                    pos[0] += dir[0]
                    pos[1] += dir[1]
                    view += 1
                scenic.append(view)

            total.append(scenic[0] * scenic[1] * scenic[2] * scenic[3])

    print(max(total))
