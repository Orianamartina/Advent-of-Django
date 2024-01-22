from .lib.input_handlers import read_file, split_content

file_contents = read_file("advent_days/days/day_2_input.txt")

def solve(input=file_contents):
    scores = {
        "A": 1,
        "B": 2,
        "C": 3,
        "X": 1,
        "Y": 2,
        "Z": 3,
        "win": 6,
        "draw": 3,
        "loose": 0,
    }
    rounds = split_content(input)
    # El número de la derecha le gana al número a su izquierda
    figure_scores = [3, 1, 2, 3, 1]

    def winning_condition(opponent, player):
        return figure_scores[player] == (figure_scores[opponent + 1])

    score_1 = 0
    for round in rounds:
        opponent = round[0]
        player = round[2]
        if scores[opponent] == scores[player]:
            score_1 += scores["draw"]
        elif winning_condition(scores[opponent], scores[player]):
            score_1 += scores["win"]
        else:
            score_1 += scores["loose"]
        score_1 += scores[player]

    score_2 = 0
    for round in rounds:
        opponent = round[0]
        player = round[2]
        if scores[player] == 1:
            score_2 += figure_scores[scores[opponent] - 1]
        elif scores[player] == 2:
            score_2 += figure_scores[scores[opponent]] + scores["draw"]
        else:
            score_2 += figure_scores[scores[opponent] + 1] + scores["win"]

    return {1: str(score_1), 2: str(score_2)}
