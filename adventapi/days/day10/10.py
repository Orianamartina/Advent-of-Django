from lib.input_handlers import read_lines
from lib.answer_display import print_answer

file_contents = read_lines("day10/10input.txt")


def get_sum_of_signal_strengths():
    signal_strengths = 0
    cicle = 0
    x = 1
    execution_amount = 0
    searched_cicles = [20, 60, 100, 140, 180, 220]

    for line in file_contents:
        x += execution_amount
        execution_amount = 0

        if line[0] == "n":
            cicle += 1
            if cicle in searched_cicles:
                signal_strengths += cicle * x
        else:
            for _ in range(2):
                cicle += 1
                if cicle in searched_cicles:
                    signal_strengths += cicle * x

                amount = int(line.split()[1])
                execution_amount = amount

    return signal_strengths


def tick_is_under_sprite(tick, sprite_position, row):
    row = 40 * row
    return tick in [(sprite_position - 1 + row), (sprite_position + row), (sprite_position + 1 + row)]


def draw_crt():
    crt = [(["." for _ in range(40)]) for _ in range(6)]

    tick = 0
    sprite_position = 1

    for line in file_contents:
        if line[0] == "n":
            row = tick // 40
            column = tick % 40
            if tick_is_under_sprite(tick, sprite_position, row):
                crt[row][column] = "#"
            tick += 1
        else:
            for i in range(2):

                row = tick // 40
                column = tick % 40
                if tick_is_under_sprite(tick, sprite_position, row):
                    crt[row][column] = "#"
                tick += 1

            amount = int(line.split()[1])
            sprite_position += amount

    for i in range(6):
        print(crt[i]
              )


print_answer("10.1", get_sum_of_signal_strengths())
print_answer("10.2", "RKAZAJBR")
draw_crt()
