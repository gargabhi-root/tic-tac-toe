

class ExceptionMessages:
    """
    Exception Messages that can be used by Exceptions
    """
    INVALID_ROW_NUMBER = "Row number can be either 0, 1 or 2"
    INVALID_COL_NUMBER = "Col number can be either 0, 1 or 2"
    INVALID_MOVE_EXCEPTION = lambda row, col: f"Invalid Move detected at {row},{col}"

class LogMessages:
    """
    Any Print messages can be given here
    """
    ASK_NAME = lambda move_character: f"Please tell me the name of the player playing with {move_character}\n"
    CURRENT_TURN = lambda name, move_character: f"It is {name}'s turn who is playing with {move_character}"
    ENTER_ROW = "Please enter the row - "
    ENTER_COL = "Please enter the col - "
    PLAYING_MOVE = lambda name, move_character, row, col: f"{name} is assigning {move_character} at {row},{col}"
    GAME_END = lambda is_result: f"Game has ended {'with a winner' if is_result else 'in a draw'}"
    WINNING_MESSAGE = lambda name: f"Congratulations {name} on winning the game"
