from enum import IntEnum

MOVE2SCORE = {"X": 1, "Y": 2, "Z": 3}
THEIR_MOVES = ["A", "B", "C"]
MY_MOVES = ["X", "Y", "Z"]


class Result(IntEnum):
    Lose = 0
    Tie = 3
    Win = 6


def get_result_1(their_move, my_move):
    result = Result.Lose

    if their_move == "A":
        if my_move == "X":
            result = Result.Tie
        elif my_move == "Y":
            result = Result.Win
        else:
            result = Result.Lose

    if their_move == "B":
        if my_move == "X":
            result = Result.Lose
        elif my_move == "Y":
            result = Result.Tie
        else:
            result = Result.Win

    if their_move == "C":
        if my_move == "X":
            result = Result.Win
        elif my_move == "Y":
            result = Result.Lose
        else:
            result = Result.Tie

    return result + MOVE2SCORE[my_move]


def get_result_2(their_move, result):
    result_score = 0
    if result == "X":
        my_move = MY_MOVES[THEIR_MOVES.index(their_move) - 1]
    elif result == "Y":
        result_score = 3
        my_move = MY_MOVES[THEIR_MOVES.index(their_move)]
    else:
        result_score = 6
        my_move = MY_MOVES[(THEIR_MOVES.index(their_move) + 1) % 3]

    return MOVE2SCORE[my_move] + result_score


def get_sol_1():
    with open("day_2_input.txt", "r") as f:
        lines = f.readlines()

    total_score = 0
    for line in lines:
        line = line.strip()
        their_move, my_move = line.split(" ")
        total_score += get_result_1(their_move, my_move)
    print(total_score)


def get_sol_2():
    with open("day_2_input.txt", "r") as f:
        lines = f.readlines()
    total_score = 0
    for line in lines:
        line = line.strip()
        their_move, result = line.split(" ")
        total_score += get_result_2(their_move, result)
    print(total_score)


def main():
    get_sol_1()
    get_sol_2()


if __name__ == "__main__":
    main()
