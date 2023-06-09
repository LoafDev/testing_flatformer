import pygame
from setting import *
from Tile import *
from player import Player
from Super_Reward import *

class Level:
    def __init__(self):
        self.display_surface = pygame.display.get_surface()

        self.visible_sprites = Camera_Group_I_Guess()
        self.active_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.setup_level()

    def setup_level(self):
        for row_index, row in enumerate(level_map):
            for col_index, col in enumerate(row):
                x = col_index * Tile_size
                y = row_index * Tile_size

                if col == 'X':
                    Tile((x,y), [self.visible_sprites, self.collision_sprites])

                if col == 'P':
                    self.player = Player((x,y), [self.visible_sprites, self.active_sprites], self.collision_sprites)

                if col == 'Z':
                    SUPER_REWARD((x,y), [self.visible_sprites, self.collision_sprites])
                    
                    

    def update(self):
        self.active_sprites.update()
        self.visible_sprites.custom_draw_that_I_want_to_name_it_very_long(self.player)

class Camera_Group_I_Guess(pygame.sprite.Group):
    def __init__(self):
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2(100,300)

        # #center camera setup
        # self.half_w = self.display_surface.get_size()[0] // 2
        # self.half_h = self.display_surface.get_size()[1] // 2

        #camera
        cam_left = CAMERA_LIMITS['left']
        cam_right = CAMERA_LIMITS['right']

        cam_top = CAMERA_LIMITS['top']
        cam_bottom = CAMERA_LIMITS['bottom']

        cam_width = self.display_surface.get_size()[0] - (cam_left + cam_right)
        cam_height = self.display_surface.get_size()[1] - (cam_top + cam_bottom)

        self.camera_rect = pygame.Rect(cam_left, cam_top, cam_width, cam_height)


    def custom_draw_that_I_want_to_name_it_very_long(self, player):
        
        # #get player's offset
        # self.offset.x = player.rect.centerx - self.half_w
        # self.offset.y = player.rect.centery - self.half_h

        #getting camera position
        if player.rect.left < self.camera_rect.left:
            self.camera_rect.left = player.rect.left

        if player.rect.right > self.camera_rect.right:
            self.camera_rect.right = player.rect.right

        if player.rect.top < self.camera_rect.top:
            self.camera_rect.top = player.rect.top

        if player.rect.bottom > self.camera_rect.bottom:
            self.camera_rect.bottom = player.rect.bottom


        #camera offset
        self.offset = pygame.math.Vector2(
            self.camera_rect.left - CAMERA_LIMITS['left'],
            self.camera_rect.top - CAMERA_LIMITS['top']
        )


        for sprite in self.sprites():
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image, offset_pos)
