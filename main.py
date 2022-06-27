import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        
        #general setup
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("legend of poop TWO!!!")
        self.clock = pygame.time.Clock()
    
        self.level = Level()
    
    def run(self):                     
        while True:                     #event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                   
            self.screen.fill("black")
            self.level.run()
            pygame.display.update()
            self.clock.tick(FPS)
     
if __name__ == "__main__":              #checka se è il file principale
    game = Game()                       #chiama la classe
    game.run()                          #chama la funzione run della classe Game