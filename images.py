import pygame

def load_images():
    print "LOADING IMAGES"
    images = {}
    images['plains'] = pygame.image.load('./images/plains.jpg')
    images['ocean'] = pygame.image.load('./images/ocean.jpg')
    images['city'] = pygame.image.load('./images/city.jpg')
    return images

images = load_images()
