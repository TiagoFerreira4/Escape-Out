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




class Check:
    def __init__(self, caminho_musica):
        pygame.mixer.init()
        self.caminho = caminho_musica
        self.som_coletado = None
        self.som_tocado = False
        
        

    def tocar(self):      
        if not self.som_tocado:
            self.som_coletado = pygame.mixer.Sound(self.caminho)
            self.som_coletado.set_volume(1)
            self.som_coletado.play(loops = 0, maxtime=0, fade_ms=0)
            self.som_tocado = True
            

        else:
            self.som_coletado = pygame.mixer.Sound(self.caminho)
            self.som_coletado.set_volume(0.0)
            self.som_coletado.play(loops = 0, maxtime=0, fade_ms=0)
            


        
        

    
        

    

