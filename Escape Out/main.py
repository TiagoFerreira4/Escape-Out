import pygame
from player import *
from config import *
from button import *
from wall import *
from ground import *
from spritesheet import *
from enemies import *
from green_key import *
from blue_key import *
from red_key import *
import sys
from musica import Musica



class Game:
    def __init__(self):
        pygame.init()

        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.screen.fill(WHITE)
        pygame.display.set_caption("ESCAPE OUT")
        self.clock = pygame.time.Clock()

        self.running = True
        self.font = pygame.font.Font('arial.ttf', 32)

        self.intro_background = pygame.image.load('./img/intro_image.jpg')
        self.intro_background = pygame.transform.scale(self.intro_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.select_screen_background = pygame.image.load('./img/parede2.png')
        self.select_screen_background = pygame.transform.scale(self.select_screen_background, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.gameover_background = pygame.image.load('./img/gameover.png')
        self.win_background = pygame.image.load('./img/win.png')

        # self.block_sprite = Spritesheet('img/select.png')
        # self.terrain_background = Spritesheet('img/parede2.png')
        self.terrain_spritesheet = Spritesheet('./img/terrain.png')
        self.enemy_knight_spritesheet = Spritesheet('./img/enemy_knight.png')
        self.enemy_mage_spritesheet = Spritesheet('./img/enemy_mage.png')
        self.enemy_archer_spritesheet = Spritesheet('./img/enemy_archer.png')
        self.enemy_assassin_spritesheet = Spritesheet('./img/enemy_assassin.png')


        musica = Musica('./musica/musica_escape.mp3')
        musica.tocar()

    def create_maze(self):
        for i, row in enumerate(maze):
            for j, column in enumerate(row):
                Ground(self, j, i)

                if column == 'B' or column == 'A':
                    Wall(self, j, i, column)
                    
                if column == '1':
                    Green_key(self, j, i)
                
                if column == '2':
                    Blue_key(self, j, i)

                if column == '3':
                    Red_key(self, j, i)

                if column == 'E':
                    Enemy(self, j, i)

                if column == 'P':
                    if self.select_screen() == "KNIGHT":
                        self.character_D_spritesheet = Spritesheet('./img/cavaleiro_front.png')
                        self.character_L_spritesheet = Spritesheet('./img/cavaleiro_left.png')
                        self.character_R_spritesheet = Spritesheet('./img/cavaleiro_right.png')
                        self.character_U_spritesheet = Spritesheet('./img/cavaleiro_back.png')
                        Player(self, j, i, "KNIGHT")
                        self.attack_spritesheet = Spritesheet('./img/knight_assassin_attack.png')

                    if self.select_screen() == "MAGE":
                        self.character_D_spritesheet = Spritesheet('./img/mago_front.png')
                        self.character_L_spritesheet = Spritesheet('./img/mago_left.png')
                        self.character_R_spritesheet = Spritesheet('./img/mago_right.png')
                        self.character_U_spritesheet = Spritesheet('./img/mago_back.png')
                        Player(self, j, i, "MAGE")
                        self.attack_spritesheet = Spritesheet('./img/mage_attack.png')

                    if self.select_screen() == "ARCHER":
                        self.character_D_spritesheet = Spritesheet('./img/arqueiro_front.png')
                        self.character_L_spritesheet = Spritesheet('./img/arqueiro_left.png')
                        self.character_R_spritesheet = Spritesheet('./img/arqueiro_right.png')
                        self.character_U_spritesheet = Spritesheet('./img/arqueiro_back.png')
                        Player(self, j, i, "ARCHER")
                        self.attack_spritesheet = Spritesheet('./img/archer_attack.png')

                    if self.select_screen() == "ASSASSIN":
                        self.character_D_spritesheet = Spritesheet('./img/assassino_front.png')
                        self.character_L_spritesheet = Spritesheet('./img/assassino_left.png')
                        self.character_R_spritesheet = Spritesheet('./img/assassino_right.png')
                        self.character_U_spritesheet = Spritesheet('./img/assassino_back.png')
                        Player(self, j, i, "ASSASSIN")
                        self.attack_spritesheet = Spritesheet('./img/knight_assassin_attack.png')
    
    def new(self):
        self.playing = True

        self.all_sprites = pygame.sprite.LayeredUpdates()
        self.blocks = pygame.sprite.LayeredUpdates()
        self.green_keys = pygame.sprite.LayeredUpdates()
        self.blue_keys = pygame.sprite.LayeredUpdates()
        self.red_keys = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.attacks = pygame.sprite.LayeredUpdates()
        self.player = pygame.sprite.LayeredUpdates()

        self.create_maze()
    
    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT: #quit the game
                self.running = False
                self.playing = False

    def update(self):
        self.all_sprites.update()

    def draw(self):
        self.verde = ''
        self.azul = ''
        self.vermelho = ''
        

        self.screen.fill(BLACK)
        self.all_sprites.draw(self.screen)
        self.clock.tick(FPS)

        if len(self.green_keys) < 1:
            self.verde = 'OK'
                
            
        if len(self.blue_keys) < 1:
            self.azul = 'OK'

        if len(self.red_keys) < 1:
            self.vermelho = 'OK'

        collectable_green = Button(450, 435, 150, 35, WHITE, BLACK, f"CHAVE VERDE: {self.verde}", 12)
        self.screen.blit(collectable_green.image, collectable_green.rect)

        collectable_blue = Button(250, 435, 150, 35, WHITE, BLACK, f"CHAVE AZUL: {self.azul}", 12)
        self.screen.blit(collectable_blue.image, collectable_blue.rect)

        collectable_red = Button(50, 435, 150, 35, WHITE, BLACK, f"CHAVE VERMELHA: {self.vermelho}", 12)
        self.screen.blit(collectable_red.image, collectable_red.rect)

        pygame.display.update()

    def main(self):
        while self.playing:
            self.events()
            self.update()
            self.draw()

            if self.azul == 'OK' and self.verde == 'OK' and self.vermelho == 'OK':
                self.playing = False
                self.win_screen()
    
    def game_over(self): #algo de errado nesta função, não consegui encontrar
        game_over_screen = True
        text = self.font.render('Game Over', True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        restart_button = Button(10, SCREEN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'RESTART', 26)
        exit_go_button = Button(510, SCREEN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'QUIT', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while game_over_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over_screen = False
                    self.running == False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                game_over_screen = False
                self.select_screen()
                self.new()
                self.main()

            if exit_go_button.is_pressed(mouse_pos, mouse_pressed):
                game_over_screen = False
                self.running = False
                pygame.quit
                sys.exit()

            self.screen.blit(self.gameover_background, (0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(exit_go_button.image, exit_go_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
    
    def intro_screen(self):
        intro = True

        title = self.font.render('ESCAPE OUT', True, BLACK, WHITE)
        title_rect = title.get_rect(x=225, y=25)

        play_button = Button(PLAY_BUTTON_X, PLAY_BUTTON_Y, INTRO_BUTTON_WIDTH, INTRO_BUTTON_HEIGHT, WHITE, BLACK, "JOGAR", FONT_SIZE_INTRO_SCREEN)

        exit_intro_button = Button(EXIT_BUTTON_X, EXIT_BUTTON_Y, INTRO_BUTTON_WIDTH, INTRO_BUTTON_HEIGHT, WHITE, BLACK, "SAIR", FONT_SIZE_INTRO_SCREEN)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False
        
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if exit_intro_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                self.running = False
                pygame.quit
                sys.exit()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
                
            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(title, title_rect)
            self.screen.blit(play_button.image, play_button.rect)
            self.screen.blit(exit_intro_button.image, exit_intro_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()

    def select_screen(self):
        if self.running:
            select = True

            select_title = self.font.render('ESCOLHA SEU PERSONAGEM', True, FONT_SIZE_INTRO_SCREEN, WHITE)
            select_title_rect = select_title.get_rect(x = TITLE_SELECT_SCREEN_X, y = TITLE_SELECT_SCREEN_Y)

            knight_button = Button(KNIGHT_BUTTON_X, KNIGHT_BUTTON_Y, SELECT_BUTTON_WIDTH, SELECT_BUTTON_HEIGHT, WHITE, BLACK, "KNIGHT", FONT_SIZE_SELECT_SCREEN)
            mage_button = Button(MAGE_BUTTON_X, MAGE_BUTTON_Y, SELECT_BUTTON_WIDTH, SELECT_BUTTON_HEIGHT, WHITE, BLACK, "MAGE", FONT_SIZE_SELECT_SCREEN)
            archer_button = Button(ARCHER_BUTTON_X, ARCHER_BUTTON_Y, SELECT_BUTTON_WIDTH, SELECT_BUTTON_HEIGHT, WHITE, BLACK, "ARCHER", FONT_SIZE_SELECT_SCREEN)
            assassin_button = Button(ASSASSIN_BUTTON_X, ASSASSIN_BUTTON_Y, SELECT_BUTTON_WIDTH, SELECT_BUTTON_HEIGHT, WHITE, BLACK, "ASSASSIN", FONT_SIZE_SELECT_SCREEN)
            back_button = Button(BACK_BUTTON_X, BACK_BUTTON_Y, SELECT_BUTTON_WIDTH, SELECT_BUTTON_HEIGHT, WHITE, BLACK, "VOLTAR", FONT_SIZE_SELECT_SCREEN)

            while select:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        self.running = False
                        select = False

                mouse_pos = pygame.mouse.get_pos()
                mouse_pressed = pygame.mouse.get_pressed()

                if knight_button.is_pressed(mouse_pos, mouse_pressed):
                    select = False
                    return "KNIGHT"

                if mage_button.is_pressed(mouse_pos, mouse_pressed):
                    select = False
                    return "MAGE"
                
                if archer_button.is_pressed(mouse_pos, mouse_pressed):
                    select = False
                    return "ARCHER"
                
                if assassin_button.is_pressed(mouse_pos, mouse_pressed):
                    select = False
                    return "ASSASSIN"
                
                if back_button.is_pressed(mouse_pos, mouse_pressed):
                    select = False
                    self.intro_screen()

                self.screen.blit(self.select_screen_background, (0,0))
                self.screen.blit(select_title, select_title_rect)
                self.screen.blit(knight_button.image, knight_button.rect)
                self.screen.blit(mage_button.image, mage_button.rect)
                self.screen.blit(archer_button.image, archer_button.rect)
                self.screen.blit(assassin_button.image, assassin_button.rect)
                self.screen.blit(back_button.image, back_button.rect)
                self.clock.tick(FPS)
                self.playing = True

                pygame.display.update()

    def win_screen(self):
        win_screen = True
        text = self.font.render('PARABÉNS', True, WHITE)
        text_rect = text.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

        restart_button = Button(10, SCREEN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'RESTART', 26)
        exit_go_button = Button(510, SCREEN_HEIGHT - 60, 120, 50, WHITE, BLACK, 'QUIT', 32)

        for sprite in self.all_sprites:
            sprite.kill()

        while win_screen:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    win_screen = False
                    self.running == False
            
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                win_screen = False
                self.select_screen()
                self.new()
                self.main()

            if exit_go_button.is_pressed(mouse_pos, mouse_pressed):
                win_screen = False
                self.running = False
                pygame.quit
                sys.exit()

            self.screen.blit(self.win_background, (0, 0))
            self.screen.blit(text, text_rect)
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(exit_go_button.image, exit_go_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
