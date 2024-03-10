import pygame
import random
import time
from pygame.locals import *
import sys
import os
from Button import *
class TriviaCard():
    def __init__(self):
        self.screen = pygame.display.set_mode((800, 800))
        self.images={}
       # OK = Button(image = button_image, x_pos = 50, y_pos = 50, button_text = "Ok", 
                   # font = pygame.font.Font("freesansbold.ttf", 20))
        #for button in [OK]:
           # button.update(self.screen)
                    #pygame.display.update()

    def load_trivia_images(self):
        #self.images={}
        self.images[1]=pygame.image.load("correct.png").convert()
        self.images[2]=pygame.image.load("incorrect.png").convert()

    def display_correct_incorrect(self,correct):
        if correct==True:
            image1=pygame.transform.scale(self.images[1],(40,40))
            self.screen.blit(image1,(450,620))
        else:
            image2=pygame.transform.scale(self.images[2],(40,40))
            self.screen.blit(image2,(450,620))

    def set_message(self,message):
        self.message=message

    def print_message(self):
        print(self.message)

    def set_location(self,column,row):
        self.column=column
        self.row=row

    def clear_trivia(self):
        window=pygame.Surface((400,180))
        window.fill((0,0,0))
        self.screen.blit(window, (100,620))

    def trivia_card_content(self,AI, question,difficulty, start_ticks):
        
        window_x = 350
        window_y = 150
        window = pygame.Surface((window_x, window_y))
        window.fill((192, 232, 239)) #fixed color contrast for Trivia Cards


        pygame.font.init()
        popup_font = pygame.font.Font('freesansbold.ttf', 10)
        popup_font2 = pygame.font.Font('freesansbold.ttf', 12)
        
        popup_question = popup_font.render(question['question'], True, (0,0,0))
        answerA = popup_font.render(question['A'], True, (0,0,0))
        answerA_rect = answerA.get_rect()
        answerA_rect.move_ip(20,35)
        
        answerB = popup_font.render(question['B'], True, (0,0,0))
        answerB_rect = answerB.get_rect()
        answerB_rect.move_ip(20,65)
        
        answerC = popup_font.render(question['C'], True, (0,0,0))
        answerC_rect = answerC.get_rect()
        answerC_rect.move_ip(20,95)
        
        answerD = popup_font.render(question['D'], True, (0,0,0))
        answerD_rect = answerD.get_rect()
        answerD_rect.move_ip(20,125)
        

        popup_question_rect = popup_question.get_rect(center = (window_x // 2, window_y // 2 - 53))
        exit_font = pygame.font.Font('freesansbold.ttf', 15)
        if(AI==True):
            popup_title = popup_font2.render('Trivia AI Question!', True, (0,0,0))
        else:
            popup_title = popup_font2.render('Trivia Question!', True, (0,0,0))

       

        popup_rect = popup_title.get_rect(center = (window_x // 2, window_y // 2 - 67))

        window.blit(answerA,answerA_rect)
        window.blit(answerB,answerB_rect)
        window.blit(answerC,answerC_rect)
        window.blit(answerD,answerD_rect)
        window.blit(popup_title, popup_rect)

        

        window.blit(popup_question, popup_question_rect)

        

        self.screen.blit(window, (100, 635))
        pygame.display.flip()

        answerA_Button=Rect(30,30,128,12)
        answerA_Button.move_ip(93,641)
        answerB_Button=Rect(30,30,128,12)
        answerB_Button.move_ip(93,670)
        answerC_Button=Rect(30,30,128,12)
        answerC_Button.move_ip(93,700)
        answerD_Button=Rect(30,30,128,12)
        answerD_Button.move_ip(93,730)


        running = True
        points=0

        #AI answering trivia
        while running:
            if AI==True:
                #easy 20% of time correct
                #medium 60% of time correct
                #hard 100% of time correct
                random_num=random.randint(0,10)
                if difficulty=='easy':
                    print('AI DIFFICULTY:easy')
                    if random_num<3:
                        correct_answer=True
                        self.display_correct_incorrect(correct_answer)
                        points=1
                        return points
                    else:
                        correct_answer=False
                        self.display_correct_incorrect(correct_answer)
                        points=0
                        return points
                elif difficulty=='medium':
                    print('AI DIFFICULTY:medium')
                    if random_num<7:
                        correct_answer=True
                        self.display_correct_incorrect(correct_answer)
                        points=1
                        return points
                    else:
                        correct_answer=False
                        self.display_correct_incorrect(correct_answer)
                        points=0
                        return points
                else:
                    print('AI DIFFICULTY:hard')
                    correct_answer=True
                    self.display_correct_incorrect(correct_answer)
                    points=1
                    return points


            else:

                
                #Checking if answser clicked is correct           
                for event in pygame.event.get():    
                    #code for selecting the Trivia card answer
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos=pygame.mouse.get_pos()
                        if answerA_Button.collidepoint(mouse_pos):
                            print('clicked A')
                            #display if correct or incorrect ? Give points to be spent on boosts ?
                            if question['correct'] == 'a':
                                print('Correct! Answer A is the correct choice.')
                                correct_answer = True
                                points=1
                                self.display_correct_incorrect(correct_answer)
                            else:
                                print('Incorrect! The correct answer is:', question['correct'])
                                correct_answer =False
                                self.display_correct_incorrect(correct_answer)
                            
                            #window.fill((0,0,0))
                            #self.screen.blit(window, (100,635))
                            return points
                        

                        elif answerB_Button.collidepoint(mouse_pos):
                            print('clicked B')
                            if question['correct'] == 'b':
                                print('Correct! Answer B is the correct choice.')
                                correct_answer = True
                                points=1
                                self.display_correct_incorrect(correct_answer)
                            else:
                                print('Incorrect! The correct answer is:', question['correct'])
                                correct_answer =False
                                self.display_correct_incorrect(correct_answer)

                            
                            return points
                            

                        elif answerC_Button.collidepoint(mouse_pos):
                            print('clicked C')
                            if question['correct'] == 'c':
                                print('Correct! Answer C is the correct choice.')
                                correct_answer = True
                                points=1
                                self.display_correct_incorrect(correct_answer)
                            else:
                                print('Incorrect! The correct answer is:', question['correct'])
                                correct_answer =False
                                self.display_correct_incorrect(correct_answer)
                            
                            return points
                        

                        elif answerD_Button.collidepoint(mouse_pos):
                            print('clicked D')
                            if question['correct'] == 'd':
                                print('Correct! Answer D is the correct choice.')
                                correct_answer = True
                                points=1
                                self.display_correct_incorrect(correct_answer)
                            else:
                                print('Incorrect! The correct answer is:', question['correct'])
                                correct_answer =False
                                self.display_correct_incorrect(correct_answer)
                        
                            return points
                            
                        
                    
                    
                    #original escape method to remove popup
                    #elif event.type == pygame.KEYDOWN:
                        #if event.key == pygame.K_ESCAPE:
                            #window.fill((0,0,0))
                            #self.screen.blit(window, (100,635))
                            #running = False
                
                    


    def clone(self):
        newCard = TriviaCard()
        newCard.message=self.message
        return newCard


