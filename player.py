class Player:
    def __init__(self, name, move_character) -> None:
        self.name = name
        self.move_character = move_character
        self.is_won = False
        self.is_turn = True if move_character == "O" else False

    def get_name_of_player(self) -> str:
        """
        Returns the name of player
        """

        return self.name

    def get_move_character(self) -> str:
        """
        Tells what move does the player play with
        """

        return self.move_character

    def get_player_turn(self) -> bool:
        """
        Tells whether it is this player's turn or not?
        """

        return self.is_turn

    def set_player_turn(self) -> bool:
        """
        sets the player turn as the reverse of what it is
        """

        self.is_turn = not self.is_turn

    def is_player_won(self):
        """
        Returns whether the player won or not
        """

        return self.is_won

    def set_player_won(self):
        """
        Sets the player as won
        """

        self.is_won = True

    def __repr__(self) -> str:
        return f"{self.name} playing with {self.get_move_character()}"
