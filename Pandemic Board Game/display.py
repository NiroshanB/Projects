import pygame
import sys
from Button import Button
from pygame.locals import *
from pandemic import Board, Dice, Player

class Text():
    
    def __init__(self):
        resolution=(800, 800)
        self.screen=pygame.display.set_mode(resolution)

    def print_sentance(self,string,x_pos,y_pos,font_size,colour):
        #Refactoring Function
        text_font = pygame.font.Font('freesansbold.ttf', font_size)
        Label = text_font.render(string, 
                True, (0,0,0), colour)
        Label_Rect = Label.get_rect()
        Label_Rect.center = (x_pos, y_pos) #text position
        self.screen.blit(Label,Label_Rect)
