import images
import pygame
from pygame import font
import settings

def empty_surface(x, y):
    image = pygame.Surface([x, y], pygame.SRCALPHA, 32)
    image = image.convert_alpha()
    return image

def init_graphics(data):
    pygame.init()
    screens = {}
    screens['main'] = pygame.display.set_mode((settings.screen_width, settings.screen_height))
    screens['world'] = empty_surface(settings.tile_width * settings.worldx, settings.tile_width * settings.worldy)
    screens['info'] = empty_surface(settings.info_width, settings.info_height)
    screens, data = reset_screens(screens, data)
    return screens

def graphics_cycle(screens, data):
    screens['main'].blit(screens['world'], (0, 0))
    screens['main'].blit(screens['info'], (0, 0))
    pygame.display.flip()
    return screens

def reset_screens(screens, data):
    screens['world'] = draw_world(screens['world'], data, images.images)
    screens['world'] = draw_cities(screens['world'], data, images.images)
    screens['info'] = draw_world_info(screens['info'], data)
    return screens, data

def draw_world(surface, data, images):
    world = data['world']
    for x in range(0, len(world.map)):
        for y in range(0, len(world.map[x])):
            tile = world.map[x][y]
            screens = draw_tile(tile, surface, images)
    return surface

def draw_tile(tile, surface, images):
    mapx = settings.tile_width * tile.x
    mapy = settings.tile_width * tile.y
    image = images['plains']
    rect = pygame.Rect((mapx, mapy), (settings.tile_width, settings.tile_width))
    surface.blit(image, rect)
    return surface

def draw_cities(surface, data, images):
    cities = data['world'].cities
    for city in cities:
        cities_screen = draw_city(surface, city, images)
        screen = draw_city_text(surface, city)
    return surface

def draw_city(surface, city, images):
    mapx = settings.tile_width * city.x
    mapy = settings.tile_width * city.y
    rect = pygame.Rect((mapx, mapy), (settings.tile_width, settings.tile_width))
    image = images['city']
    surface.blit(image, rect)
    return surface

def draw_city_text(surface, city):
    font = settings.standard_font
    text = font.render(city.name, True, (200, 200, 200))
    surface.blit(text, (city.x * settings.tile_width-15, city.y*settings.tile_width+10))
    return surface

def draw_text(surface, text, color, x, y):
    font = settings.standard_font
    text = font.render(text, True, color)
    surface.blit(text, (x, y))
    return surface

def draw_world_info(screens, data):
    mapy = settings.info_width
    height = settings.info_height
    color = (220, 220, 220)
    pygame.draw.rect(screens, color, pygame.Rect(0, mapy, settings.info_width, height))
    screens = draw_text(screens, "Turn: "+str(data['turn']), (0, 0, 0), 100, mapy + 50)
    return screens
