import pygame
from setting import *

class SUPER_REWARD(pygame.sprite.Sprite):
    def __init__(self, pos , group):
        super().__init__(group)

        self.image = pygame.Surface((REWARD_SIZE, REWARD_SIZE))

        self.image.fill('blue')

        self.rect = self.image.get_rect(topleft = pos)
