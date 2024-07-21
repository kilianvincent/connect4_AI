class Connect4:
    def __init__(self):
        self._grid = [[0 for _ in range(6)] for _ in range(7)]

    def play(self, column, value):
        # Check index validity
        if not 0 <= column <= 6:
            raise ValueError('Column index not valid (' + str(column) + ').')

        # Check value validity
        if not (value == 1 or value == 2):
            raise ValueError('Played value not valid (' + str(value) + ').')

        # Check if the column isn't already full
        col = self._grid[column]
        if 0 not in col:
            raise Exception('Column already full (' + str(column) + ').')

        # Get first empty cell index
        idx = 0
        for i, val in enumerate(col):
            if val == 0:
                idx = i
                break

        # Play
        self._grid[column][idx] = value

    def is_finished(self):
        for c in range(7):
            for r in range(6):
                if self._grid[c][r] == 0:
                    continue
                if c <= 3 and all(self._grid[c + i][r] == self._grid[c][r] for i in range(4)):
                    return True
                if r <= 2 and all(self._grid[c][r + i] == self._grid[c][r] for i in range(4)):
                    return True
                if c <= 3 and r <= 2 and all(self._grid[c + i][r + i] == self._grid[c][r] for i in range(4)):
                    return True
                if c <= 3 <= r and all(self._grid[c + i][r - i] == self._grid[c][r] for i in range(4)):
                    return True
        return all(self._grid[c][5] != 0 for c in range(7))

    def get_grid(self):
        return self._grid

    def __str__(self):
        str_val = ''
        for j in range(6):
            for i in range(7):
                str_val += str(self._grid[i][5-j])
            str_val += '\n'

        return str_val
