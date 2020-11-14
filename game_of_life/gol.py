"""
Game of Life implementation in a functional style
"""


def evolve(alive_neighbours=0, cell_is_alive=False):
    """ Applies the 4 Game of Life rules """
    return cell_is_alive and alive_neighbours == 2 or alive_neighbours == 3


def count_neighbours(board, position):
    """ counts the number of neighbours at given position in board"""
    row_number, column_number = position
    upper_row_idx = row_number-1+len(board) % len(board)  # upper wrap around
    lower_row_idx = row_number+1 % len(board)  # lower wrap around
    rows = (board[upper_row_idx], board[row_number], board[lower_row_idx])

    count = 0
    for row in rows:
        cells = (row[column_number-1], row[column_number], row[column_number+1])
        count += sum(cells)

    count -= board[row_number][column_number]
    return count
