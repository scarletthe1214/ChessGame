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
