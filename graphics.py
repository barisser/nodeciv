import pygame
import settings

def init_graphics():
    pygame.init()
    screens = {}
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    screens['background'] = screen
    return screens

def graphics_cycle(screens, data):
    pygame.draw.rect(screens['background'], (0, 128, 255), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()
    return screens
