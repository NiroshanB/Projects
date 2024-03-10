
import pygame
import random
from pygame.locals import *
import sys
import os

class Dice():

    def __init__(self,resolution,outcome,maxVal):
        self.outcome=outcome
        self.max_value=maxVal
        self.resolution=resolution
        self.screen = pygame.display.set_mode(self.resolution)
        
    def load_diceimage(self):
        self.images={}
        self.images[1]=pygame.image.load("one.png").convert()
        self.images[2]=pygame.image.load("two.png").convert()
        self.images[3]=pygame.image.load("three.png").convert()
        return self.images 

    def display_roll(self,rollNumber):
        if rollNumber==1:
            image1=pygame.transform.scale(self.images[1],(160,160))
            self.screen.blit(image1,(620,120))
        elif rollNumber==2:
            image2=pygame.transform.scale(self.images[2],(160,160))
            self.screen.blit(image2,(620,120))
        elif rollNumber==3:
            image3=pygame.transform.scale(self.images[3],(160,160))
            self.screen.blit(image3,(620,120))

    def create_button(self):
        color=(255,0,0)
        diceButton= Rect(30,30,100,50)
        diceButton.move_ip(625,21)
        pygame.draw.rect(self.screen,color,diceButton)
        font=pygame.font.Font('freesansbold.ttf',20)
        text=font.render('Roll Dice',True,(0,0,128))
        textRect=text.get_rect()
        textRect.center=(704,75)
        self.screen.blit(text,textRect)

    def roll_dice(self):
        min_value=1
        #print("Rolling the dice...")
        outcome=random.randint(min_value,self.max_value)
        #print(outcome)
        return outcome