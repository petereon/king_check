from behave import *
from src.king_check import *


board = {
    "A": {"1": {"piece": "king", "color": "black"}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}, "8": {}},
    "B": {"1": {}, "2": {}, "3": {"piece": "pawn", "color": "white"}, "4": {}, "5": {}, "6": {}, "7": {}, "8": {}},
    "C": {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}, "8": {}},
    "D": {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}, "8": {}},
    "E": {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}, "8": {}},
    "F": {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}, "8": {}},
    "G": {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}, "8": {}},
    "H": {"1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}, "8": {}},
}


@given("a game board")
def game_board(context):
    context.board = create_board()


@given("King is on A1")
def king_on_position(context):
    context.board = set_piece(context.board, 'A', '1', "king", "black")


@given("Pawn is on B3")
def pawn_on_position(context):
    context.board = set_piece(context.board, 'B', '3', "pawn", "white")


@when("Pawn moves on B2")
def pawn_moves_to_position(context):
    context.board = move(context.board, 'B', '2', "pawn", "white")


@then("King is in check")
def assert_check(context):
    assert is_check(context.board)
