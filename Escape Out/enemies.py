from config import *
import random
import math
import pygame


class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = ENEMY_LAYER
        self.groups = self.game.all_sprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.height = TILESIZE

        self.change_x = 0
        self.change_y = 0

        self.facing = random.choice(['LEFT', 'RIGHT'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7, 30)

        self.number = random.randint(1,4)
        if self.number == 1:
            self.image = self.game.enemy_knight_spritesheet.get_sprite(KNIGHT_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, KNIGHT_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)
        if self.number == 2:
            self.image = self.game.enemy_mage_spritesheet.get_sprite(MAGE_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, MAGE_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)
        if self.number == 3:
            self.image = self.game.enemy_archer_spritesheet.get_sprite(ARCHER_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, ARCHER_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)
        if self.number == 4:
            self.image = self.game.enemy_assassin_spritesheet.get_sprite(ASSASSIN_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, ASSASSIN_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)

        self.image.set_colorkey(WHITE)
        self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, 50, 50)

    def update(self):
        self.movement()

        self.rect.x += self.change_x
        self.rect.y += self.change_y

        self.change_x = 0
        self.change_y = 0

    def movement(self):
        if self.facing == 'LEFT':
            self.change_x -= ENEMY_SPEED
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'RIGHT'
        if self.facing == 'RIGHT':
            self.change_x += ENEMY_SPEED
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'LEFT'   

    def animate(self): 
        if self.number == 1:
            animations = [
                        self.game.enemy_knight_spritesheet.get_sprite(KNIGHT_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, KNIGHT_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT),
                        self.game.enemy_knight_spritesheet.get_sprite(KNIGHT_ENEMY_DOWN_ANIMATION_FRAME_2_X, ENEMY_DOWN_ANIMATION_FRAME_2_HEIGHT, KNIGHT_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_2_HEIGHT),
                        self.game.enemy_knight_spritesheet.get_sprite(KNIGHT_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, KNIGHT_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT),
                    ]
            
        if self.number == 2:
            animations = [
                        self.game.enemy_mage_spritesheet.get_sprite(MAGE_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, MAGE_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT),
                        self.game.enemy_mage_spritesheet.get_sprite(MAGE_ENEMY_DOWN_ANIMATION_FRAME_2_X, ENEMY_DOWN_ANIMATION_FRAME_2_HEIGHT, MAGE_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_2_HEIGHT),
                        self.game.enemy_mage_spritesheet.get_sprite(MAGE_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, MAGE_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)
                    ]
            
        if self.number == 3:
            animations = [
                        self.game.enemy_archer_spritesheet.get_sprite(ARCHER_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, ARCHER_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT),
                        self.game.enemy_archer_spritesheet.get_sprite(ARCHER_ENEMY_DOWN_ANIMATION_FRAME_2_X, ENEMY_DOWN_ANIMATION_FRAME_2_HEIGHT, ARCHER_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_2_HEIGHT),
                        self.game.enemy_archer_spritesheet.get_sprite(ARCHER_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, ARCHER_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)
                    ]
            
        if self.number == 4:
            animations = [
                        self.game.enemy_assassin_spritesheet.get_sprite(ASSASSIN_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, ASSASSIN_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT),
                        self.game.enemy_assassin_spritesheet.get_sprite(ASSASSIN_ENEMY_DOWN_ANIMATION_FRAME_2_X, ENEMY_DOWN_ANIMATION_FRAME_2_HEIGHT, ASSASSIN_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_2_HEIGHT),
                        self.game.enemy_assassin_spritesheet.get_sprite(ASSASSIN_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, ASSASSIN_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)
                    ]
        
        if self.facing == 'DOWN' or self.facing == 'UP' or self.facing == 'RIGHT' or self.facing == 'LEFT':
            if self.change_y == 0 and self.change_x == 0:
                if self.number == 1:
                    self.image = self.game.enemy_knight_spritesheet.get_sprite(KNIGHT_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, KNIGHT_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)
                if self.number == 2:
                    self.image = self.game.enemy_mage_spritesheet.get_sprite(MAGE_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, MAGE_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)
                if self.number == 3:
                    self.image = self.game.enemy_archer_spritesheet.get_sprite(ARCHER_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, ARCHER_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)
                if self.number == 4:
                    self.image = self.game.enemy_assassin_spritesheet.get_sprite(ASSASSIN_ENEMY_DOWN_ANIMATION_FRAME_1_X, ENEMY_DOWN_ANIMATION_FRAME_1_Y, ASSASSIN_ENEMY_DOWN_ANIMATION_WIDTH, ENEMY_DOWN_ANIMATION_FRAME_1_HEIGHT)
            else:
                self.image = animations[math.floor(self.animation_loop)]

                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1