import pygame
from abc import ABC, abstractmethod
import random
from pygame.locals import *
import sys
import os

class CharacterFactory(pygame.sprite.Sprite,ABC):
    def __init__(self,column, row, width, height, line_width, image_path, player_number):
    
        pygame.sprite.Sprite.__init__(self)
        self.images=[]
        self.player_number = player_number
        self.player_points = 0
        img = pygame.image.load(os.path.join(image_path)).convert()
        self.images.append(img)
        self.image = self.images[0]
        #self.image = pygame.Surface([width, height])
        self.image = pygame.transform.scale(img, (22, 15))
        #rectangular object
        self.rect = self.image.get_rect() 
        self.column = column
        self.row = row
        self.rect.x = self.column * (width + line_width) + line_width + 81
        self.rect.y = self.row * (height + line_width) + line_width + 55
        self.trivia1=0
        self.trivia2=0
        self.trivia3=0



    @abstractmethod
    def update_position(self,column, row, width, height, line_width):
        
        self.column = column
        self.row = row
        self.rect.x = self.column * (width + line_width) + line_width + 81
        self.rect.y = self.row * (height + line_width) + line_width + 50

    @abstractmethod
    def move(self, dice_roll, square_width, square_height, line_width):
       
        while dice_roll > 0:
            directions = ["right", "down", "up"]

            direction = random.choice(directions)
            dx = 0
            dy = 0
            if direction == "right":
                dx = 1
            elif direction == "down":
                dy = 1
                dx = 1
            elif direction == "up":
                dy = -1
                dx = 1

            new_column = self.column + dx
            new_row = self.row + dy 
            
            #print(direction)
            #print(new_column, new_row)
            
            self.update_position(new_column, new_row, square_width, square_height, line_width) 
            pygame.display.flip()
            dice_roll -= 1 
    
    @abstractmethod
    def update(self,player_turn):
        pass





class Player(CharacterFactory):
    def __init__(self,column, row, width, height, line_width, image_path, player_number):
        super().__init__(column, row, width, height, line_width,image_path,player_number)
    

    def update_position(self,column, row, width, height, line_width):
        if self.player_number==0:
            top_bound=0
            bot_bound=4
        if self.player_number==1:
            top_bound=4
            bot_bound=8
        if self.player_number==2:
            top_bound=8
            bot_bound=12
        if self.player_number==3:
            top_bound=12
            bot_bound=16
        
        
        if 0 <= column < 15 and top_bound <= row < bot_bound:
            self.column = column
            self.row = row
            self.rect.x = self.column * (width + line_width) + line_width + 81
            self.rect.y = self.row * (height + line_width) + line_width + 50
            return True
            
        
    

    def move(self):
        pass

    def update(self,player_turn):
        if player_turn == self.player_number:
            print("This is the players turn")






class AI(CharacterFactory):
    def __init__(self,column, row, width, height, line_width,image_path,player_number):
        super().__init__(column, row, width, height, line_width, image_path, player_number)
    

    def update_position(self,column, row, width, height, line_width):
        if 0 <= column <= 16 and 16 <= row < 20:
            self.column = column
            self.row = row
            self.rect.x = self.column * (width + line_width) + line_width + 81
            self.rect.y = self.row * (height + line_width) + line_width + 50
            return True
        return False

    def set_difficulty(self,rating):
        self.difficulty=rating

    
    def move(self, dice_roll, square_width, square_height, line_width,trivia1,trivia2,trivia3):
        #points=0
        hitTriviaFlag=0
        while dice_roll > 0:
            directions = ["right", "down", "up"]

            if self.row == 4:
                directions = ["right","down"]
            
            if self.row == 7:
                directions = ["right","up"]

            direction = random.choice(directions)
            dx = 0
            dy = 0
            if direction == "right":
                dx = 1
            elif direction == "down":
                dy = 1
                dx = 1
            elif direction == "up":
                dy = -1
                dx = 1

            new_column = self.column + dx
            new_row = self.row + dy 
            # print(direction)
            # print(new_column, new_row)


            trivia_questions = []
            with open('trivia.txt', 'r',encoding='cp1252',errors='ignore') as file:
                lines = file.readlines()
                for i in range(0, len(lines), 6):
                    question = lines[i].strip()
                    optionA = lines[i + 1].strip()
                    optionB = lines[i + 2].strip()
                    optionC = lines[i + 3].strip()
                    optionD = lines[i + 4].strip()
                    correct_answer = lines[i + 5].strip().split(":")[1].strip()
                    trivia_questions.append({
                        'question': question,
                        'A': optionA,
                        'B': optionB,
                        'C': optionC,
                        'D': optionD,
                        'correct': correct_answer
                    })


            flag=self.update_position(new_column, new_row, square_width, square_height, line_width) 
            pygame.display.flip()
            if((new_column == 4) or (new_column == 8) or (new_column == 12)):
                if new_column==4 and self.trivia1==0:
                    hitTriviaFlag=1
                    self.trivia1=1
                if new_column==8 and self.trivia2==0:
                    hitTriviaFlag=1
                    self.trivia2=1
                if new_column==12 and self.trivia3==0:
                    hitTriviaFlag=1
                    self.trivia3=1
                #selected_question = random.choice(trivia_questions)
                #points=trivia1.trivia_card_content(True,selected_question)
                
                
            if flag==True:
                dice_roll -= 1 
        return hitTriviaFlag
        
        
    def update(self,player_turn):
        if player_turn == self.player_number:
            print("This is the AIs turn")
    



