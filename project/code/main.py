import abc
import functools
import pathlib
import random

WINS = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]


class Board:
    def __init__(self):
        self.positions = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        self.sequence = []

    def display(self):
        p = self.positions
        div = "+---+---+---+\n"
        r1 = f"| {p[0]} | {p[1]} | {p[2]} |\n"
        r2 = f"| {p[3]} | {p[4]} | {p[5]} |\n"
        r3 = f"| {p[6]} | {p[7]} | {p[8]} |\n"
        print(div + r1 + div + r2 + div + r3 + div)

    @property
    def available_positions(self):
        return [p for p in self.positions if isinstance(p, int)]

    def assign_position(self, position, symbol):
        self.positions[position] = symbol
        self.sequence.append(position)

    def is_full(self):
        return len(self.available_positions) == 0

    def has_win(self):
        for win in WINS:
            if self.positions[win[0]] == self.positions[win[1]] == self.positions[win[2]]:
                return True
        return False


class Player(abc.ABC):
    def __init__(self, symbol: str):
        self.symbol = symbol
        self.positions = []

    @abc.abstractmethod
    def get_position(self, board: Board) -> int:
        """Implement the logic for selecting a position"""


class Human(Player):
    def get_position(self, board):
        board.display()
        while True:
            position = int(input("Choose an available position: "))
            if position not in board.available_positions:
                print("That position is taken")
                continue
            else:
                break
        return position


class Random(Player):
    def get_position(self, board):
        position = random.choice(board.available_positions)
        print(f"Random selected position {position}.")
        return position


class AIEasy(Player):
    """Works toward a win if any remain, but is not optimized.
    It leverages a knowledge base of known winning game sequences.
    """

    @functools.cache
    def load_winning_sequences(self):
        """Knowledge base is compiled from the perspective of the first player.
        Therefore, the AI needs to choose appropriate game sequences depending on
        whether it goes first or second.

        This method is cached because it is called at every turn.
        """

        if self.symbol == "x":
            sequence_file_name = "win.txt"
        else:
            sequence_file_name = "lose.txt"
        fp = pathlib.Path(__file__).parent / "data" / sequence_file_name
        with open(fp, "r") as f:
            return [line.strip() for line in f.readlines()]

    def get_position(self, board: Board) -> int:
        current_sequence = "".join([str(i) for i in board.sequence])
        winning_sequences = self.load_winning_sequences()
        available_winning_sequences = [s for s in winning_sequences if s.startswith(current_sequence)]

        if available_winning_sequences:
            random_winning_sequences = random.choice(available_winning_sequences)
            next_move_index = len(current_sequence)
            return int(random_winning_sequences[next_move_index])
        else:
            return random.choice(board.available_positions)


class AIMedium(Player):
    """This bot prioritize winning moves.
    It leverages a knowledge base of winning game combinations.
    """

    def get_intersection(self, l1, l2):
        return [i for i in l1 if i in l2]

    def get_difference(self, l1, l2):
        return [i for i in l1 if i not in l2]

    def get_opponent_symbol(self):
        if self.symbol == "x":
            return "o"
        return "x"

    def get_position(self, board: Board) -> int:
        # Begin randomly
        if not self.positions:
            position = random.choice(board.available_positions)
            self.positions.append(position)
            return position
        # Filter out any wins opponent is working on
        possible_wins = []
        for win in WINS:
            if not any([board.positions[p] == self.get_opponent_symbol() for p in win]):
                possible_wins.append(win)
        for win in possible_wins:
            # if already have 2 positions, choose winning position
            if len(self.get_intersection(win, self.positions)) == 2:
                position = self.get_difference(win, self.positions)[0]
                self.positions.append(position)
                return position
        for win in possible_wins:
            # Continue working on the first win in progress
            if len(self.get_intersection(win, self.positions)) == 1:
                position = random.choice(self.get_difference(win, self.positions))
                self.positions.append(position)
                return position
        position = random.choice(board.available_positions)
        self.positions.append(position)
        return position


class AIHard(Player):
    """This bot prioritize winning moves and blocks opponent wins.
    It leverages a knowledge base of winning game combinations.
    """

    def get_intersection(self, l1, l2):
        return [i for i in l1 if i in l2]

    def get_difference(self, l1, l2):
        return [i for i in l1 if i not in l2]

    def get_opponent_symbol(self):
        if self.symbol == "x":
            return "o"
        return "x"

    def get_opponent_positions(self, positions):
        opponent_symbol = self.get_opponent_symbol()
        opponent_positions = []
        for position, symbol in enumerate(positions):
            if symbol == opponent_symbol:
                opponent_positions.append(position)
        return opponent_positions

    def get_position(self, board: Board) -> int:
        # Begin randomly
        if not self.positions:
            position = random.choice(board.available_positions)
            self.positions.append(position)
            return position
        # Filter out any wins opponent is working on
        possible_wins = []
        opponent_wins = []
        opponent_positions = self.get_opponent_positions(board.positions)
        for win in WINS:
            if self.get_intersection(win, opponent_positions):
                opponent_wins.append(win)
            else:
                possible_wins.append(win)
        # Block opponents win
        for win in opponent_wins:
            if len(self.get_intersection(win, opponent_positions)) == 2:
                position = self.get_difference(win, opponent_positions)[0]
                if position not in board.available_positions:
                    continue
                self.positions.append(position)
                return position
        for win in possible_wins:
            # if already have 2 positions, choose winning position
            if len(self.get_intersection(win, self.positions)) == 2:
                position = self.get_difference(win, self.positions)[0]
                self.positions.append(position)
                return position
        for win in possible_wins:
            # Continue working on the first win in progress
            if len(self.get_intersection(win, self.positions)) == 1:
                position = random.choice(self.get_difference(win, self.positions))
                self.positions.append(position)
                return position
        position = random.choice(board.available_positions)
        self.positions.append(position)
        return position


class Game:
    def __init__(self):
        self.board = Board()
        self.player_x = Human("x")
        self.player_o = AIHard("o")
        self.current_player = self.player_x

    def switch_players(self):
        if self.current_player == self.player_x:
            self.current_player = self.player_o
        else:
            self.current_player = self.player_x

    def announce_winner(self):
        self.board.display()
        print(f"Player {self.current_player.symbol} wins!")

    def announce_draw(self):
        self.board.display()
        print("The game ended in a draw.")

    def play(self):
        while True:
            position = self.current_player.get_position(self.board)
            self.board.assign_position(position, self.current_player.symbol)
            if self.board.has_win():
                self.announce_winner()
                break
            if self.board.is_full():
                self.announce_draw()
                break
            self.switch_players()


if __name__ == '__main__':
    game = Game()
    game.play()
