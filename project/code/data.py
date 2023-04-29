"""
This module plays through every possible tic tac toe game sequence
to determine if the sequence results in the first player winning,
losing, or a draw. The results are then recorded in the `data/`
directory. Possible optimizations include accounting for reflections
and rotations of the board, but those are not accounted for here.


The results are:
    All: 362880
    Win: 212256 (58%)
    Lose: 104544 (29%)
    Draw: 46080 (13%)


Position win chance:
    +-------+-------+-------+
    | 0.375 | 0.25  | 0.375 |
    +-------+-------+-------+
    | 0.25  | 0.5   | 0.25  |
    +-------+-------+-------+
    | 0.375 | 0.25  | 0.375 |
    +-------+-------+-------+
"""
from itertools import permutations
from pathlib import Path

wins = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

outcomes = {
    "all": [],
    "draw": [],
    "lose": [],
    "win": []
}


class Player:
    def __init__(self, number: int):
        self.number = number
        self.positions = []

    def has_won(self):
        for win in wins:
            if all(p in self.positions for p in win):
                return True
        return False


play_sequences = permutations(range(0, 9))
for sequence in play_sequences:
    current_sequence = sequence
    outcomes["all"].append(current_sequence)
    player_1 = Player(1)
    player_2 = Player(2)
    current_player = player_1

    for turn in range(0, 9):
        position = sequence[0]
        sequence = sequence[1:]
        current_player.positions.append(position)

        # check for win
        if current_player.has_won():
            if current_player.number == 1:
                outcomes["win"].append(current_sequence)
            else:
                outcomes["lose"].append(current_sequence)
            break

        # switch players
        if current_player == player_1:
            current_player = player_2
        else:
            current_player = player_1

    # No winner and all positions taken, so it's a draw
    else:
        outcomes["draw"].append(current_sequence)


def record_outcomes(label, sequences):
    lines = []
    for seq in sequences:
        s = "".join([str(i) for i in seq])
        s += "\n"
        lines.append(s)
    fp = Path(__file__).parent / "data" / f"{label}.txt"
    with open(fp, "w") as f:
        f.writelines(lines)


for k, v in outcomes.items():
    record_outcomes(k, v)
