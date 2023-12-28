from adventapi.days.lib.input_handlers import read_file, split_content


file_contents = read_file("adventapi/days/day_4_input.txt")


def solve(input=file_contents):
    pairs = split_content(input)
    # part 1
    contained_pairs = 0
    # part 2
    duplicates = 0

    for assignment in pairs:
        splitted_assignments = assignment.split(",")

        first_ranges = splitted_assignments[0].split("-")
        second_ranges = splitted_assignments[1].split("-")

        first_range_lower = int(first_ranges[0])
        first_range_higher = int(first_ranges[1])
        second_range_lower = int(second_ranges[0])
        second_range_higher = int(second_ranges[1])

        # part 1
        if (
            first_range_lower <= second_range_lower
            and first_range_higher >= second_range_higher
        ):
            contained_pairs += 1
        elif (
            first_range_lower >= second_range_lower
            and first_range_higher <= second_range_higher
        ):
            contained_pairs += 1

        # part 2
        first_work_list = list(range(first_range_lower, first_range_higher + 1))
        second_work_list = list(range(second_range_lower, second_range_higher + 1))

        if len(set(first_work_list).intersection(set(second_work_list))) > 0:
            duplicates += 1

    return {1: contained_pairs, 2: duplicates}
