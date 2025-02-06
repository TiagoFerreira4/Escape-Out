import pygame

class Musica:
    def __init__(self, caminho_musica):
        pygame.mixer.init()
        self.caminho = caminho_musica
        self.musica = None


    def tocar(self):
        self.musica = pygame.mixer.Sound(self.caminho)
        self.musica.set_volume(0.5)
        self.musica.play(loops =-1, maxtime=0, fade_ms=0)


    def parar(self):
        if self.musica:
            self.musica.stop()






        
        

    
        

    

