"""
Chess game controller class.

Author: Steve Matsumoto <stephanos.matsumoto@sporic.me>
"""

import chess_board


class ChessController:
    """
    A controller that stores the board and view and translates input from the
    user into moves on the board.

    Attributes:
        board: the chess board model.
        view: the view of the board.
    """

    def __init__(self):
        """
        Create an instance of the controller.
        """
        # Create a new chess board.

        # Create a view of this board.
        pass

    def translate_coordinates(self, square, column=None):
        """
        Translate coordinates given in one of several formats into a pair of
        integers.

        The coordinates may be given in algebraic notation, such as the string
        "1d", as a pair of integers (0, 4), or as two separate integer arguments
        0, 4.

        Args:
            square: a generic argument representing one or both coordinates.
            column: an optional argument representing the column/file if square
                only represented the rank.

        Returns:
            A tuple of three elements, with the first two elements representing
            the row and column on the board, and the last element representing
            whether square contained one or both coordinates.

        Raises:
            ValueError: either of the resulting coordinates are out of the board
            range, or the input mixed and matched encodings (e.g., square was a
            string and column was provided).
        """
        pass

    def run(self):
        """
        Run the main loop that displays the board, gets user input, and tries
        to make the change to the board.

        Returns:
            None.
        """
        # While neither side is in checkmate, display the board and give a
        # prompt about whose turn is it, like "white>" or "black>".

        # Get user input. This may be in algebraic chess notation, a set of two
        # tuples representing the starting and ending ranks and files, or a
        # set of four integers representing the starting and ending ranks and
        # files.

        # Check whether the desired move is legal. If not, display an error
        # message and repeat the prompt for the current player. Otherwise,
        # make the move and loop back to the beginning of this function.
        pass
