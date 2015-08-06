import events
import graphics
import pygame

def cycle(screens, data):
    screens = graphics.graphics_cycle(screens, data)
    cont, data = events.handle_events(data)
    return screens, data, cont
