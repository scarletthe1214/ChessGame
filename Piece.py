class Piece:
    """
    Represents a generic chess piece and contains
    common interface methods for various types of pieces.
    """

    def __init__(self):
        """
        initialize piece
        """

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
        Find if any piece is on end square to decide if this move is capture or not
        If it is capture, update board by removing the captured piece on end square
        Put start piece into the end square
        :param start: start square of the piece
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: void
        """
        pass


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
        pass


class Rook(Piece):
    """
    Represents Rook Piece and contains Rook's implementation of general behaviors
    """

    def is_move_eligible(self, start, end, board):
        """
        King can move 1 space in any direction, but cannot jump pieces.
        :param start: start square of the piece
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: True if move is valid, otherwise false
        """
        pass


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
        pass


class Knight(Piece):
    """
    Represents Knight Piece and contains Knight's implementation of general behaviors
    """

    def is_move_eligible(self, start, end, board):
        """
        Bishop can move two spaces forward along the row or column
        and then one space to the left or right of where it lands.
        The Knight CAN jump over pieces.
        :param start: start square of the piece
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: True if move is valid, otherwise false
        """
        pass
