from messages import ExceptionMessages

class InvalidRowNumberException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = ExceptionMessages.INVALID_ROW_NUMBER
        super().__init__(self.message, *args)

class InvalidColNumberException(Exception):
    def __init__(self, *args: object) -> None:
        self.message = ExceptionMessages.INVALID_COL_NUMBER
        super().__init__(self.message, *args)

class InvalidMoveException(Exception):
    def __init__(self, row, col, *args: object) -> None:
        self.message = ExceptionMessages.INVALID_MOVE_EXCEPTION(row=row, col=col)
        super().__init__(self.message, *args)    
