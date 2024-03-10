import pygame
import sys
from Button import Button
from pandemic import Board, Dice, Player
from New_game import *
from display import Text

class MainMenu():
    def __init__(self):
        resolution=(800, 800)
        self.createGame=0
        self.difficulty=0
        self.loadGame=0
        self.how_to_play=0
        self.screen=pygame.display.set_mode(resolution)
    # main menu title
    def Run(self,loadGameFlag): 
        pygame.init()
        # screen
        resolution = (800,800)
        text=Text()
        color = (173,216,230)
        self.screen.fill(color)
        pygame.display.flip()
        clock = pygame.time.Clock()
        flag=True
        while flag==True:
            pygame.display.set_caption("Main Menu")
            pygame.font.init()

            text.print_sentance('Pandemic',400,100,55,color)
            
            button_image = pygame.image.load("button-image.png")
            button_image = pygame.transform.scale(button_image, (250, 45))
            PLAY = Button(image = button_image, x_pos = 400, y_pos = 250, button_text = "Play New Game", 
                        font = pygame.font.Font("freesansbold.ttf", 20))
            LOAD_GAME = Button(image = button_image, x_pos = 400, y_pos = 350, button_text = "Load Game", 
                        font = pygame.font.Font("freesansbold.ttf", 20))
            DIFFICULTY_SELECTION = Button(image = button_image, x_pos = 400, y_pos = 450, button_text = "Select Difficulty",
                            font = pygame.font.Font("freesansbold.ttf", 20))
            HOW_TO_PLAY = Button(image = button_image, x_pos = 400, y_pos = 550, button_text = "How To Play",
                            font = pygame.font.Font("freesansbold.ttf", 20))
            QUIT_GAME = Button(image = button_image, x_pos = 400, y_pos = 650, button_text = "End Game",
                            font = pygame.font.Font("freesansbold.ttf", 20))
            for button in [PLAY, DIFFICULTY_SELECTION, QUIT_GAME, LOAD_GAME, HOW_TO_PLAY]:
                button.update(self.screen)
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if QUIT_GAME.user_click(pygame.mouse.get_pos()):
                            pygame.quit()
                            quit()
                        elif PLAY.user_click(pygame.mouse.get_pos()):
                            pygame.display.set_caption("Create New Game")
                            self.createGame=1
                            #pandemic.main()
                            #self.createGame=1
                            #print("here")
                            self.screen.fill((0,0,0))
                            flag=False
                            #pygame.quit()
                        elif DIFFICULTY_SELECTION.user_click(pygame.mouse.get_pos()):
                            pygame.display.set_caption("Difficulty")
                            self.difficulty=1
                            self.screen.fill((0,0,0))
                            flag=False

                        elif LOAD_GAME.user_click(pygame.mouse.get_pos()) and loadGameFlag==1:
                            pygame.display.set_caption("Loaded Game")
                            self.loadGame=1
                            self.screen.fill((0,0,0))
                            flag=False

                        elif HOW_TO_PLAY.user_click(pygame.mouse.get_pos()):
                            pygame.display.set_caption("How to Play")
                            self.how_to_play=1
                            self.screen.fill((0,0,0))
                            flag=False
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                    pygame.display.update()

    

            

