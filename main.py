import time

import src.connect4.Connect4 as c4
import src.connect4.GameUIManager as gmui


def main():
    game = c4.Connect4()
    manager = gmui.GameManager(game)
    manager.display()

    time.sleep(1)

    game.play(4, 1)
    manager.display()

    time.sleep(1)

    game.play(4, 2)
    manager.display()

    time.sleep(10)


if __name__ == '__main__':
    main()
