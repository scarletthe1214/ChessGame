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
        _king_black: tuple of black king's coordinate
        _king_white: tuple of white king's coordinate
        """
        self._king_white = (0, 0)
        self._king_black = (0, 7)
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
        Check if the game is UNFINISHED by calling self.get_game_state()
        check if start and end coordinates are in the board
        check if the piece on start square belongs to the player whose turn it is
        checking if move is valid: call is_move_valid on start piece
        update turn if move has been executed
        :param start: start position of the piece being moved from
        :param end: target position of the piece being moved to
        :return: True if move is valid, otherwise False
        """
        pass

    def is_move_valid(self, start, end):
        """
        Check if move is valid by calling start.is_move_eligible
        to check eligibility of move for the specific type of piece

        Store a copy of _board before executing move in case move is eligible for type of piece
        but causing either king in check

        Execute move on _board by calling start.move()
        update _king_black and _king_white if necessary

        Call self.is_any_king_in_check() to check if any king is in check by the move

        If kings are not in check, return True
        Otherwise, restore _board using previously stored copy of _board and return False

        :param start: start position of the piece being moved from
        :param end: target position of the piece being moved to
        :return: True if move is valid, otherwise False
        """

    def is_any_king_in_check(self):
        """
        Check if any king is in check by checking both sides' kings
        Use class member _king_white & _king_black and is_king_in_check inner method
        :return: True if any king is in check, otherwise False
        """

        def is_king_in_check(location):
            """
            check if the king is in check:
            for all opponent color's pieces, if any of them can capture the king,
            then the king is in check. In other words, for all opponent color's pieces P,
            if any is_move_eligible from P to King, then king is in check.
            * note: all opponent color's pieces can be found by iterating _board 2D-array
            :param location: tuple of king's coordinates
            :return: True if the king is in check, otherwise False
            """
            pass

        return is_king_in_check(self._king_white) and is_king_in_check(self._king_black)

# DETAILED TEXT DESCRIPTIONS OF HOW TO HANDLE THE SCENARIOS
# 1. Initializing the ChessVar class
#       __init__() will initialize 8 * 8 size 2d array _board and fill in _board cells with initialized pieces from
#       King, Rook, Bishop, and Knight classes, corresponding to the beginning state in real chess board.
#       It also includes following members to keep track of game states:
#           _turn: white as 0, black as 1
#           _king_black: tuple of black king's coordinate
#           _king_white: tuple of white king's coordinate
# 2. Keeping track of turn order.
#       Turn order will be tracked using an integer, 0 as white, 1 as black. After each move, turn will be flipped
# 3. Keeping track of the current board position.
#       Board position will be stored in _board 2d array where each cell will have instance of corresponding piece
#       in the real chess board.
# 4. Determining if a regular move is valid.
#       Each move's eligibility will be determined using self.is_move_valid() method, which first calls each piece's
#       is_move_eligible and then make the move to check if any king is in check. Restore board and reject if invalid.
# 5. Determining if a capture is valid.
#       Same to move, capture's eligibility will be decided using self.is_move_valid()
# 6. Determining whether a move places either king into check.
#       Call self.is_any_king_in_check(). for all opponent color's pieces, if any of them can capture the king,
#       then the king is in check. In other words, for all opponent color's pieces P,
#       if any P.is_move_eligible from P to King, then king is in check.
# 7. Determining the current state of the game.
#       call get_game_state to check _board if there is a king on row 8th and whether we should wait for black finishes
