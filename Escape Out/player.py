from config import *
from spritesheet import *
import math
import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y, select_character):

        self.game = game
        self._layer = PLAYER_LAYER
        self.groups = self.game.all_sprites

        pygame.sprite.Sprite.__init__(self, self.groups)
        self.x = x * TILESIZE
        self.y = y * TILESIZE
        self.width = TILESIZE
        self.heigth = TILESIZE
        self.select_character = select_character

        if self.select_character == "KNIGHT":
            self.image = self.game.character_D_spritesheet.get_sprite(KNIGHT_DOWN_ANIMATION_FRAME_1_X, KNIGHT_DOWN_ANIMATION_Y, KNIGHT_DOWN_ANIMATION_WIDTH, KNIGHT_DOWN_ANIMATION_FRAME_1_HEIGHT)
        elif self.select_character == "MAGE":
            self.image = self.game.character_D_spritesheet.get_sprite(MAGE_DOWN_ANIMATION_FRAME_1_X, MAGE_DOWN_ANIMATION_Y, MAGE_DOWN_ANIMATION_WIDTH, MAGE_DOWN_ANIMATION_HEIGHT)
        elif self.select_character == "ARCHER":
            self.image = self.game.character_D_spritesheet.get_sprite(ARCHER_DOWN_ANIMATION_FRAME_1_X, ARCHER_DOWN_ANIMATION_Y, ARCHER_DOWN_ANIMATION_WIDTH, ARCHER_DOWN_ANIMATION_FRAME_1_HEIGHT)
        elif self.select_character == "ASSASSIN":
            self.image = self.game.character_D_spritesheet.get_sprite(ASSASSIN_DOWN_ANIMATION_FRAME_1_X, ASSASSIN_DOWN_ANIMATION_Y, ASSASSIN_DOWN_ANIMATION_WIDTH, ASSASSIN_DOWN_ANIMATION_FRAME_1_HEIGHT)
        
        self.image = pygame.Surface((32, 48))

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


        self.image.blit(self.image, self.rect)

        self.change_x = 0
        self.change_y = 0

        self.facing = 'DOWN'
        self.animation_loop = 1
    
    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x += PLAYER_SPEED
            self.change_x -= PLAYER_SPEED
            self.facing = 'LEFT'
        elif keys[pygame.K_RIGHT]:
            for sprite in self.game.all_sprites:
                sprite.rect.x -= PLAYER_SPEED
            self.change_x += PLAYER_SPEED
            self.facing = 'RIGHT'
        elif keys[pygame.K_UP]:
            for sprite in self.game.all_sprites:
                sprite.rect.y += PLAYER_SPEED
            self.change_y -= PLAYER_SPEED
            self.facing = 'UP'
        elif keys[pygame.K_DOWN]:
            for sprite in self.game.all_sprites:
                sprite.rect.y -= PLAYER_SPEED
            self.change_y += PLAYER_SPEED
            self.facing = 'DOWN'
    
    def update(self):
        self.movement()
        self.animate()
        self.collide_enemy()

        if self.select_character == 'ASSASSIN':
            self.image = pygame.transform.scale(self.image, (30, 50))
        elif self.select_character == 'ARCHER':
            self.image = pygame.transform.scale(self.image, (40, 50))
        else:
            self.image = pygame.transform.scale(self.image, (50, 50))

        self.rect.x += self.change_x
        self.collide_blocks('x')
        self.rect.y += self.change_y
        self.collide_blocks('y')

        self.change_x = 0
        self.change_y = 0

        hits = pygame.sprite.spritecollide(self, self.game.green_keys, True)
        for key in hits:
            key.collected = True

        hits_R = pygame.sprite.spritecollide(self, self.game.red_keys, True)
        for key in hits_R:
            key.collected = True

        hits_B = pygame.sprite.spritecollide(self, self.game.blue_keys, True)
        for key in hits_B:
            key.collected = True
    
    def animate(self):
        if self.select_character == 'KNIGHT':
            down_animations = [
                self.game.character_D_spritesheet.get_sprite(KNIGHT_DOWN_ANIMATION_FRAME_1_X, KNIGHT_DOWN_ANIMATION_Y, KNIGHT_DOWN_ANIMATION_WIDTH, KNIGHT_DOWN_ANIMATION_FRAME_1_HEIGHT),
                self.game.character_D_spritesheet.get_sprite(KNIGHT_DOWN_ANIMATION_FRAME_2_X, KNIGHT_DOWN_ANIMATION_Y, KNIGHT_DOWN_ANIMATION_WIDTH, KNIGHT_DOWN_ANIMATION_FRAME_2_3_HEIGHT),
                self.game.character_D_spritesheet.get_sprite(KNIGHT_DOWN_ANIMATION_FRAME_3_X, KNIGHT_DOWN_ANIMATION_Y, KNIGHT_DOWN_ANIMATION_WIDTH, KNIGHT_DOWN_ANIMATION_FRAME_2_3_HEIGHT)
                ]
            
            up_animations = [
                self.game.character_U_spritesheet.get_sprite(KNIGHT_UP_ANIMATION_FRAME_1_X, KNIGHT_UP_ANIMATION_Y, KNIGHT_UP_ANIMATION_WIDTH, KNIGHT_UP_ANIMATION_HEIGHT),
                self.game.character_U_spritesheet.get_sprite(KNIGHT_UP_ANIMATION_FRAME_2_X, KNIGHT_UP_ANIMATION_Y, KNIGHT_UP_ANIMATION_WIDTH, KNIGHT_UP_ANIMATION_HEIGHT),
                self.game.character_U_spritesheet.get_sprite(KNIGHT_UP_ANIMATION_FRAME_3_X, KNIGHT_UP_ANIMATION_Y, KNIGHT_UP_ANIMATION_WIDTH, KNIGHT_UP_ANIMATION_HEIGHT)
            ]
            
            right_animations = [
                self.game.character_R_spritesheet.get_sprite(KNIGHT_RIGHT_ANIMATION_FRAME_1_X, KNIGHT_RIGHT_ANIMATION_Y, KNIGHT_RIGHT_ANIMATION_WIDTH, KNIGHT_RIGHT_ANIMATION_HEIGHT),
                self.game.character_R_spritesheet.get_sprite(KNIGHT_RIGHT_ANIMATION_FRAME_2_X, KNIGHT_RIGHT_ANIMATION_Y, KNIGHT_RIGHT_ANIMATION_WIDTH, KNIGHT_RIGHT_ANIMATION_HEIGHT),
                self.game.character_R_spritesheet.get_sprite(KNIGHT_RIGHT_ANIMATION_FRAME_1_X, KNIGHT_RIGHT_ANIMATION_Y, KNIGHT_RIGHT_ANIMATION_WIDTH, KNIGHT_RIGHT_ANIMATION_HEIGHT)
                ]
            
            left_animations = [
                self.game.character_L_spritesheet.get_sprite(KNIGHT_LEFT_ANIMATION_FRAME_1_X, KNIGHT_LEFT_ANIMATION_Y, KNIGHT_LEFT_ANIMATION_WIDTH, KNIGHT_LEFT_ANIMATION_HEIGHT),
                self.game.character_L_spritesheet.get_sprite(KNIGHT_LEFT_ANIMATION_FRAME_2_X, KNIGHT_LEFT_ANIMATION_Y, KNIGHT_LEFT_ANIMATION_WIDTH, KNIGHT_LEFT_ANIMATION_HEIGHT),
                self.game.character_L_spritesheet.get_sprite(KNIGHT_LEFT_ANIMATION_FRAME_1_X, KNIGHT_LEFT_ANIMATION_Y, KNIGHT_LEFT_ANIMATION_WIDTH, KNIGHT_LEFT_ANIMATION_HEIGHT)
            ]

        elif self.select_character == 'MAGE':
            down_animations = [
                            self.game.character_D_spritesheet.get_sprite(MAGE_DOWN_ANIMATION_FRAME_1_X, MAGE_DOWN_ANIMATION_Y, MAGE_DOWN_ANIMATION_WIDTH, MAGE_DOWN_ANIMATION_HEIGHT),
                            self.game.character_D_spritesheet.get_sprite(MAGE_DOWN_ANIMATION_FRAME_2_X, MAGE_DOWN_ANIMATION_Y, MAGE_DOWN_ANIMATION_WIDTH, MAGE_DOWN_ANIMATION_HEIGHT),
                            self.game.character_D_spritesheet.get_sprite(MAGE_DOWN_ANIMATION_FRAME_3_X, MAGE_DOWN_ANIMATION_Y, MAGE_DOWN_ANIMATION_WIDTH, MAGE_DOWN_ANIMATION_HEIGHT)
                            ]
            
            up_animations = [
                            self.game.character_U_spritesheet.get_sprite(MAGE_UP_ANIMATION_FRAME_X, MAGE_UP_ANIMATION_Y, MAGE_UP_ANIMATION_WIDTH, MAGE_UP_ANIMATION_HEIGHT),
                            self.game.character_U_spritesheet.get_sprite(MAGE_UP_ANIMATION_FRAME_X, MAGE_UP_ANIMATION_Y, MAGE_UP_ANIMATION_WIDTH, MAGE_UP_ANIMATION_HEIGHT),
                            self.game.character_U_spritesheet.get_sprite(MAGE_UP_ANIMATION_FRAME_X, MAGE_UP_ANIMATION_Y, MAGE_UP_ANIMATION_WIDTH, MAGE_UP_ANIMATION_HEIGHT)
                            ]
            
            right_animations = [
                            self.game.character_R_spritesheet.get_sprite(MAGE_RIGHT_ANIMATION_FRAME_X, MAGE_RIGHT_ANIMATION_Y, MAGE_RIGHT_ANIMATION_WIDTH, MAGE_RIGHT_ANIMATION_HEIGHT),
                            self.game.character_R_spritesheet.get_sprite(MAGE_RIGHT_ANIMATION_FRAME_X, MAGE_RIGHT_ANIMATION_Y, MAGE_RIGHT_ANIMATION_WIDTH, MAGE_RIGHT_ANIMATION_HEIGHT),
                            self.game.character_R_spritesheet.get_sprite(MAGE_RIGHT_ANIMATION_FRAME_X, MAGE_RIGHT_ANIMATION_Y, MAGE_RIGHT_ANIMATION_WIDTH, MAGE_RIGHT_ANIMATION_HEIGHT)
                            ]

            left_animations = [
                            self.game.character_L_spritesheet.get_sprite(MAGE_LEFT_ANIMATION_FRAME_X, MAGE_LEFT_ANIMATION_Y, MAGE_LEFT_ANIMATION_WIDTH, MAGE_LEFT_ANIMATION_HEIGHT),
                            self.game.character_L_spritesheet.get_sprite(MAGE_LEFT_ANIMATION_FRAME_X, MAGE_LEFT_ANIMATION_Y, MAGE_LEFT_ANIMATION_WIDTH, MAGE_LEFT_ANIMATION_HEIGHT),
                            self.game.character_L_spritesheet.get_sprite(MAGE_LEFT_ANIMATION_FRAME_X, MAGE_LEFT_ANIMATION_Y, MAGE_LEFT_ANIMATION_WIDTH, MAGE_LEFT_ANIMATION_HEIGHT)
                            ]

        elif self.select_character == 'ARCHER':
            down_animations = [
                self.game.character_D_spritesheet.get_sprite(ARCHER_DOWN_ANIMATION_FRAME_1_X, ARCHER_DOWN_ANIMATION_Y, ARCHER_DOWN_ANIMATION_WIDTH, ARCHER_DOWN_ANIMATION_FRAME_1_HEIGHT),
                self.game.character_D_spritesheet.get_sprite(ARCHER_DOWN_ANIMATION_FRAME_2_X, ARCHER_DOWN_ANIMATION_Y, ARCHER_DOWN_ANIMATION_WIDTH, ARCHER_DOWN_ANIMATION_FRAME_2_3_HEIGHT),
                self.game.character_D_spritesheet.get_sprite(ARCHER_DOWN_ANIMATION_FRAME_3_X, ARCHER_DOWN_ANIMATION_Y, ARCHER_DOWN_ANIMATION_WIDTH, ARCHER_DOWN_ANIMATION_FRAME_2_3_HEIGHT)
                ]
        
            up_animations = [
                self.game.character_U_spritesheet.get_sprite(ARCHER_UP_ANIMATION_FRAME_1_X, ARCHER_UP_ANIMATION_Y, ARCHER_UP_ANIMATION_WIDTH, ARCHER_UP_ANIMATION_HEIGHT),
                self.game.character_U_spritesheet.get_sprite(ARCHER_UP_ANIMATION_FRAME_2_X, ARCHER_UP_ANIMATION_Y, ARCHER_UP_ANIMATION_WIDTH, ARCHER_UP_ANIMATION_HEIGHT),
                self.game.character_U_spritesheet.get_sprite(ARCHER_UP_ANIMATION_FRAME_3_X, ARCHER_UP_ANIMATION_Y, ARCHER_UP_ANIMATION_WIDTH, ARCHER_UP_ANIMATION_HEIGHT)
            ]

            right_animations = [
                self.game.character_R_spritesheet.get_sprite(ARCHER_RIGHT_ANIMATION_FRAME_1_X, ARCHER_RIGHT_ANIMATION_Y, ARCHER_RIGHT_ANIMATION_WIDTH, ARCHER_RIGHT_ANIMATION_HEIGHT),
                self.game.character_R_spritesheet.get_sprite(ARCHER_RIGHT_ANIMATION_FRAME_2_X, ARCHER_RIGHT_ANIMATION_Y, ARCHER_RIGHT_ANIMATION_WIDTH, ARCHER_RIGHT_ANIMATION_HEIGHT),
                self.game.character_R_spritesheet.get_sprite(ARCHER_RIGHT_ANIMATION_FRAME_1_X, ARCHER_RIGHT_ANIMATION_Y, ARCHER_RIGHT_ANIMATION_WIDTH, ASSASSIN_RIGHT_ANIMATION_HEIGHT)
            ]

            left_animations = [
                self.game.character_L_spritesheet.get_sprite(ARCHER_LEFT_ANIMATION_FRAME_1_X, ARCHER_LEFT_ANIMATION_Y, ARCHER_LEFT_ANIMATION_WIDTH, ARCHER_LEFT_ANIMATION_HEIGHT),
                self.game.character_L_spritesheet.get_sprite(ARCHER_LEFT_ANIMATION_FRAME_2_X, ARCHER_LEFT_ANIMATION_Y, ARCHER_LEFT_ANIMATION_WIDTH, ARCHER_LEFT_ANIMATION_HEIGHT),
                self.game.character_L_spritesheet.get_sprite(ARCHER_LEFT_ANIMATION_FRAME_1_X, ARCHER_LEFT_ANIMATION_Y, ARCHER_LEFT_ANIMATION_WIDTH, ARCHER_LEFT_ANIMATION_HEIGHT)
            ]

        elif self.select_character == 'ASSASSIN':
            down_animations = [
                self.game.character_D_spritesheet.get_sprite(ASSASSIN_DOWN_ANIMATION_FRAME_1_X, ASSASSIN_DOWN_ANIMATION_Y, ASSASSIN_DOWN_ANIMATION_WIDTH, ASSASSIN_DOWN_ANIMATION_FRAME_1_HEIGHT),
                self.game.character_D_spritesheet.get_sprite(ASSASSIN_DOWN_ANIMATION_FRAME_2_X, ASSASSIN_DOWN_ANIMATION_Y, ASSASSIN_DOWN_ANIMATION_WIDTH, ASSASSIN_DOWN_ANIMATION_FRAME_2_3_HEIGHT),
                self.game.character_D_spritesheet.get_sprite(ASSASSIN_DOWN_ANIMATION_FRAME_3_X, ASSASSIN_DOWN_ANIMATION_Y, ASSASSIN_DOWN_ANIMATION_WIDTH, ASSASSIN_DOWN_ANIMATION_FRAME_2_3_HEIGHT)
                ]

            up_animations = [
                self.game.character_U_spritesheet.get_sprite(ASSASSIN_UP_ANIMATION_FRAME_1_X, ASSASSIN_UP_ANIMATION_Y, ASSASSIN_UP_ANIMATION_WIDTH, ASSASSIN_UP_ANIMATION_HEIGHT),
                self.game.character_U_spritesheet.get_sprite(ASSASSIN_UP_ANIMATION_FRAME_2_X, ASSASSIN_UP_ANIMATION_Y, ASSASSIN_UP_ANIMATION_WIDTH, ASSASSIN_UP_ANIMATION_HEIGHT),
                self.game.character_U_spritesheet.get_sprite(ASSASSIN_UP_ANIMATION_FRAME_3_X, ASSASSIN_UP_ANIMATION_Y, ASSASSIN_UP_ANIMATION_WIDTH, ASSASSIN_UP_ANIMATION_HEIGHT)
            ]

            right_animations = [
                self.game.character_R_spritesheet.get_sprite(ASSASSIN_RIGHT_ANIMATION_FRAME_1_X, ASSASSIN_RIGHT_ANIMATION_Y, ASSASSIN_RIGHT_ANIMATION_WIDTH, ASSASSIN_RIGHT_ANIMATION_HEIGHT),
                self.game.character_R_spritesheet.get_sprite(ASSASSIN_RIGHT_ANIMATION_FRAME_2_X, ASSASSIN_RIGHT_ANIMATION_Y, ASSASSIN_RIGHT_ANIMATION_WIDTH, ASSASSIN_RIGHT_ANIMATION_HEIGHT),
                self.game.character_R_spritesheet.get_sprite(ASSASSIN_RIGHT_ANIMATION_FRAME_1_X, ASSASSIN_RIGHT_ANIMATION_Y, ASSASSIN_RIGHT_ANIMATION_WIDTH, ASSASSIN_RIGHT_ANIMATION_HEIGHT)
            ]

            left_animations = [
                self.game.character_L_spritesheet.get_sprite(ASSASSIN_LEFT_ANIMATION_FRAME_1_X, ASSASSIN_LEFT_ANIMATION_Y, ASSASSIN_LEFT_ANIMATION_WIDTH, ASSASSIN_LEFT_ANIMATION_HEIGHT),
                self.game.character_L_spritesheet.get_sprite(ASSASSIN_LEFT_ANIMATION_FRAME_2_X, ASSASSIN_LEFT_ANIMATION_Y, ASSASSIN_LEFT_ANIMATION_WIDTH, ASSASSIN_LEFT_ANIMATION_HEIGHT),
                self.game.character_L_spritesheet.get_sprite(ASSASSIN_LEFT_ANIMATION_FRAME_1_X, ASSASSIN_LEFT_ANIMATION_Y, ASSASSIN_LEFT_ANIMATION_WIDTH, ASSASSIN_LEFT_ANIMATION_HEIGHT)
            ]

        if self.facing == 'DOWN':
            if self.change_y == 0:
                if self.select_character == "KNIGHT":
                    self.image = self.game.character_D_spritesheet.get_sprite(KNIGHT_DOWN_ANIMATION_FRAME_1_X, KNIGHT_DOWN_ANIMATION_Y, KNIGHT_DOWN_ANIMATION_WIDTH, KNIGHT_DOWN_ANIMATION_FRAME_1_HEIGHT)
                elif self.select_character == "MAGE":
                    self.image == self.game.character_D_spritesheet.get_sprite(MAGE_DOWN_ANIMATION_FRAME_1_X, MAGE_DOWN_ANIMATION_Y, MAGE_DOWN_ANIMATION_WIDTH, MAGE_DOWN_ANIMATION_HEIGHT)
                elif self.select_character == "ARCHER":
                    self.image = self.game.character_D_spritesheet.get_sprite(ARCHER_DOWN_ANIMATION_FRAME_1_X, ARCHER_DOWN_ANIMATION_Y, ARCHER_DOWN_ANIMATION_WIDTH, ARCHER_DOWN_ANIMATION_FRAME_1_HEIGHT)
                elif self.select_character == "ASSASSIN":
                    self.image = self.game.character_D_spritesheet.get_sprite(ASSASSIN_DOWN_ANIMATION_FRAME_1_X, ASSASSIN_DOWN_ANIMATION_Y, ASSASSIN_DOWN_ANIMATION_WIDTH, ASSASSIN_DOWN_ANIMATION_FRAME_1_HEIGHT)
            else:
                self.image = down_animations[math.floor(self.animation_loop)]

                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
        
        elif self.facing == 'UP':
            if self.change_y == 0:
                if self.select_character == "KNIGHT":
                    self.image = self.game.character_U_spritesheet.get_sprite(KNIGHT_UP_ANIMATION_FRAME_1_X, KNIGHT_UP_ANIMATION_Y, KNIGHT_UP_ANIMATION_WIDTH, KNIGHT_UP_ANIMATION_HEIGHT)
                elif self.select_character == "MAGE":
                    self.image == self.game.character_U_spritesheet.get_sprite(MAGE_UP_ANIMATION_FRAME_X, MAGE_UP_ANIMATION_Y, MAGE_UP_ANIMATION_WIDTH, MAGE_UP_ANIMATION_HEIGHT)
                elif self.select_character == "ARCHER":
                    self.image = self.game.character_U_spritesheet.get_sprite(ARCHER_UP_ANIMATION_FRAME_1_X, ARCHER_UP_ANIMATION_Y, ARCHER_UP_ANIMATION_WIDTH, ARCHER_UP_ANIMATION_HEIGHT)
                elif self.select_character == "ASSASSIN":
                    self.image = self.game.character_U_spritesheet.get_sprite(ASSASSIN_UP_ANIMATION_FRAME_1_X, ASSASSIN_UP_ANIMATION_Y, ASSASSIN_UP_ANIMATION_WIDTH, ASSASSIN_UP_ANIMATION_HEIGHT)
            else:
                self.image = up_animations[math.floor(self.animation_loop)]

                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
            
        
        elif self.facing == 'RIGHT':
            if self.change_x == 0:
                if self.select_character == "KNIGHT":
                    self.image = self.game.character_R_spritesheet.get_sprite(KNIGHT_RIGHT_ANIMATION_FRAME_1_X, KNIGHT_RIGHT_ANIMATION_Y, KNIGHT_RIGHT_ANIMATION_WIDTH, KNIGHT_RIGHT_ANIMATION_HEIGHT)
                elif self.select_character == "MAGE":
                    self.image == self.game.character_R_spritesheet.get_sprite(MAGE_RIGHT_ANIMATION_FRAME_X, MAGE_RIGHT_ANIMATION_Y, MAGE_RIGHT_ANIMATION_WIDTH, MAGE_RIGHT_ANIMATION_HEIGHT)
                elif self.select_character == "ARCHER":
                    self.image = self.game.character_R_spritesheet.get_sprite(ARCHER_RIGHT_ANIMATION_FRAME_1_X, ARCHER_RIGHT_ANIMATION_Y, ARCHER_RIGHT_ANIMATION_WIDTH, ARCHER_RIGHT_ANIMATION_HEIGHT)
                elif self.select_character == "ASSASSIN":
                    self.image = self.game.character_R_spritesheet.get_sprite(ASSASSIN_RIGHT_ANIMATION_FRAME_1_X, ASSASSIN_RIGHT_ANIMATION_Y, ASSASSIN_RIGHT_ANIMATION_WIDTH, ASSASSIN_RIGHT_ANIMATION_HEIGHT)
            else:
                self.image = right_animations[math.floor(self.animation_loop)]

                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
            
        
        elif self.facing == 'LEFT':
            if self.change_x == 0:
                if self.select_character == "KNIGHT":
                    self.image = self.game.character_L_spritesheet.get_sprite(KNIGHT_LEFT_ANIMATION_FRAME_1_X, KNIGHT_LEFT_ANIMATION_Y, KNIGHT_LEFT_ANIMATION_WIDTH, KNIGHT_LEFT_ANIMATION_HEIGHT)
                elif self.select_character == "MAGE":
                    self.image == self.game.character_L_spritesheet.get_sprite(MAGE_LEFT_ANIMATION_FRAME_X, MAGE_LEFT_ANIMATION_Y, MAGE_LEFT_ANIMATION_WIDTH, MAGE_LEFT_ANIMATION_HEIGHT)
                elif self.select_character == "ARCHER":
                    self.image = self.game.character_L_spritesheet.get_sprite(ARCHER_LEFT_ANIMATION_FRAME_1_X, ARCHER_LEFT_ANIMATION_Y, ARCHER_LEFT_ANIMATION_WIDTH, ARCHER_LEFT_ANIMATION_HEIGHT)
                elif self.select_character == "ASSASSIN":
                    self.image = self.game.character_L_spritesheet.get_sprite(ASSASSIN_LEFT_ANIMATION_FRAME_1_X, ASSASSIN_LEFT_ANIMATION_Y, ASSASSIN_LEFT_ANIMATION_WIDTH, ASSASSIN_LEFT_ANIMATION_HEIGHT)
            else:
                self.image = left_animations[math.floor(self.animation_loop)]

                self.animation_loop += 0.1
                if self.animation_loop >= 3:
                    self.animation_loop = 1
            
                    

    def collide_blocks(self, direction):
        if direction == 'x':
            for block in self.game.blocks:
                if self.rect.colliderect(block.rect):
                    #print("Colisão com block detectada!")
                    if self.change_x > 0:
                        self.rect.right = block.rect.left
                    if self.change_x < 0:
                        self.rect.left = block.rect.right
        if direction == 'y':
            for block in self.game.blocks:
                if self.rect.colliderect(block.rect):
                   #print("Colisão com block detectada!")
                    if self.change_y > 0:
                        self.rect.bottom = block.rect.top
                    if self.change_y < 0:
                        self.rect.top = block.rect.bottom

    def collide_enemy(self):
        for enemy in self.game.enemies:
            if self.rect.colliderect(enemy.rect):
                #print("Colisão com inimigo detectada!")
                self.kill()
                self.game.playing = False

    def collide_green_key(self):
        for green_key in self.game.green_key:
            if self.rect.colliderect(green_key.rect) and not green_key:
                #print("Colisão com chave_verde detectada!")
                green_key.collected = True
                self.game.green_key.remove(green_key)
                self.game.all_sprites.remove(green_key)

    def collide_red_key(self):
        for red_key in self.game.red_key:
            if self.rect.colliderect(red_key.rect) and not red_key:
               # print("Colisão com chave_verde detectada!")
                red_key.collected = True
                self.game.red_key.remove(red_key)
                self.game.all_sprites.remove(red_key)


    def collide_blue_key(self):
        for blue_key in self.game.blue_key:
            if self.rect.colliderect(blue_key.rect) and not blue_key:
                #print("Colisão com chave_verde detectada!")
                blue_key.collected = True
                self.game.blue_key.remove(blue_key)
                self.game.all_sprites.remove(blue_key)

    def collide_door(self):
        for door in self.game.door:
            if self.rect.colliderect(door.rect) and not door:
                #print("Colisão com porta")
                door.position = True
                self.game.playing = False

