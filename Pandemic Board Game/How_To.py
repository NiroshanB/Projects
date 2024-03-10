import pygame
import sys
from Button import Button
from pygame.locals import *
from pandemic import Board, Dice, Player
from display import Text
class How_To_Menu():

    def __init__(self):
        resolution=(800, 800)
        self.screen=pygame.display.set_mode(resolution)

    def Run(self):
        pygame.init()
        # screen
        resolution = (800,800)
        color = (173,216,230)
        pygame.display.flip()
        text=Text()
        flag=True
        while flag==True:
            #font
            pygame.display.set_caption("How To Play")
            self.screen.fill(color)
            self.draw_images()
            self.draw_bullet_points()
            
            #How To Instructions
            text.print_sentance("How To Play Pandemic: The Triva Board Game",400,75,25,color)
            text.print_sentance("To begin a player turn click the 'Roll' Button to roll the 3-Sided dice. Then use your cursor to",410,162,15,color)
            text.print_sentance("move your flag forward within your lane.",255,200,15,color)
            text.print_sentance("Upon crossing a Trivia Cell, the player is prompted with a random trivia question. To answer",415,262,15,color)
            text.print_sentance("the trivia question, simply click on any of the four multiple-choice answers.",375,302,15,color)
            text.print_sentance("Within each players lane there are hidden chance cards that can either give one point or",403,362,15,color)
            text.print_sentance("deduct one point.",170,392,15,color)
            text.print_sentance("Players are able to spend these points by clicking the 'Buy Upgrades' button and choosing",415,462,15,color)
            text.print_sentance("either of the 3 options.",192,492,15,color)
            text.print_sentance("To win the game a player must reach the right side of the board before the timer reaches 0.",407,562,15,color)
            
            
            #Return to main menu button
            button_image = pygame.image.load("button-image.png")
            button_image = pygame.transform.scale(button_image, (250, 45))
            BACK = Button(image = button_image, x_pos = 235, y_pos = 700, button_text = "Back to Main Menu", 
                        font = pygame.font.Font("freesansbold.ttf", 20))
            BACK.update(self.screen)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if BACK.user_click(pygame.mouse.get_pos()):
                        self.screen.fill((0,0,0))
                        flag=False

    def draw_bullet_points(self):
        #Function to display the square bullet points
        bullet_point=pygame.image.load("black.png").convert()
        image1=pygame.transform.scale(bullet_point,(25,25))
        self.screen.blit(image1,(50,150))
        self.screen.blit(image1,(50,250))
        self.screen.blit(image1,(50,350))
        self.screen.blit(image1,(50,450))
        self.screen.blit(image1,(50,550))
    
    def draw_images(self):
        #Function to display images along with instructions
        #Recognition > Recall
        roll=pygame.image.load("roll.png").convert()
        image1=pygame.transform.scale(roll,(70,40))
        self.screen.blit(image1,(410,180))
        roll=pygame.image.load("tcell.png").convert()
        image2=pygame.transform.scale(roll,(35,35))
        self.screen.blit(image2,(665,280))
        roll=pygame.image.load("buyupgrade.png").convert()
        image2=pygame.transform.scale(roll,(95,40))
        self.screen.blit(image2,(290,480))
        roll=pygame.image.load("timer.png").convert()
        image2=pygame.transform.scale(roll,(125,40))
        self.screen.blit(image2,(100,580))

    

        