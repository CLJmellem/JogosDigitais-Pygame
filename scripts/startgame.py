import pygame, sys, threading, time
from scripts.menu import Menu
from scripts.game import Game
from scripts.winner import Winner
from scripts.gameover import GameOver
from scripts.settings import *

class StartGame:

    def __init__(self):

        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        pygame.display.set_caption("Volcano Scape")
        
        self.display = pygame.display.set_mode([WIDTH,HEIGHT])
        self.scene = "menu"
        self.current_scene = Menu() 
        self.max_time = 90
        self.start_ticks=pygame.time.get_ticks() 
        self.tempo_inicial = (pygame.time.get_ticks()-self.start_ticks)/1000
        self.finalTimer = 0
        self.time = int((pygame.time.get_ticks()-self.start_ticks)/1000)
        self.fps = pygame.time.Clock()
    
    def run(self):

        while True: 
            
            if self.scene == "menu" and self.current_scene.active == False:
                self.scene = "game"
                self.start_ticks = pygame.time.get_ticks() 
                self.tempo_inicial = pygame.time.get_ticks() // 1000
                self.max_time = 90
                self.time = int((pygame.time.get_ticks()-self.start_ticks)/1000)
                self.current_scene = Game()

            if self.scene == "game" and self.current_scene.active == True and self.current_scene.stage == 3:
                self.scene = "winner"
                self.current_scene = Winner(self.finalTimer)
            elif self.scene == "game" and self.current_scene.active == False:
                self.scene = "gameover"
                self.current_scene = GameOver()
            elif self.scene == "game" and self.current_scene.active == True and self.finalTimer == 1:
                pygame.mixer.music.load('assets/Sounds/gameover-sound.wav')
                pygame.mixer.music.play(1)
                self.scene = "gameover"
                self.current_scene = GameOver()
            elif (self.scene == "gameover" or self.scene == "winner") and self.current_scene.active == False:
                self.scene = "menu"
                self.current_scene = Menu()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                self.current_scene.events(event)
            
            self.fps.tick(60)

            self.imagem_fundo = pygame.image.load('assets/Background/Vulcano_Pixels.jpg')
            self.display.blit(self.imagem_fundo, (0, 0))
            self.current_scene.draw()
            if(self.scene == "game"):
                self.timerScreen()
            self.current_scene.update()
            pygame.display.flip()
    
    def timerScreen(self):
        fonte = pygame.font.Font(None, 36)

        seconds = (pygame.time.get_ticks()-self.start_ticks)/1000 #calculate how many seconds
        self.time = int(seconds)
        text_content = str(self.max_time - self.time)
        texto_timer = fonte.render("Tempo: {}s".format(text_content), True, (0, 255, 0))
        self.finalTimer = int(text_content)
        self.display.blit(texto_timer, (0, 100))