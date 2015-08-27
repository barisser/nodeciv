import pygame
from pygame import font

screen_width = 1000
screen_height = 1000
worldx = 100
worldy = 80
tile_width = 10
average_pop_per_tile = 10

food_per_person = 1.0
starvation_rate = 0.02
growth_rate = 0.01

pygame.font.init()
standard_font = pygame.font.Font(None, 20)
