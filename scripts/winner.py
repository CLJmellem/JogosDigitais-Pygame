import sys
import pygame
from scripts.animatedbg import AnimatedBg
from scripts.button import Button
from scripts.obj import Obj
from scripts.scene import Scene
from scripts.settings import *

class Winner(Scene):

    def __init__(self, finalTimer):
        super().__init__()

        self.bg = AnimatedBg("assets/menu/bg.png",[0,0],[0,-HEIGHT],[self.all_sprites])
        
        if(finalTimer < 35):
            self.title = Obj("assets/menu/Bronze.png",[436,166],[self.all_sprites])
        elif(finalTimer >= 35 and finalTimer < 47):
            self.title = Obj("assets/menu/Silver.png",[436,166],[self.all_sprites])
        if(finalTimer >= 47):
            self.title = Obj("assets/menu/gold.png",[436,166],[self.all_sprites])

        self.finalTimer = finalTimer

        self.btn_play = Button("white",64,520, "Return", self.next_scene)
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