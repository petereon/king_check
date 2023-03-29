from behave import *

board = {
    "A": {"0": {"figure": "king"}, "1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}},
    "B": {"0": {}, "1": {"figure": "pawn"}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}},
    "C": {"0": {}, "1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}},
    "D": {"0": {}, "1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}},
    "E": {"0": {}, "1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}},
    "F": {"0": {}, "1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}},
    "G": {"0": {}, "1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}},
    "H": {"0": {}, "1": {}, "2": {}, "3": {}, "4": {}, "5": {}, "6": {}, "7": {}},
}


@given("King is on A1")
def king_on_position():
    pass


@given("Pawn is on B3")
def pawn_on_position():
    pass


@when("Pawn moves on B2")
def pawn_moves_to_position():
    pass


@then("King is in check")
def assert_check():
    pass