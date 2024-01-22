from .lib.input_handlers import read_lines

file_contents = read_lines("advent_days/days/day_5_input.txt")

def solve(input = file_contents):

    boxes = []

    # Boxes setup
    for i in range(0, 8):
        boxes.append(input[i])


    def format_boxes():
        piles_of_boxes = []
        n = 1
        for i in range(9):
            new_line = []
            for line in boxes:
                if (line[n]) != " ":
                    new_line.append(line[n])
            n += 4
            piles_of_boxes.append(new_line)
        return piles_of_boxes


    # Instructions setup
    instructions = []
    for i in range(10, len(input)):
        inst = input[i].split(" ")
        guide = dict()
        guide[inst[0]] = int(inst[1])
        guide[inst[2]] = int(inst[3])
        guide[inst[4]] = int(inst[5][0])
        instructions.append(guide)


    piles_of_boxes = format_boxes()
    piles_of_boxes_p2 = format_boxes()
    for instruction in instructions:
        # setup
        quantity_to_move = instruction["move"]
        origin = instruction["from"] - 1
        destiny = instruction["to"] - 1

        # p1

        for i in range(quantity_to_move):
            moving_box = piles_of_boxes[origin].pop(0)
            piles_of_boxes[destiny].insert(0, moving_box)

        # p2

        moving_boxes = piles_of_boxes_p2[origin][0:quantity_to_move]
        piles_of_boxes_p2[origin] = piles_of_boxes_p2[origin][quantity_to_move:]
        piles_of_boxes_p2[destiny] = moving_boxes + piles_of_boxes_p2[destiny]


    answer_1 = ""

    for line in piles_of_boxes:
        answer_1 += line[0]

    # part 2

    answer_2 = ""

    for line in piles_of_boxes_p2:
        answer_2 += line[0]

    return {1: answer_1, 2: answer_2}