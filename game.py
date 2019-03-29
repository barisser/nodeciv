import game_logic
import graphics
import pygame
import tempdata


def run():
    data = tempdata.init_data()
    screens = graphics.init_graphics(data)

    cont = True
    while cont:
        screens, data, cont = game_logic.cycle(screens, data)


if __name__ == "__main__":
    run()
