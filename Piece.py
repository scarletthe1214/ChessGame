class Piece:
    """
    Represents a generic chess piece and contains
    common interface methods for various types of pieces.
    """

    def move_without_capture(self, start, end, board):
        """
        check if move_without_capture is valid for the type of piece
            if valid, update board by putting piece into the end square and return true
            otherwise, return false
        :param start: start square of the piece
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: True if move is valid, otherwise false
        """
        pass

    def capture(self, start, end, board):
        """
        check if capture is valid for the type of piece
            if valid, update board by removing the captured piece on end square and
            putting piece into the end square and return true
            otherwise, return false
        :param start: start square of the piece
        :param end: end square of the piece
        :param board: reference to the game board 2-D list
        :return: True if move is valid, otherwise false
        """
        pass


class King(Piece):
    """
    Represents King Piece and contains King's implementation of general behaviors
    """

    def move_without_capture(self, start, end, board):
        pass

    def capture(self, start, end, board):
        pass


class Pawn(Piece):
    """
    Represents Pawn Piece and contains Pawn's implementation of general behaviors
    Also includes the method promote() specific to Pawn
    """

    def move_without_capture(self, start, end, board):
        pass

    def capture(self, start, end, board):

        pass

    def promote(self, target_piece, board):
        pass
