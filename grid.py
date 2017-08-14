from typing import List, Optional

from cell import Cell


class Grid:

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def columns(self) -> int:
        return self._columns

    def __init__(self, rows: int, columns: int) -> None:
        if rows is None or rows < 0:
            raise ValueError("Rows must be a positive integer")
        if columns is None or columns < 0:
            raise ValueError("Columns must be a positive integer")

        self._rows = rows           # type: int
        self._columns = columns     # type: int
        self._grid = self.prepare_grid()
        self.configure_cells()

    def get_cell(self, row: int, column: int) -> Optional[Cell]:
        if not (0 <= row < self.rows):
            return None
        if not (0 <= column < self.columns):
            return None
        return self._grid[row][column]

    def prepare_grid(self) -> List[List["Cell"]]:
        return [[Cell(row, column) for column in range(self.columns)] for row in range(self.rows)]

    def configure_cells(self) -> None:
        for row in range(self.rows):
            for column in range(self.columns):
                cell = self.get_cell(row, column)
                if cell is None:
                    raise IndexError(
                        "Cell ({},{}) out of grid bounds ({},{})".format(column, row, self.columns, self.rows))
                cell.north = self.get_cell(row - 1, column)
                cell.south = self.get_cell(row + 1, column)
                cell.east = self.get_cell(row, column + 1)
                cell.west = self.get_cell(row, column - 1)

    # TODO: Decide if interesting to keep (at least for tests) or remove
    def __repr__(self) -> str:
        return str(self._grid)
