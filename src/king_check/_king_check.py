from cytoolz.dicttoolz import assoc_in  # type: ignore
from cytoolz.dicttoolz import get_in as weird_get_in
from typing import Any, Dict, Union, cast, Iterable


def get_in(d: dict, keys: Iterable[str]) -> dict:
    return cast(dict, weird_get_in(keys, d))


BoardType = dict[str, dict]
CoordType = tuple[str, str]


class Piece:
    def validate_move(self, from_coord: CoordType, to_coord: CoordType):  # type: ignore
        pass


class Pawn(Piece):
    def is_starting_position(self, coord):  # type: ignore
        pass

    def validate_move(self, from_coord: CoordType, to_coord: CoordType):  # type: ignore
        pass


def char_range(c1: str, c2: str) -> list[str]:
    """Generates the characters from `c1` to `c2`, inclusive."""
    return [chr(c) for c in range(ord(c1), ord(c2) + 1)]


def create_board() -> dict[str, dict]:
    row: dict[str, dict] = {str(i): {} for i in range(1, 9)}
    return {i: row for i in char_range('A', 'H')}


def set_piece(board: BoardType, coord: CoordType, piece: str, color: str) -> BoardType:
    return cast(Dict[str, Dict[Any, Any]], assoc_in(board, coord, {'piece': piece, 'color': color}))


def move(board: BoardType, coord_from: CoordType, coord_to: CoordType) -> tuple[BoardType, Union[str, None]]:
    board = assoc_in(board, coord_to, get_in(board, coord_from))
    return assoc_in(board, coord_from, {}), None


def is_check(*args):  # type: ignore
    pass
