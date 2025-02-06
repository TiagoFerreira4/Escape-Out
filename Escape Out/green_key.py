import pygame
from config import *


class Green_key(pygame.sprite.Sprite):

    def __init__(self, game, x, y):
        self.game = game
        self._layer = KEY_LAYER
        self.groups = self.game.all_sprites, self.game.green_keys

        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.image = pygame.image.load('./img/green_key.png')
        self.image = pygame.transform.scale(self.image, (TILESIZE, TILESIZE))

        self.rect = self.image.get_rect()

        self.rect.x = self.x
        self.rect.y = self.y
        self.collected = False

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.width, self.height)



    def key_collected(self):
        for green_key in self.game.green_keys:
            if green_key.collected:
                self.game.green_keys.remove(green_key)

                



