import pygame
from pygame import font
import settings

def init_graphics(data):
    pygame.init()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    screen = reset_screen(screen, data)
    return screen

def graphics_cycle(screen, data):
    pygame.display.flip()
    return screen

def reset_screen(screen, data):
    screen = draw_world(screen, data)
    screen = draw_cities(screen, data)
    screen = draw_world_info(screen, data)
    return screen, data

def draw_world(screen, data):
    world = data['world']
    for x in range(0, len(world.map)):
        for y in range(0, len(world.map[x])):
            tile = world.map[x][y]
            screen = draw_tile(tile, screen)
    return screen

def draw_tile(tile, screen):
    mapx = settings.tile_width * tile.x
    mapy = settings.tile_width * tile.y
    color = (0, 120, 0)
    pygame.draw.rect(screen, color, pygame.Rect(mapx, mapy, settings.tile_width, settings.tile_width))
    return screen

def draw_cities(screen, data):
    cities = data['world'].cities
    for city in cities:
        cities_screen = draw_city(screen, city)
        screen = draw_city_text(screen, city)
    return screen

def draw_city(screen, city):
    mapx = settings.tile_width * city.x
    mapy = settings.tile_width * city.y
    color = (200,200,200)
    pygame.draw.rect(screen, color, pygame.Rect(mapx, mapy, settings.tile_width, settings.tile_width))
    return screen

def draw_city_text(screen, city):
    font = settings.standard_font
    text = font.render(city.name, True, (200, 200, 200))
    screen.blit(text, (city.x * settings.tile_width-15, city.y*settings.tile_width+10))
    return screen

def draw_text(screen, text, color, x, y):
    font = settings.standard_font
    text = font.render(text, True, color)
    screen.blit(text, (x, y))
    return screen

def draw_world_info(screen, data):
    mapy = settings.worldy * settings.tile_width
    height = settings.screen_height - mapy
    color = (220, 220, 220)
    pygame.draw.rect(screen, color, pygame.Rect(0, mapy, settings.screen_width, height))
    screen = draw_text(screen, "Turn: "+str(data['turn']), (0,0,0), 100, mapy + 50)
    return screen
