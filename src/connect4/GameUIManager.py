import src.connect4.Connect4 as c4
import tkinter as tk


class GameManager:
    def __init__(self, game: c4.Connect4):
        self._game = game
        self._screen = tk.Tk()
        self._window_width = 400
        self._window_height = 400

        self._screen.title("Connect4")
        self._screen.geometry(f"{self._window_width}x{self._window_height}")

        self._canvas = tk.Canvas(self._screen, width=self._window_width, height=self._window_height, bg='white')
        self._canvas.pack()

    def display(self):
        self._screen.after(100, self.draw_grid)
        self._screen.update()
        return self

    def draw_grid(self):
        grid = self._game.get_grid()

        rows = len(grid)
        cols = len(grid[0])

        square_width = self._window_width / cols
        square_height = self._window_height / rows
        square_size = min(square_width, square_height)

        for row in range(rows):
            for col in range(cols):
                x1 = col * square_size
                y1 = row * square_size
                x2 = x1 + square_size
                y2 = y1 + square_size
                color = 'white'
                if grid[row][5-col] == 1:
                    color = 'red'
                elif grid[row][5-col] == 2:
                    color = 'yellow'
                self._canvas.create_rectangle(y1, x1, y2, x2, fill=color, outline='grey')
