import numpy


def check_boundary(i):
    """
    check if i is between 0, 7
    :param i: coordinate
    :return: True if in boundary, otherwise False
    """
    if i < 0 or i >= 8:
        return False
    return True


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
        self._board = numpy.empty((8, 8), dtype=Piece)

        self._board[0][0] = King(0)
        self._board[0][7] = King(1)
        self._board[0][1] = Bishop(0)
        self._board[1][1] = Bishop(0)
        self._board[0][6] = Bishop(1)
        self._board[1][6] = Bishop(1)
        self._board[1][0] = Rook(0)
        self._board[1][7] = Rook(1)
        self._board[0][2] = Knight(0)
        self._board[1][2] = Knight(0)
        self._board[0][5] = Knight(1)
        self._board[1][5] = Knight(1)

        self._king_white = (0, 0)
        self._king_black = (0, 7)

        self._turn = 0

    def __repr__(self):
        result = ""
        for row in self._board:
            row_res = ""
            for ele in row:
                if ele is None:
                    row_res += "None "
                else:
                    row_res += type(ele).__name__ + "_" + str(ele.get_owner()) + " "
            result += str(row_res) + '\n'
        return result

    def get_game_state(self):
        """
        returns current game state
        check _board if there is a king on row 8th and whether we should wait for black finishes
        :return: 'UNFINISHED', 'WHITE_WON', 'BLACK_WON', or 'TIE'.
        """
        white_arrived = False
        black_arrived = False
        for i in range(8):
            piece = self._board[7][i]
            if type(piece) is King:
                if piece.get_owner() == 0:
                    white_arrived = True
                else:
                    black_arrived = True
        if white_arrived and black_arrived:
            return 'TIE'
        if black_arrived:
            return 'BLACK_WON'
        if white_arrived and self._turn == 1:
            return 'UNFINISHED'
        if white_arrived:
            return 'WHITE_WON'
        return 'UNFINISHED'

    def make_move(self, start, end):
        """
        Check if the game is UNFINISHED by calling self.get_game_state()
        check if start and end coordinates are in the board
        checking if move is valid and execute: call validate_and_execute_move on start piece
        :param start: start position of the piece being moved from
        :param end: target position of the piece being moved to
        :return: True if move is valid, otherwise False
        """
        from_y = 0
        from_x = 0
        to_y = 0
        to_x = 0
        try:
            from_y = ord(start[0]) - ord('a')
            from_x = ord(start[1]) - ord('1')
            to_y = ord(end[0]) - ord('a')
            to_x = ord(end[1]) - ord('1')
        except RuntimeError:
            print("invalid start, end string")

        if not self.get_game_state() == 'UNFINISHED':
            print("Game is finished!")
            return False
        if not (check_boundary(from_y) and check_boundary(from_x)
                and check_boundary(to_y) and check_boundary(to_x)):
            print("Move is not within board")
            return False
        return self.validate_and_execute_move((from_x, from_y), (to_x, to_y))

    def validate_and_execute_move(self, start, end):
        """
        check if there is a piece on start square and the piece belongs to the player whose turn it is

        Check if move is valid by calling piece.is_move_eligible
        to check eligibility of move for the specific type of piece

        check if piece on end square belongs to current player

        Store a copy of _board before executing move in case move is eligible for type of piece
        but causing either king in check

        Execute move on _board by calling start.move()
        update _king_black and _king_white if necessary

        Call self.is_any_king_in_check() to check if any king is in check by the move

        If kings are not in check, return True and update turn
        Otherwise, restore _board using previously stored copy of _board and return False

        :param start: tuple for start position of the piece being moved from
        :param end: tuple for target position of the piece being moved to
        :return: True if move is valid, otherwise False
        """
        piece = self._board[start[0]][start[1]]
        if piece is None:
            return False
        if piece.get_owner() != self._turn:
            return False

        end_piece = self._board[end[0]][end[1]]
        if end_piece is not None and end_piece.get_owner() == self._turn:
            return False

        if not piece.is_move_eligible(start, end, self._board):
            return False

        backup_board = numpy.copy(self._board)
        piece.move(start, end, self._board)
        if type(piece) is King:
            if piece.get_owner() == 0:
                self._king_white = end
            else:
                self._king_black = end
        if self.is_any_king_in_check():
            self._board = backup_board
            return False
        self._turn = 1 - self._turn
        return True

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
            king = self._board[location[0]][location[1]]
            opponent_color = 1 - king.get_owner()
            for i in range(8):
                for j in range(8):
                    piece = self._board[i][j]
                    if piece is not None and piece.get_owner() == opponent_color:
                        if piece.is_move_eligible((i, j), location, self._board):
                            return True
            return False

        return is_king_in_check(self._king_white) and is_king_in_check(self._king_black)


class Piece:
    """
    Represents a generic chess piece and contains
    common interface methods for various types of pieces.
    """

    def __init__(self, owner):
        """
        initialize Piece
        :param owner: 0 is white or 1 is black
        """
        self._owner = owner

    def get_owner(self):
        return self._owner

    def is_move_eligible(self, start, end, board):
        """
        Should be overwritten by each type of subClass
        Check if the move is eligible for the type of piece
        :param start: start square of the piece
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: True if move is valid, otherwise false
        """
        pass

    def move(self, start, end, board):
        """
        update board by removing any piece on end square
        Put start piece into the end square
        :param start: start square of the piece, assuming start is in board
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: void
        """
        board[end[0]][end[1]] = board[start[0]][start[1]]
        board[start[0]][start[1]] = None
        return


class King(Piece):
    """
    Represents King Piece and contains King's implementation of general behaviors
    """

    def is_move_eligible(self, start, end, board):
        """
        Find if move is eligible for king piece.
        King can move 1 space in any direction, but cannot jump pieces
        :param start: start square of the piece
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: True if move is valid, otherwise false
        """
        if abs(end[0] - start[0]) <= 1 and abs(end[1] - start[1]) <= 1:
            return True
        return False


class Rook(Piece):
    """
    Represents Rook Piece and contains Rook's implementation of general behaviors
    """

    def is_move_eligible(self, start, end, board):
        """
        The Rook can move only along the row or column of its current square and cannot jump over pieces.
        :param start: start square of the piece
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: True if move is valid, otherwise false
        """
        if start[0] != end[0] and start[1] != end[1]:
            return False
        if start[0] == end[0]:
            # assume moving along y axis
            stepY = 1 if start[1] < end[1] else -1
            y = start[1] + stepY
            while y != end[1]:
                if board[start[0]][y] is not None:
                    return False
        else:
            # assume moving along x axis
            stepX = 1 if start[0] < end[0] else -1
            x = start[0] + stepX
            while x != end[0]:
                if board[x][start[1]] is not None:
                    return False
        return True


class Bishop(Piece):
    """
    Represents Bishop Piece and contains Bishop's implementation of general behaviors
    """

    def is_move_eligible(self, start, end, board):
        """
        Bishop can only move along the diagonal spaces of its current square
        and cannot jump over pieces
        :param start: start square of the piece
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: True if move is valid, otherwise false
        """
        if abs(start[0] - end[0]) != abs(start[1] - end[1]):
            return False
        stepX = 1 if start[0] < end[0] else -1
        stepY = 1 if start[1] < end[1] else -1
        x = start[0] + stepX
        y = start[1] + stepY
        while x != end[0] and y != end[1]:
            if board[x][y] is not None:
                return False
            x += stepX
            y += stepY
        return True


class Knight(Piece):
    """
    Represents Knight Piece and contains Knight's implementation of general behaviors
    """

    def is_move_eligible(self, start, end, board):
        """
        Knight can move two spaces forward along the row or column
        and then one space to the left or right of where it lands.
        The Knight CAN jump over pieces.
        :param start: start square of the piece
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: True if move is valid, otherwise false
        """
        dirs = [(2, 1), (-2, 1), (2, -1), (-2, -1), (1, 2), (-1, 2), (1, -2), (-1, -2)]
        for dir in dirs:
            if start[0] + dir[0] == end[0] and start[1] + dir[1] == end[1]:
                return True
        return False


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
#       Each move's eligibility will be determined using self.validate_and_execute_move() method,
#       which first calls each piece's is_move_eligible and then make the move to check if any king is in check.
#       Restore board and reject if invalid.
# 5. Determining if a capture is valid.
#       Same to move, capture's eligibility will be decided using self.validate_and_execute_move()
# 6. Determining whether a move places either king into check.
#       Call self.is_any_king_in_check(). for all opponent color's pieces, if any of them can capture the king,
#       then the king is in check. In other words, for all opponent color's pieces P,
#       if any P.is_move_eligible from P to King, then king is in check.
# 7. Determining the current state of the game.
#       call get_game_state to check _board if there is a king on row 8th and whether we should wait for black finishes
if __name__ == "__main__":
    game = ChessVar()
    print(game)
    move_result = game.make_move('c2', 'e3')
    print(move_result)
    print(game)
    print(game.make_move('g1', 'f1'))
    print(game)
    print(game.get_game_state())
