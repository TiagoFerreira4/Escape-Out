from main import *

g = Game()
g.intro_screen()
g.select_screen()
g.new()

while g.running:
    g.main()
    if g.running:
        if g.azul == 'OK' and g.verde == 'OK' and g.vermelho == 'OK':
            g.win_screen()
        else:
            g.game_over()

pygame.quit
sys.exit()
