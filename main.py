import pygame

if __name__ == "__main__":
    pygame.init()

    surface = pygame.display.set_mode((1000, 500))
    surface.fill((110, 110, 5))
    

    block = pygame.image.load("resources/block.jpg").convert()
    surface.blit(block, (0,0))


    pygame.display.flip()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
            elif event.type == pygame.QUIT:
                running = False
