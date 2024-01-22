from .lib.input_handlers import read_file, split_content

file_contents = read_file("advent_days/days/day_3_input.txt")

def solve(input=file_contents):
    contents = split_content(input)
    item_types = "_abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    total_priority = 0
    for content in contents:
        length = len(content)
        firstHalf = content[: length // 2]
        secondHalf = content[length // 2 :]
        foundItem = list(set(firstHalf).intersection(secondHalf))
        total_priority += item_types.index(foundItem[0])

    ## part 2: divide into groups of three
    total_badge_priority = 0

    for i in range(0, len(contents), 3):
        group = contents[i : i + 3]
        repeating_char = list(set(group[0]).intersection(*group[1:]))
        total_badge_priority += item_types.index(repeating_char[0])

    return {1: str(total_priority), 2: str(total_badge_priority)}
