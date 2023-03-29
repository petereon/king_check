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


coordinates = [
    ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8'],
    ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8'],
    ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8'],
    ['D1', 'D2', 'D3', 'D4', 'D5', 'D6', 'D7', 'D8'],
    ['E1', 'E2', 'E3', 'E4', 'E5', 'E6', 'E7', 'E8'],
    ['F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8'],
    ['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8'],
    ['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8'],
]


@test(f'Board cell with column index 0 and row index 0 is A1')
def _():
    board = create_board()
    for row_idx in range(8):
        for col_idx in range(8):
            expect(board[row_idx][col_idx]['coord']).to.be_equal_to(coordinates[row_idx][col_idx])
