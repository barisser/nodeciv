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
    data = cities(data)
    return screens, data
