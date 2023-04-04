def char_range(c1: str, c2: str) -> list[str]:
    """Generates the characters from `c1` to `c2`, inclusive."""
    return [chr(c) for c in range(ord(c1), ord(c2) + 1)]


def create_board() -> dict[str, dict]:
    row: dict[str, dict] = {str(i): {} for i in range(1, 9)}
    return {i: row for i in char_range('A', 'H')}


def set_piece(board: dict[str, dict], col: str, row: str, piece: str, color: str) -> dict[str, dict]:
    board = board.copy()
    board[col][row] = {'piece': piece, 'color': color}
    return board


def move(*args):  # type: ignore
    ...


def is_check(*args):  # type: ignore
    ...
