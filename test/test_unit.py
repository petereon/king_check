from ward import test
from expycted import expect
from king_check import create_board

# Entities:
# - Board
# - Chess Piece
#   - King: K
#   - Queen: Q
#   - Rook: R
#   - Bishop: B
#   - Knight: N
#   - Pawn: P

# Value Objects:
# - Position

# Operational Behavior:
# - Position Change (Move)


@test('Board is a structure of 8 rows and 8 columns')
def _():
    board = create_board()
    expect(len(board)).to.be_equal_to(8)
    for row in board:
        expect(len(row)).to.be_equal_to(8)
