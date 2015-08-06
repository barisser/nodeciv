import game_logic
import graphics
import tempdata

def run():
    data = tempdata.init_data()
    screens = graphics.init_graphics()

    cont = True
    while cont:
        screen, data, cont = game_logic.cycle(screens, data)

if __name__ == "__main__":
    run()
