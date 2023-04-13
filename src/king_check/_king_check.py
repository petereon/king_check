from abc import abstractclassmethod, ABC
from cytoolz.dicttoolz import assoc_in  # type: ignore
from cytoolz.dicttoolz import get_in as weird_get_in
from typing import Any, Dict, Tuple, Union, cast, Iterable


def get_in(d: dict, keys: Iterable[str]) -> dict:
    return cast(dict, weird_get_in(keys, d))


BoardType = dict[str, dict]
CoordType = tuple[str, str]

SuccessErrType = Tuple[bool, Union[str, None]]


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


class Piece(ABC):
    color: str
    letter_mapping = char_range('A', 'H')

    @abstractclassmethod
    def validate_move(cls, from_coord: CoordType, to_coord: CoordType, color: str) -> SuccessErrType:
        raise NotImplementedError()


class Pawn(Piece):
    @classmethod
    def is_starting_position(cls, coord: CoordType, color: str) -> bool:
        _, row = coord
        return (color == 'white' and row == '2') or (color == 'black' and row == '7')

    @classmethod
    def validate_move(cls, from_coord: CoordType, to_coord: CoordType, color: str) -> SuccessErrType:
        from_col, from_row = from_coord
        to_col, to_row = to_coord

        if cls.is_starting_position(from_coord, color) and abs(int(to_row) - int(from_row)) == 2 and from_col == to_col:
            return True, None

        if abs(cls.letter_mapping.index(from_col) - cls.letter_mapping.index(to_col)) <= 1 and (abs(int(to_row) - int(from_row)) == 1):
            return True, None

        return False, 'Cannot move there'
