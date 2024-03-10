import pygame
import sys
from Button import Button
from pygame.locals import *
from pandemic import Board, Dice, Player
#import Main_menu
#from Main_menu import *

class DiffSelection():
   
    def __init__(self):
        resolution=(800, 800)
        self.diffselect=0
        self.screen=pygame.display.set_mode(resolution)
    
    def difficulty_selection_popup(self, screen, selected_diff):
        window_x = 225
        window_y = 50
        window = pygame.Surface((window_x, window_y))
        window.fill((240, 128, 128))
        selected_popup = Rect(window_x, window_y, 350, 150) 
        pygame.font.init()
        selected_diff_font = pygame.font.Font('freesansbold.ttf', 15)
        selected_diff_text = selected_diff_font.render(selected_diff, True, (0,0,0))
        selected_diff_rect = selected_diff_text.get_rect(center = (window_x // 2, window_y // 2))
        window.blit(selected_diff_text, selected_diff_rect)
        self.screen.blit(window, (550, 550))
        pygame.display.flip()


    
    def Run(self):
        
        pygame.init()
        # screen
        resolution = (800,800)
        color = (172,178,251)
        self.screen.fill(color)
        pygame.display.flip()
        clock = pygame.time.Clock()
        #default difficulty
        difficulty='easy'
        flag=True
        while flag==True:
            #print("test")
            pygame.font.init()
            diff_font = pygame.font.Font('freesansbold.ttf', 35)
            DIFF_TITLE = diff_font.render("Select Difficulty of AI", True, (0,0,0), color)
            DIFF_RECT = DIFF_TITLE.get_rect()
            DIFF_RECT.center = (400, 100) # text positi
            self.screen.blit(DIFF_TITLE, DIFF_RECT)
            pygame.display.flip()
            def_font = pygame.font.Font('freesansbold.ttf', 17)
            DEF_TITLE = def_font.render("NOTE: Difficulty is preset to Easy.", True, (0,0,0), color)
            DEF_RECT = DEF_TITLE.get_rect()
            DEF_RECT.center = (655, 30) # text positin
            self.screen.blit(DEF_TITLE, DEF_RECT)
            pygame.display.flip()
            #print("test")
            button_image = pygame.image.load("button-image.png")
            button_image = pygame.transform.scale(button_image, (250, 45))
            difficulty_image1 = pygame.image.load("EasyDifficulty.png")
            difficulty_image2 = pygame.image.load("MediumDifficulty.png")
            difficulty_image3 = pygame.image.load("HardDifficulty.png")
            difficulty_image1 = pygame.transform.scale(difficulty_image1, (165, 67))
            difficulty_image2 = pygame.transform.scale(difficulty_image2, (175, 67))
            difficulty_image3 = pygame.transform.scale(difficulty_image3, (175, 67))
            BACK = Button(image = button_image, x_pos = 235, y_pos = 625, button_text = "Back to Main Menu", 
                        font = pygame.font.Font("freesansbold.ttf", 20))
            BACK.update(self.screen)
            EASY = Button(image = difficulty_image1, x_pos = 400, y_pos = 175, button_text = '', font = pygame.font.Font("freesansbold.ttf", 20))
            EASY.update(self.screen)
            MEDIUM = Button(image = difficulty_image2, x_pos = 400, y_pos = 325, button_text = '', font = pygame.font.Font("freesansbold.ttf", 20))
            MEDIUM.update(self.screen)
            HARD = Button(image = difficulty_image3, x_pos = 400, y_pos = 475, button_text = '', font = pygame.font.Font("freesansbold.ttf", 20))
            HARD.update(self.screen)
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.diffselect=1
                   # self.screen.fill((0,0,0))
                    if EASY.user_click(pygame.mouse.get_pos()):
                        difficulty = 'easy'
                        DiffSelection.difficulty_selection_popup(self, self.screen, "Difficulty Selected - Easy")
                    if MEDIUM.user_click(pygame.mouse.get_pos()):
                        difficulty = 'medium'
                        DiffSelection.difficulty_selection_popup(self, self.screen, "Difficulty Selected - Medium")
                    if  HARD.user_click(pygame.mouse.get_pos()):
                        difficulty = 'hard'
                        DiffSelection.difficulty_selection_popup(self, self.screen, "Difficulty Selected - Hard")
                    if BACK.user_click(pygame.mouse.get_pos()):
                        self.diffselect = 0
                        self.screen.fill((0,0,0))
                       # restartGame = 0
                        return difficulty
                        flag = False

               
                    


                    

                        

                        