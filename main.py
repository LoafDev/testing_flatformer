import pygame, sys
from setting import *
from level import *

if __name__ == '__main__':
    pygame.init()
    
    screen = pygame.display.set_mode(Screen_size)
    clock = pygame.time.Clock()

    level = Level()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(pygame.Color(colour))
        level.update()

        pygame.display.update()
        clock.tick(FPS)
