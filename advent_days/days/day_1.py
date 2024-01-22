from .lib.input_handlers import double_split_content, read_file


file_contents = read_file("advent_days/days/day_1_input.txt")


def solve(input=file_contents):
    number_groups = double_split_content(input)
    number_group_lists = [list(map(int, group.split())) for group in number_groups]
    maxCalories = 0
    for group in number_group_lists:
        calories = sum(group)
        if calories > maxCalories:
            maxCalories = calories

    top_calories = [0, 0, 0]

    for group in number_group_lists:
        calories = sum(group)
        for i in range(3):
            if calories > top_calories[i]:
                top_calories.insert(i, calories)
                top_calories = top_calories[:3]
                break

    return {1: str(maxCalories), 2: str(top_calories)}
