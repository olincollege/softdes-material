"""
Chess board view class.

Author: Steve Matsumoto <stephanos.matsumoto@sporic.me>
"""

import chess_board


class ChessView:
    """
    An abstract class that provides the structure for any view of the chess
    board.

    NOTE: This can actually be implemented as an abstract class, but I didn't
        do that here.

    Attributes:
        board: a ChessBoard instance representing the board to view.
    """

    def __init__(self, board):
        """
        Create an instance of the board view.

        Args:
            board: the ChessBoard to represent.
        """
        self.board = board

    def draw(self):
        """
        Draw a representation of the board.

        Returns:
            Depends on the representation.
        """
        pass


class ChessTextView(ChessView):
    """
    A textual representation of a chess board.
    """

    def __init__(self, board):
        """
        Create an instance of the board view.

        Args:
            board: the ChessBoard to represent.
        """
        # Just call the parent constructor.
        super().__init__(board)

    def draw(self):
        """
        Draw the text representation of the board.

        The representation looks something like this:

              **BLACK**

           a b c d e f g h
        8 |R|N|B|Q|K|B|N|R| 8
        7 |P|P|P|P|P|P|P|P| 7
        6 | | | | | | | | | 6
        5 | | | | | | | | | 5
        4 | | | | | | | | | 4
        3 | | | | | | | | | 3
        2 |p|p|p|p|p|p|p|p| 2
        1 |r|n|b|q|k|b|n|r| 1
           a b c d e f g h

              **white**

        Returns:
            A string representing the current board state.
        """
        # Set up the initial strings that are constant, like the top and bottom
        # three rows.

        # Loop through the board and turn each row into a text representation.

        # Combine the rows into a large string and return it.
        pass
