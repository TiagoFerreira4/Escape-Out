import pygame
from config import *
from spritesheet import *

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y, type):
        self.game = game
        self._layer = BLOCK_LAYER
        self.groups = self.game.all_sprites, self.game.blocks
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.type = type

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        if self.type == 'A':
            self.image = pygame.image.load('./img/select.png')
        else:
            self.image = pygame.image.load('./img/parede2.png')

        self.image.set_colorkey(BLACK)

        self.image = pygame.transform.scale(self.image, (32, 32))
        
        self.rect = self.image.get_rect()



        self.rect.x = self.x
        self.rect.y = self.y

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)
