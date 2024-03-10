import pygame
import sys
from Button import Button
from pygame.locals import *
from pandemic import Board, Dice, Player
from display import Text
class NewGame():
    def __init__(self):
        resolution=(800, 800)
        self.createNewGame=0
        self.screen=pygame.display.set_mode(resolution)
        

    # main menu title
    def Run(self): 
        pygame.init()
        # screen
        resolution = (800,800)
        color = (172,178,251)
        self.screen.fill(color)
        pygame.display.flip()
        text_write=Text()
        clock = pygame.time.Clock()
        global text 
        global text2 
        global text3 
        global text4 
        global listName
        listName = ["1", "2", "3", "4"]
        text = ["Select Country 1"]
        text2 = ["Select Country 2"]
        text3 = ["Select Country 3"]
        text4 = ["Select Country 4"]
        flag=True
        self.screen.fill(color)
        text_write.print_sentance("Select Your Country",400,100,34,(172,178,251))
        while flag==True:
            pygame.display.set_caption("Create New Game")
            DropDownMenu.draw_selection_button(self, self.screen, 400, 175, 400, 325, 400, 475, 400, 625, text)
            button_image = pygame.image.load("button-image.png")
            button_image = pygame.transform.scale(button_image, (250, 45))
            CREATE_GAME = Button(image = button_image, x_pos = 650, y_pos = 625, button_text = "Create Game", 
                        font = pygame.font.Font("freesansbold.ttf", 20))
          
            for button in [CREATE_GAME]:
                if text[0] != "Select Country 1" and text2[0] != "Select Country 2" and text3[0] != "Select Country 3" and text4[0] != "Select Country 4":
                    button.update(self.screen)
            for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if CREATE_GAME.user_click(pygame.mouse.get_pos()):
                            pygame.display.set_caption("New Game")
                            
                            self.createNewGame=1
                            
                            self.screen.fill((0,0,0))
                            flag=False
                        
                
                    pygame.display.update()

class DropDownMenu():
    def __init__(self, color, font, option_list, active_option):
        self.color = color
        self.font = font
        self.option_list = option_list
        self.selected = False
        self.active_option = active_option

    def draw_option(self, screen,text, winx, winy, x_pos, y_pos, color = (0,0,0)):
        self.active_option = 0
        self.option_list = []
        window_x = winx
        window_y = winy
        window = pygame.Surface((window_x, window_y))
        window.fill(color) 
        pygame.font.init()
        dropdownfont = pygame.font.Font('freesansbold.ttf', 14)
        dropdown = dropdownfont.render(text, True, (0,0,0))
        dropdown_rect = dropdown.get_rect(center = (winx // 2, winy // 2))

        window.blit(dropdown, dropdown_rect)
        self.screen.blit(window, (x_pos, y_pos))
        pygame.display.flip()
    


    def draw_selection_button(self, screen, x_pos, y_pos,x_pos2, y_pos2,x_pos3, y_pos3,x_pos4, y_pos4, text):
       
        
        dropdown_button = Rect(275, 200, 125, 45)
        dropdown_button2 = Rect(400, 200, 125, 45)
        dropdown_button3 = Rect(275, 245, 125, 45)
        dropdown_button4 = Rect(400, 245, 125, 45)

        dropdown_button5 = Rect(275, 350, 125, 45)
        dropdown_button6 = Rect(400, 350, 125, 45)
        dropdown_button7 = Rect(275, 395, 125, 45)
        dropdown_button8 = Rect(400, 395, 125, 45)

        dropdown_button9 = Rect(275, 500, 125, 45)
        dropdown_button10 = Rect(400, 500, 125, 45)
        dropdown_button11 = Rect(275, 545, 125, 45)
        dropdown_button12 = Rect(400, 545, 125, 45)

        dropdown_button13 = Rect(275, 650, 125, 45)
        dropdown_button14 = Rect(400, 650, 125, 45)
        dropdown_button15 = Rect(275, 695, 125, 45)
        dropdown_button16 = Rect(400, 695, 125, 45)
        
        button_image = pygame.image.load("select-country-button.png")
        button_image = pygame.transform.scale(button_image, (250, 50))
        OPTION_1 = Button(image = button_image, x_pos = x_pos, y_pos = y_pos, 
            button_text = text[0], font = pygame.font.Font("freesansbold.ttf", 18))
        OPTION_1.update(self.screen)

        OPTION_2 = Button(image = button_image, x_pos = x_pos2, y_pos = y_pos2, 
            button_text = text2[0], font = pygame.font.Font("freesansbold.ttf", 18))
        OPTION_2.update(self.screen)

        OPTION_3 = Button(image = button_image, x_pos = x_pos3, y_pos = y_pos3, 
            button_text = text3[0], font = pygame.font.Font("freesansbold.ttf", 18))
        OPTION_3.update(self.screen)

        OPTION_4 = Button(image = button_image, x_pos = x_pos4, y_pos = y_pos4, 
            button_text = text4[0], font = pygame.font.Font("freesansbold.ttf", 18))
        OPTION_4.update(self.screen)


        for event in pygame.event.get():
                    SKY_BLUE = (118, 197, 234)
                    BLUE = (118, 158, 234)
                    PASTEL_BLUE = (120, 118, 234)
                    DODGER_BLUE = (66, 97, 252)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTION_1.user_click(pygame.mouse.get_pos()):
                            DropDownMenu.draw_option(self, self.screen, "Player 1 - Canada", 125, 45, 275, 200, color = SKY_BLUE )
                            DropDownMenu.draw_option(self, self.screen, "Player 1 - China", 125, 45, 400, 200, color = BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 1 - Mexico", 125, 45, 275, 245, color = PASTEL_BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 1 - India", 125, 45, 400, 245, color = DODGER_BLUE)
          
                        DropDownMenu.selectFlag(self, dropdown_button, dropdown_button2, dropdown_button3, dropdown_button4, OPTION_1, text, 1, listName)

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTION_2.user_click(pygame.mouse.get_pos()):
                            DropDownMenu.draw_option(self, self.screen, "Player 2 - Canada", 125, 45, 275, 350, color = SKY_BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 2 - China", 125, 45, 400, 350, color = BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 2 - Mexico", 125, 45, 275, 395, color = PASTEL_BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 2 - India", 125, 45, 400, 395, color = DODGER_BLUE)
          
                        DropDownMenu.selectFlag(self, dropdown_button5, dropdown_button6, dropdown_button7, dropdown_button8, OPTION_2, text2, 2, listName) 

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTION_3.user_click(pygame.mouse.get_pos()):
                            DropDownMenu.draw_option(self, self.screen, "Player 3 - Canada", 125, 45, 275, 500, color = SKY_BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 3 - China", 125, 45, 400, 500, color = BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 3 - Mexico", 125, 45, 275, 545, color = PASTEL_BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 3 - India", 125, 45, 400, 545, color = DODGER_BLUE)
          
                        DropDownMenu.selectFlag(self, dropdown_button9, dropdown_button10, dropdown_button11, dropdown_button12, OPTION_3, text3, 3, listName) 

                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if OPTION_4.user_click(pygame.mouse.get_pos()):
                            DropDownMenu.draw_option(self, self.screen, "Player 4 - Canada", 125, 45, 275, 650, color = SKY_BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 4 - China", 125, 45, 400, 650, color = BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 4 - Mexico", 125, 45, 275, 695, color = PASTEL_BLUE)
                            DropDownMenu.draw_option(self, self.screen, "Player 4 - India", 125, 45, 400, 695, color = DODGER_BLUE)
          
                        DropDownMenu.selectFlag(self, dropdown_button13, dropdown_button14, dropdown_button15, dropdown_button16, OPTION_4, text4, 4, listName)           


                                    
                            
        pygame.display.flip()

    def selectFlag(self, dropdown_button, dropdown_button2, dropdown_button3, dropdown_button4, OPTION_1, text, playerNum, listName1):
         
        
        mouse_pos1=pygame.mouse.get_pos()
        if dropdown_button.collidepoint(mouse_pos1):
            OPTION_1.set_text("Player" + str(playerNum) + " - Canada")
            text[0] = "Player" + str(playerNum) + " - Canada"
            OPTION_1.update(self.screen)
            listName1[playerNum - 1] = "canada.png"
        
        mouse_pos2=pygame.mouse.get_pos()
        if dropdown_button2.collidepoint(mouse_pos2):
            print('test')
            OPTION_1.set_text("Player" + str(playerNum) + " - China")
            text[0] = "Player" + str(playerNum) + " - China"
            OPTION_1.update(self.screen)
            listName1[playerNum - 1] = "china.png"
        mouse_pos3=pygame.mouse.get_pos()
        if dropdown_button3.collidepoint(mouse_pos3):
            print('test')
            OPTION_1.set_text("Player" + str(playerNum) + " - Mexico")
            text[0] = "Player" + str(playerNum) + " - Mexico"
            OPTION_1.update(self.screen) 
            listName1[playerNum - 1] = "mexico.png"
        mouse_pos4=pygame.mouse.get_pos()
        if dropdown_button4.collidepoint(mouse_pos3):
            print('test')
            OPTION_1.set_text("Player" + str(playerNum) + " - India")
            text[0] = "Player" + str(playerNum) + " - India"
            OPTION_1.update(self.screen)
            listName1[playerNum - 1] = "india.png"   

        if playerNum == 1:
            global name1
            name1 = listName1[playerNum - 1]
        elif playerNum == 2:
            global name2
            name2 = listName1[playerNum - 1]   
        elif playerNum == 3:
            global name3
            name3 = listName1[playerNum - 1] 
        elif playerNum == 4:
            global name4
            name4 = listName1[playerNum - 1]    
