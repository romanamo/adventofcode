with open("input.txt", "r") as input_file:
    tree_matrix = [[int(item) for item in list(line)] for line in input_file.read().splitlines()]

    is_visible = lambda tree, others: tree > max(others, default=-1)

    visible = 0
    for y in range(len(tree_matrix)):
        for x in range(len(tree_matrix[y])):
            top = [tree_matrix[i][x] for i in range(0, y)]
            bottom = [tree_matrix[i][x] for i in range(y + 1, len(tree_matrix))]

            left = [tree_matrix[y][i] for i in range(0, x)]
            right = [tree_matrix[y][i] for i in range(x + 1, len(tree_matrix[y]))]

            if any([is_visible(tree_matrix[y][x], dir) for dir in [top, bottom, left, right]]):
                visible += 1

    print(visible)
