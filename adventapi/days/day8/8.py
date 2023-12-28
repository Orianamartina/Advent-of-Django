from lib.input_handlers import read_file, split_content
from lib.answer_display import print_answer

file_contents = read_file("day8/8input.txt")

contents = split_content(file_contents)
map_heigth = len(contents)
map_width = len(contents[0])


def set_up_matrix(content):
    matrix = []

    for _ in range(map_heigth):
        matrix.append([])

    return matrix


def format_content(content):
    matrix = set_up_matrix(content)

    for i in range(map_width):
        for j, line in enumerate(content):
            matrix[j].append(int(line[i]))

    return matrix


def check_if_visible(y, x, matrix):
    return (
        check_if_visible_from_bottom(y, x, matrix)
        or check_if_visible_from_top(y, x, matrix)
        or check_if_visible_from_left(y, x, matrix)
        or check_if_visible_from_right(y, x, matrix)
    )


def check_if_visible_from_left(y, x, matrix):
    return all(matrix[y][i] < matrix[y][x] for i in range(x))


def check_if_visible_from_right(y, x, matrix):
    return all(matrix[y][i] < matrix[y][x] for i in range(x + 1, len(matrix[0])))


def check_if_visible_from_top(y, x, matrix):
    return all(matrix[i][x] < matrix[y][x] for i in range(y))


def check_if_visible_from_bottom(y, x, matrix):
    return all(matrix[i][x] < matrix[y][x] for i in range(y + 1, len(matrix)))


def get_visible_trees(matrix):
    visible_trees = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if check_if_visible(i, j, matrix):
                visible_trees += 1

    return visible_trees


# ------
# Part 2
# ------
def get_highest_scenic_score(matrix):
    highest_score = 0
    scores = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            scores.append(get_score(i, j, matrix))
            if get_score(i, j, matrix) > highest_score:
                highest_score = get_score(i, j, matrix)

    return highest_score


def get_score(y, x, matrix):
    return (
        check_score_from_left(y, x, matrix)
        * check_score_from_right(y, x, matrix)
        * check_score_from_top(y, x, matrix)
        * check_score_from_bottom(y, x, matrix)
    )


def check_score_from_top(y, x, matrix):
    tree_heigth = matrix[y][x]
    score = 0
    for i in range(y - 1, -1, -1):
        if matrix[i][x] < tree_heigth:
            score += 1
        else:
            score += 1
            return score
    return score

def check_score_from_left(y, x, matrix):
    tree_heigth = matrix[y][x]
    score = 0
    for i in range(x - 1, -1, -1):
        if matrix[y][i] < tree_heigth:
            score += 1
        else:
            score += 1
            return score
    return score


def check_score_from_right(y, x, matrix):
    tree_heigth = matrix[y][x]
    score = 0
    for i in range(x + 1, map_width):
        if matrix[y][i] < tree_heigth:
            score += 1
        else:
            score += 1
            return score
    return score



def check_score_from_bottom(y, x, matrix):
    tree_heigth = matrix[y][x]
    score = 0
    for i in range(y + 1, map_heigth):
        if matrix[i][x] < tree_heigth:
            score += 1
        else:
            score += 1
            return score
    return score


matrix = format_content(contents)
# p1
print_answer("8.1", get_visible_trees(matrix))
# p2
print_answer("8.2", get_highest_scenic_score(matrix))
