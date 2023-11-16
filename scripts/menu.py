import sys
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.button import Button
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *

class Menu(Scene):

    def __init__(self):
        super().__init__()

        self.bg = AnimatedBg("assets/menu/bg.png",[0,0],[0,-HEIGHT],[self.all_sprites])
        self.title = Obj("assets/menu/title.png",[436,166],[self.all_sprites])

        self.btn_play = Button("white",64,520, "Play", self.next_scene)
        self.btn_quit = Button("white",64,600, "Quit", self.quit_game)
    
    def next_scene(self):
        self.active = False
    
    def quit_game(self):
        pygame.quit()
        sys.exit()

    def events(self, event):
        self.btn_play.events(event)
        self.btn_quit.events(event)
        return super().events(event)

    def update(self):
        self.bg.update()
        self.btn_play.draw()
        self.btn_quit.draw()
        return super().update()




