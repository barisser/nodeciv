import game_logic
import pygame


def handle_events(screens, data):
    r = True
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                screens, data = game_logic.game_turn(screens, data)
            #r = False
    return screens, data, r
