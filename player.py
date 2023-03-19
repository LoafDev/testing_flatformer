import pygame
from setting import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)

        self.pos = pos

        self.display_surface = pygame.display.get_surface()

        self.image = pygame.Surface((Tile_size / 2 , Tile_size))
 
        self.image.fill('white')

        self.rect = self.image.get_rect(topleft = self.pos)

        self.group = groups

        #player's variable

        self.direction = pygame.math.Vector2()
        self.collision_sprites = collision_sprites
        self.speed = 10
        self.Jump_power = 24
        self.gravity = 1.3
        self.on_floor = False

    def player_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.direction.x = 1

        elif keys[pygame.K_LEFT]:
            self.direction.x = -1

        else:
            self.direction.x = 0

        if keys[pygame.K_SPACE] and self.on_floor:
            self.direction.y = -self.Jump_power
            self.on_floor = False

    def hori_collision(self):
        for sprite in self.collision_sprites.sprites():           
            if sprite.rect.colliderect(self.rect):
                if self.direction.x < 0:
                    self.rect.left = sprite.rect.right
                
                if self.direction.x > 0:
                    self.rect.right = sprite.rect.left

    def ver_collision(self):
        for sprite in self.collision_sprites.sprites():           
            if sprite.rect.colliderect(self.rect):

                if self.direction.y < 0:
                    self.rect.top = sprite.rect.bottom
                    self.direction.y = 0

                if self.direction.y > 0:
                    self.rect.bottom = sprite.rect.top
                    self.direction.y = 0
                    self.on_floor = True
        
        # if self.on_floor and self.direction.y != 0:
        #     self.on_floor = False

    def gracity_is_not_a_force(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

        
        if self.rect.bottom > self.display_surface.get_size()[1]:
            self.Restart_the_game()

    def Restart_the_game(self):
        (self.rect.x, self.rect.y) = self.pos
                
        
    def update(self):
        self.player_input()
        self.rect.x += self.direction.x * self.speed
        self.hori_collision()
        self.gracity_is_not_a_force()
        self.ver_collision()