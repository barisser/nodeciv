import pygame
from pygame import font

screen_width = 800
screen_height = 700
info_height = 100
info_width = 800
worldx = 80
worldy = 60
tile_width = 10
average_pop_per_tile = 10

food_per_person = 1.0
starvation_rate = 0.02
growth_rate = 0.01

pygame.font.init()
standard_font = pygame.font.Font(None, 20)
