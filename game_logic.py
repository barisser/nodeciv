import events
import graphics
import pygame

def cycle(screen, data):
    screen = graphics.graphics_cycle(screen, data)
    screen, data, cont = events.handle_events(screen, data)
    return screen, data, cont

def cities(data):
    for city in data['world'].cities:
        data = city.cycle(data)
    return data

def game_turn(screen, data):
    print "GAME TURN " + str(data['turn'])
    data = cities(data)
    screen, data = graphics.reset_screen(screen, data)
    data['turn'] += 1
    return screen, data
