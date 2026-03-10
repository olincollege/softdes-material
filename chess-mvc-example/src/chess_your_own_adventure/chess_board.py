"""
Chess board class.

Author: Steve Matsumoto <stephanos.matsumoto@sporic.me>
"""

# Define various constants to make the code readable.
# NOTE: In a real implementation, these should be defined in an enum.
WHITE = 0
BLACK = 1
BOARD_WIDTH = 8
UNKNOWN_SQUARE = -2
EMPTY_SQUARE = -1
WHITE_PAWN = 0
BLACK_PAWN = 1
WHITE_KNIGHT = 2
BLACK_KNIGHT = 3
WHITE_BISHOP = 4
BLACK_BISHOP = 5
WHITE_ROOK = 6
BLACK_ROOK = 7
WHITE_QUEEN = 8
BLACK_QUEEN = 9
WHITE_KING = 10
BLACK_KING = 11
WHITE_PIECES = [WHITE_PAWN, WHITE_KNIGHT, WHITE_BISHOP, WHITE_ROOK, WHITE_QUEEN,
                WHITE_KING]
BLACK_PIECES = [BLACK_PAWN, BLACK_KNIGHT, BLACK_BISHOP, BLACK_ROOK, BLACK_QUEEN,
                BLACK_KING]


class ChessBoard:
    """
    A model of a chess board with standard chess pieces.

    NOTE: This board currently does not detect or allow draw via repetition.

    Attributes:
        next_turn: the color of the next player to move.
        squares: a two-dimensional list representing the pieces on each square
            of the board.
        white_in_check: whether the white king is in check.
        black_in_check: whether the black king is in check.
        white_king_moved: whether the white king has moved.
        white_a_rook_moved: whether the white rook in the "a" file has moved.
        white_h_rook_moved: whether the white rook in the "h" file has moved.
        black_king_moved: whether the black king has moved.
        black_a_rook_moved: whether the black rook in the "a" file has moved.
        black_h_rook_moved: whether the black rook in the "h" file has moved.
        en_passant: a set of squares that can be moved to for an en passant
            capture.
    """

    def __init__(self):
        """
        Create and set up a new chess board.
        """
        # Set the next turn to be white's, since white goes first.

        # Create the board as a list of lists, representing the squares of the
        # board. Initially, each square contains EMPTY.

        # Fill in the starting pieces of the board.

        # Set all of the moved variables to False.
        pass

    def is_white_square(self, rank, file):
        """
        Determine if a square is white or black.

        Compute and return whether a square on the board is white or black. This
        information is only used for rendering a graphical representation of the
        chess board.

        Args:
            rank: the row of the board to use, starting at 0, where the white
                side starts.
            file: the column of the board to use, starting at 0, which is closer
                to where the queen starts on each side.

        Returns:
            True if the square is white on a standard chess board, and False
            otherwise.

        Raises:
            ValueError: Either coordinate is outside of the board's range.
        """
        # Check if rank or file is negative or greater than 7, and raise an
        # exception if so.

        # Add the row and column together.

        # The square is black if this number is even and white if it's odd, so
        # return whether the number is odd or not.
        pass

    def get_possible_moves(self, rank, file):
        """
        Determine the possible moves of the piece at a given square.

        NOTE: this could be split into several functions depending on the piece.

        Args:
            rank: the rank of the square, starting at 0.
            file: the file of the square, starting at 0.

        Returns:
            A set representing the possible rank/file pairs that the piece there
            could move to.

        Raises:
            ValueError: Either coordinate is outside of the board's range, or
                the square is unoccupied or unknown.
        """
        # Check that the rank and file are valid coordinates, and that the
        # square is occupied. If not, raise an exception.

        # If the piece is a pawn and in its original row, it can move either one
        # or two rows towards the other side, as long as no piece blocks its
        # path, or it can capture diagonally forward in either direction (and
        # this capture may be en passant).

        # If the piece is a knight, it can move exactly three spaces away from
        # the starting rank and file, not in the same rank or file as the start
        # point, and cannot move to a square containing a piece of the same
        # color.

        # If the piece is a bishop, it can move an equal number of ranks and
        # files away from its starting space, as long as no piece exists in the
        # path between the start and end. The exception is if capturing (i.e.,
        # the move would be legal except that the end contains a piece of the
        # opposite color.

        # If the piece is a rook, it can change either its rank or its file, as
        # long as no piece exists in the path between start and end (unless
        # capturing).

        # If the piece is a queen, simply reuse the checks for bishop and rook.

        # If the piece is a king, check the squares that are exactly one space
        # away (the ending rank and file are both within one of the starting
        # rank and file without being the same as the start). The ending square
        # cannot contain a piece of the same color. The exception to the above
        # is castling, which has various requirements.
        pass

    def is_in_check(self, board, side):
        """
        Determine whether a side's king is in check.

        Args:
            board: a two-dimensional array representing a chess board of pieces.
            side: the target player's side.

        Returns:
            True if the given side is in check in the current board and False
            otherwise.

        Raises:
            ValueError: the board is the wrong size, it contains any invalid
                pieces, or the side (white/black) is invalid.
        """
        # Loop through the board. If any square is occupied by the opposing
        # side's pieces, find their possible moves and add it to a set. If a
        # square contains the current side's king, record this.

        # If the king is in any of the possible moves, then the king is in
        # check.
        pass

    def is_legal_move(self, start_rank, start_file, end_rank, end_file):
        """
        Determine whether moving a piece between two spaces is a legal move.

        Args:
            start_rank: the rank of the starting piece, starting at 0.
            start_file: the file  of the starting piece, starting at 0.
            end_rank: the desired ending rank of the piece, starting at 0.
            end_file: the desired ending file of the piece, starting at 0.

        Returns:
            True if the move is possible, and False otherwise.

        Raises:
            ValueError: Any coordinate is outside of the board's range.
        """
        # Find the legal moves from the starting rank and file.

        # Check that the ending rank and file is in the set of possible moves.
        # If not, the move is illegal.

        # If the current player's king is in check, create a copy of the board
        # as it would be if the move happened. Then see if the resulting board
        # is in check for the current player. If so, the move is illegal.

        # Otherwise, the move is legal.
        pass

    def move(self, start_rank, start_file, end_rank, end_file):
        """
        Move a piece if possible.

        Args:
            start_rank: the rank of the starting piece, starting at 0.
            start_file: the file  of the starting piece, starting at 0.
            end_rank: the desired ending rank of the piece, starting at 0.
            end_file: the desired ending file of the piece, starting at 0.

        Returns:
            True if the move is possible, and False otherwise.

        Raises:
            ValueError: Any coordinate is outside of the board's range.
        """
        # Check if the requested move is legal.

        # Move the piece, making any capture as necessary.

        # If the move was a pawn moving to the last rank of the opposing side,
        # promote it (requires player input).

        # Clear the en passant list. If the piece that just moved was a pawn and
        # it moved two spaces, record its relevant space as an en passant space.

        # Go through and find all the current player's pieces and their legal
        # moves. If the opposing king is in any of them, the other player is
        # now in check.

        # Switch the next move to the other player.
        pass
