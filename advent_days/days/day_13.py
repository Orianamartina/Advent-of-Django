from .lib.input_handlers import read_file, split_content, double_split_content
import ast

file_contents = read_file("advent_days/days/day_13_input.txt")

def solve(text_input = file_contents):

    contents = double_split_content(text_input)

    pairs = []
    for pair in contents:
        a = []
        for division in split_content(pair):
            a.append(ast.literal_eval(division))
        pairs.append(a)

    right_order_indexes = []

    def compare_list(a, b):
        if type(a) is int and type(b) is int:
            if a > b:
                return -1
            elif a == b:
                return 0
            else:
                return 1

        if type(a) is int:
            a = [a]
        if type(b) is int:
            b = [b]
        shortest_list = min(len(a), len(b))
        for i in range(shortest_list):
            is_ordered = compare_list(a[i], b[i])
            if is_ordered == 0:
                continue
            else:
                return is_ordered
        return compare_list(len(a), len(b))


    for i, pair in enumerate(pairs, start=1):
        if compare_list(*pair) == 1:
            right_order_indexes.append(i)


    # part 2
    packets = []
    for item in contents:
        for division in item.split("\n"):
            packets.append(ast.literal_eval(division))


    packets.append([[2]])
    packets.append([[6]])

    order = [packets[0]]

    for packet in packets:
        found = False
        for i, item in enumerate(order):
            compare = compare_list(packet, item)
            if compare == 1:
                order.insert(i, packet)
                found = True
                break
        if not found:
            order.append(packet)

    indexes = order.index([[2]]) * order.index([[6]])
    return({1:sum(right_order_indexes), 2:indexes})