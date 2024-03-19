from games.tictactoe.action import TicTacToeAction
from games.tictactoe.player import TicTacToePlayer
from games.tictactoe.state import TicTacToeState


class HumanTicTacToePlayer(TicTacToePlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: TicTacToeState):
        state.display()
        print(f"Player {state.get_acting_player()}, choose a row: ")
        x = int(input())
        print(f"Player {state.get_acting_player()}, choose a column: ")
        y = int(input())

        while True:
            # noinspection PyBroadException
            try:
                return TicTacToeAction(x, y)
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: TicTacToeState):
        # ignore
        pass

    def event_end_game(self, final_state: TicTacToeState):
        # ignore
        pass
