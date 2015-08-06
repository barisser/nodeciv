def handle_events(data):
    r = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            r = False
        if event.type = pygame.KEYDOWN:
            r = False
    return r, data
