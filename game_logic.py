import events
import graphics
import pygame


def cycle(screens, data):
    screens = graphics.graphics_cycle(screens, data)
    screens, data, cont = events.handle_events(screens, data)
    return screens, data, cont


def cities(data):
    for city in data['world'].cities:
        data = city.cycle(data)
    return data


def game_turn(screens, data):
    print "GAME TURN " + str(data['turn'])
    data = cities(data)
    screens, data = graphics.reset_screen(screens, data)
    data['turn'] += 1
    return screens, data
