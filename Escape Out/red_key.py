import pygame
from config import *


class Red_key(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = KEY_LAYER
        self.groups = self.game.all_sprites, self.game.red_keys

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.image.load('./img/red_key.png')
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        self.collected = False

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)

    def key_collected(self):
        for red_key in self.game.red_keys:
            if red_key.collected:
                self.game.red_keys.remove(red_key)

        





