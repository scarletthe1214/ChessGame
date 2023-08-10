class ChessVar:
    """
    initializes game and provide methods to play game and provide feedback
    """

    def __init__(self):
        """
        An init method that initializes any data members:
        _board: initialize 8 * 8 size 2d array
            Fill in _board cells with pieces on start position
        _turn: white as 0, black as 1
        """
        pass

    def get_game_state(self):
        """
        returns current game state
        check _board if there is a king on row 8th and whether we should wait for black finishes
        :return: 'UNFINISHED', 'WHITE_WON', 'BLACK_WON', or 'TIE'.
        """
        pass

    def make_move(self, start, end):
        """
        check if start and end are in the board
        check if the piece on start square belongs to the player whose turn it is
        check if move is legal:
            find if any piece is on end square to decide if this move is capture or not
                if it is capture, call piece's capture to validate capture and make move,
                otherwise, call piece's move_without_capture to validate and make move
        update turn if move is legal
        :param start: start position of the piece being moved from
        :param end: target position of the piece being moved to
        :return: True if move is valid, otherwise False
        """
        pass
