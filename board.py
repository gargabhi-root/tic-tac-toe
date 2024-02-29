# tic tac toe...
from player import Player
from messages import LogMessages
from exceptions import InvalidColNumberException, InvalidMoveException, InvalidRowNumberException

class Board:
    valid_moves = ["O", "X"]
    ROWS = 3
    COLS = 3
    empty_char = "-"

    def __init__(self) -> None:
        self.reset_and_start_game()
    
    def assign_player(self, player, is_player_one=True) -> None:
        """
        Assigns the p1 or p2 depending on is_player_one boolean
        """

        if is_player_one:
            self.p1 = player
        else:
            self.p2 = player
    
    def make_starting_board(self)->None:
        """
        Resets the board with all empty_char
        empty_char decided on the board denotes a vacant position
        """

        self.board = [[self.empty_char] * self.COLS for i in range(self.ROWS)]

    def reset_and_start_game(self) -> None:
        """
        Resets the game board, players and starts the game
        """

        self.make_starting_board()
        self.p1 = None
        self.p2 = None
        self.run_game()

    def print_board(self) -> None:
        """
        Prints the board on the console with separators
        """
        for row in range(self.ROWS):
            for col in range(self.COLS):
                col_separator = " | " if col < 2 else "\n"
                print(self.board[row][col], end=col_separator )
            if row < 2: print("-----------")

    def get_player_whose_turn(self) -> Player:
        """
        Returns the player whose turn it is to play the move
        """

        if self.p1.get_player_turn():
            return self.p1
        return self.p2
    
    def get_player_who_won(self) -> Player:
        """
        Returns the player who won the game
        """

        if self.p1.is_player_won():
            return self.p1
        return self.p2

    def set_other_player_turn(self) -> None:
        """
        Sets the current turn player as False and other player's turn as True
        """

        self.p1.set_player_turn()
        self.p2.set_player_turn()

    def is_empty_slot_exists(self):
        """
        Checks whether there is an empty slot for the move or not?
        """

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.board[row][col] == self.empty_char:
                    return True
        
        return False

    def is_valid_move(self, row, col, move_character) -> bool:
        """
        Tells me that move_character at row, col is valid or not?
        """

        if (
            row >2 or
            row<0 or
            col > 2 or
            col<0 or
            move_character not in self.valid_moves
        ):
            return False
        
        return self.board[row][col] == self.empty_char

    def make_move(self, row, col) -> None:
        """
        Marks O or X on the board
        """

        current_player = self.get_player_whose_turn()
        move_character = current_player.get_move_character()
        if self.is_valid_move(row,col, move_character):
            self.board[row][col] = move_character
            self.set_other_player_turn()
        else:
            raise InvalidMoveException(row=row, col=col)

    def is_board_won(self)->bool:
        """
        Checks the board if it is either won by X or O
        """

        # logic for a particular char
        for move_character in self.valid_moves:
            # check row
            for row in range(self.ROWS):
                row_count = 0
                for col in range(self.COLS):
                    if self.board[row][col] == move_character:
                        row_count += 1
                if row_count == self.ROWS:
                    return True

            # check column
            for col in range(self.COLS):
                col_count = 0
                for row in range(self.ROWS):
                    if self.board[row][col] == move_character:
                        col_count += 1
                if col_count == self.COLS:
                    return True
            
            # forward diagnol check
            forward_diagnol_count = 0
            for row in range(self.ROWS):
                if self.board[row][row] == move_character:
                    forward_diagnol_count += 1
            if forward_diagnol_count == self.ROWS:
                return True
            
            #backward_diagnol_count
            col = 0 # iterator for col position
            backward_diagnol_count = 0
            for row in range(self.ROWS-1, -1, -1):
                if self.board[row][col] == move_character:
                    backward_diagnol_count += 1
                col += 1
            if backward_diagnol_count == self.ROWS:
                return True

        return False

    def game_end_logic(self, game_won=False) -> None:
        """
        Runs if the game is won by any player or board is wasted/exhausted
        Implemets a restart logic basis the user input.
        """

        print(LogMessages.GAME_END(is_result=game_won))
        self.print_board()
        
        if game_won:
            player_turn = self.get_player_who_won()
            print(LogMessages.WINNING_MESSAGE(name=player_turn.get_name_of_player()))

        valid_yes_or_no = False
        restart_game = False
        while not valid_yes_or_no:
            yes_or_no = input("Do you wish to restart? Press Y/N. (Press Q to quit) - ")
            if yes_or_no.lower() == "y":
                restart_game = True
                valid_yes_or_no = True
            elif yes_or_no.lower() == "n" or yes_or_no.lower() == "q":
                yes_or_no = False
                valid_yes_or_no = True
        if restart_game:
            self.reset_and_start_game()

    def run_game(self):
        game_won = False
        while True:
            if not self.p1 or not self.p2:
                p1_move_character = self.valid_moves[0]
                p1_name = input(LogMessages.ASK_NAME(move_character=p1_move_character))
                self.assign_player(
                    player=Player(name=p1_name, move_character=p1_move_character)
                )

                p2_move_character = self.valid_moves[1]
                p2_name = input(LogMessages.ASK_NAME(move_character=p2_move_character))
                self.assign_player(
                    player=Player(name=p2_name, move_character=p2_move_character),
                    is_player_one=False
                )

            if not self.is_empty_slot_exists():
                break
 
            self.print_board()

            player_turn = self.get_player_whose_turn()
            print(LogMessages.CURRENT_TURN(
                name=player_turn.get_name_of_player(),
                move_character=player_turn.get_move_character()
            ))

            is_valid_row_input = False
            while not is_valid_row_input:
                try:
                    row = int(input(LogMessages.ENTER_ROW))
                    if row < 0 or row > 2:
                        raise InvalidRowNumberException()
                    is_valid_row_input = True
                except ValueError:
                    print(ExceptionMessages.INVALID_ROW_NUMBER)
                except InvalidRowNumberException as ire:
                    print(ire.message)
            
            is_valid_col_input = False
            while not is_valid_col_input:
                try:
                    col = int(input(LogMessages.ENTER_COL))
                    if col < 0 or col > 2:
                        raise InvalidColNumberException()
                    is_valid_col_input = True
                except ValueError:
                    print(ExceptionMessages.INVALID_COL_NUMBER)
                except InvalidColNumberException as ice:
                    print(ice.message)

            print(LogMessages.PLAYING_MOVE(
                    name=player_turn.get_name_of_player(),
                    move_character=player_turn.get_move_character(),
                    row=row,
                    col=col
                )
            )
            
            try:
                self.make_move(row, col)
                if self.is_board_won():
                    game_won = True
                    player_turn.set_player_won()
                    break
            except InvalidMoveException as ime:
                print(ime.message)
        
        self.game_end_logic(game_won=game_won)
