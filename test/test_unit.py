from ward import test
from expycted import expect
from king_check import create_board, set_piece, move, Pawn

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
    expect(list(board.keys())).to.be_equal_to(["A", "B", "C", "D", "E", "F", "G", "H"])
    expect(len(board)).to.be_equal_to(8)
    for row in board.values():
        expect(len(row)).to.be_equal_to(8)
        expect(list(row.keys())).to.be_equal_to(["1", "2", "3", "4", "5", "6", "7", "8"])


@test('Specified piece is placed on board to defined coordinates')
def _():
    board = create_board()
    board = set_piece(board, ('A', '1'), 'pawn', 'white')

    expect(board['A']['1']).to.be_equal_to({'piece': 'pawn', 'color': 'white'})


@test("Pawn moves one step ahead from A2 to A1")
def _():
    board = create_board()
    board = set_piece(board, ('A', '2'), 'pawn', 'white')
    board, err = move(board, ('A', '2'), ('A', '1'))

    expect(board['A']['1']).to.be_equal_to({'piece': 'pawn', 'color': 'white'})
    expect(board['A']['2']).to.be_equal_to({})
    expect(err).to.be_falsey()


@test("Pawn wants to move diagonally from B2 to A1 but cannot, error is raised")
def _():
    board = create_board()
    board = set_piece(board, ('B', '2'), 'pawn', 'white')
    board, err = move(board, ('B', '2'), ('A', '1'))

    expect(board['B']['2']).to.be_equal_to({'piece': 'pawn', 'color': 'white'})
    expect(board['A']['1']).to.be_equal_to({})
    expect(err).to.be_truthy()
    expect(err).to.be_equal_to("Pawn cannot move from B2 to A1")


@test("Given Pawn is at starting position, it can move 2 steps ahead")
def _():
    expect(Pawn.validate_move(("A", "7"), ("A", "5"), color="black")[0]).to.be_true()
    expect(Pawn.validate_move(("A", "7"), ("A", "5"), color="black")[1]).to.be_equal_to(None)


@test("Given Pawn is at non-starting position, it can move 1 step ahead")
def _():
    expect(Pawn.validate_move(("A", "3"), ("A", "4"), color="white")[0]).to.be_true()
    expect(Pawn.validate_move(("A", "3"), ("A", "4"), color="white")[1]).to.be_equal_to(None)


@test("Given Pawn is at non-starting position, it can move 1 diagonally")
def _():
    expect(Pawn.validate_move(("A", "3"), ("B", "4"), color="white")[0]).to.be_true()
    expect(Pawn.validate_move(("A", "3"), ("B", "4"), color="white")[1]).to.be_equal_to(None)


@test("Given Pawn is at non-starting position, it cannot move 1 steps vertically")
def _():
    expect(Pawn.validate_move(("A", "3"), ("B", "3"), color="white")[0]).to.be_false()
    expect(Pawn.validate_move(("A", "3"), ("B", "3"), color="white")[1]).to.be_equal_to("Cannot move there")


@test("Determine if piece is at starting position")
def _():
    expect(Pawn.is_starting_position(("A", "2"), color="white")).to.be_true()
    expect(Pawn.is_starting_position(("A", "3"), color="white")).to.be_false()


# @test(f'Board cell with column index 0 and row index 0 is A1')
# def _():
#     board = create_board()
#     for row_idx in range(8):
#         for col_idx in range(8):
#             expect(board[row_idx][col_idx]['coord']).to.be_equal_to(coordinates[row_idx][col_idx])
