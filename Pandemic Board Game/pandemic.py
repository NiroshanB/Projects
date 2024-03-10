import pygame
import random
import time
from pygame.locals import *
import sys
import os
from dice import * 
from board import *
from player import *
from Button import *
from Main_menu import *
from TriviaCard import *
from New_game import *
import New_game
import QuestionsList
from Difficulty_Selection import *
import json
from How_To import *
from ChanceCard import *
from display import Text


def main():
    difficulty = 'easy'
    pygame.init()
    restartGame=0
    loadGameFlag=0
    mainmenu1=MainMenu()
    newgame = NewGame()
    howto=How_To_Menu()
    diff=DiffSelection()
    while(restartGame==0):
        mainmenu1.createGame=0
        mainmenu1.createNewGame=0
        mainmenu1.difficulty=0
        newgame.createNewGame=0
        mainmenu1.Run(loadGameFlag)
        
        
        
        #newgame.Run()
        #diff.Run()
        if mainmenu1.createGame==1:
            mainmenu1.screen.fill((0,0,0))
            newgame.Run()
        if mainmenu1.difficulty==1:
            mainmenu1.screen.fill((0,0,0))
            difficulty = diff.Run()
            continue
        if mainmenu1.how_to_play==1:
            mainmenu1.screen.fill((0,0,0))
            howto.Run()
            mainmenu1.how_to_play=0
            continue
        if newgame.createNewGame==1 or mainmenu1.loadGame==1:
            newgame.screen.fill((0,0,0))
            resolution = (800, 800)
            map_size = (20, 15)
            line_width = 3
            clock = pygame.time.Clock()


            square_width = 25
            square_height = 25
            screen = pygame.display.set_mode(resolution)

            #dice
            dice = Dice(resolution,0,3)
            dice_images=dice.load_diceimage()
            BUTTON=Rect(30,30,100,50)
            BUTTON.move_ip(625,21)
            #upgradables
            BUTTON_UP=Rect(30,30,150,50)
            BUTTON_UP.move_ip(595,280)
            BUTTON_UP1=Rect(30,30,150,30)
            BUTTON_UP1.move_ip(595,340)
            BUTTON_UP2=Rect(30,30,150,30)
            BUTTON_UP2.move_ip(595,380)
            BUTTON_UP3=Rect(30,30,150,30)
            BUTTON_UP3.move_ip(595,420)
            BUTTON_WHO1=Rect(30,30,55,15)
            BUTTON_WHO1.move_ip(645,495)
            BUTTON_WHO2=Rect(30,30,55,13)
            BUTTON_WHO2.move_ip(645,517)
            BUTTON_WHO3=Rect(30,30,55,13)
            BUTTON_WHO3.move_ip(645,536)
            BUTTON_WHO4=Rect(30,30,55,15)
            BUTTON_WHO4.move_ip(645,558)
            #SAVE Button
            saveBUTTON= Rect(30,30,30,30)
            saveBUTTON.move_ip(715,-20)

            #board
            board = Board(resolution, map_size, line_width)
            board.screen.fill((0, 0, 0))
            board.save_exit_image()

            #design pattern : prototype 
            triviacard1 = TriviaCard()
            triviacard1.set_message("Trivia Card Question 1: What class is this")
            triviacard2 = TriviaCard()
            triviacard2.set_message("Trivia Card Question 2: What time is it")
            triviacard3 = TriviaCard()
            triviacard3.set_message("Trivia Card Question 3: When is this due")
            tcAI1=triviacard1.clone()
            tcAI2=triviacard2.clone()
            tcAI3=triviacard3.clone()
            triviacard1.load_trivia_images()
            
            # adding multiple players to the array for easy access
            all_sprites = pygame.sprite.Group()
            playersList = []
            if mainmenu1.loadGame==0:
                playersList.append(Player(0,0*4,square_width,square_height, line_width, New_game.name1,0)) 
                playersList.append(Player(0,1*4,square_width,square_height, line_width, New_game.name2,1))
                playersList.append(Player(0,2*4,square_width,square_height, line_width, New_game.name3,2))
                playersList.append(Player(0,3*4,square_width,square_height, line_width, New_game.name4,3))   
                playersList.append(AI(0,16,square_width,square_height, line_width,"swiss_flag.webp",4))
                playersList[4].set_difficulty(difficulty)

            else:
                    f=open('game_data.json',)
                    gameDataRetrieved=json.load(f)
                    all_sprites.empty()
                    playersList.append(Player(gameDataRetrieved['player1_col'],gameDataRetrieved['player1_row'],square_width,square_height, line_width, gameDataRetrieved['player1_country'],0)) 
                    playersList.append(Player(gameDataRetrieved['player2_col'],gameDataRetrieved['player2_row'],square_width,square_height, line_width, gameDataRetrieved['player2_country'],1))
                    playersList.append(Player(gameDataRetrieved['player3_col'],gameDataRetrieved['player3_row'],square_width,square_height, line_width, gameDataRetrieved['player3_country'],2))
                    playersList.append(Player(gameDataRetrieved['player4_col'],gameDataRetrieved['player4_row'],square_width,square_height, line_width, gameDataRetrieved['player4_country'],3))   
                    playersList.append(AI(gameDataRetrieved['player5_col'],gameDataRetrieved['player5_row'],square_width,square_height, line_width,"swiss_flag.webp",4))
                    playersList[4].set_difficulty(gameDataRetrieved['Difficulty'])
                    playersList[0].player_points=gameDataRetrieved['player1_points']
                    playersList[1].player_points=gameDataRetrieved['player2_points']
                    playersList[2].player_points=gameDataRetrieved['player3_points']
                    playersList[3].player_points=gameDataRetrieved['player4_points']
                    playersList[4].player_points=gameDataRetrieved['player5_points']

            
            gameData={
                'player1_col':0,
                'player1_row':0,
                'player1_points':0,
                'player1_country':New_game.name1,
                'player2_col':0,
                'player2_row':4,
                'player2_points':0,
                'player2_country':New_game.name2,
                'player3_col':0,
                'player3_row':8,
                'player3_points':0,
                'player3_country':New_game.name3,
                'player4_col':0,
                'player4_row':12,
                'player4_points':0,
                'player4_country':New_game.name4,
                'player5_col':0,
                'player5_row':16,
                'player5_points':0,
                'Difficulty':playersList[4].difficulty,
                'Player_Turn':0,
                'Timer':0
            }
            
            
            
            
            all_sprites.add(playersList[0], playersList[1] ,playersList[2], playersList[3], playersList[4])
            
            #array that collects data from trivia.txt
            '''trivia_questions = []
            with open('trivia.txt', 'r', encoding='cp1252',errors='ignore') as file:
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
                    })'''
            trivia_questions = QuestionsList.QuestionsList()
            trivia_questions.GenerateQuestions(5, 'trivia.txt')
            
            # main global variables for the game
            roll = 0
            flag = True
            startFlag = 1
            GameRunFlag = True
            playerTurnsDone = False
            if newgame.createNewGame==0:
                playerTurn=gameDataRetrieved['Player_Turn']
            else:
                playerTurn = 0
            firstTurn = 0
            AIturn=False
            moveAccepted=False
            endOfTurn = True
            requireRoll = True
            upgradeClicked=0
            triviaFlag=0
            triviaFlag2=0
            whoFlag=0
            backSingle=0
            restartPlayer=0
            chanceCardGenerated = False
            start_ticks=pygame.time.get_ticks()
            seconds=(pygame.time.get_ticks()-start_ticks)/1000 #calculate how many seconds have elapsed

        
            #main game loop
            while flag:
                if firstTurn==0:
                    
                    board.leaderboardPlace(playersList[0].player_points,playersList[1].player_points,playersList[2].player_points,playersList[3].player_points,playersList[4].player_points)
                    gameData['Player_Turn']=playerTurn
                    board.draw_turn_indicator(screen,'Player : '+str(playerTurn+1))
                    board.draw_timer_box()
                    #board.start_timer()

                    
                    board.clear_timer_number()
                    firstTurn=1
                clock.tick(60)
                
                if chanceCardGenerated == False:
                    chance_card_list = generateChanceCard(4)
                    chanceCardGenerated = True
                
                seconds = (int(seconds)) #print how many seconds
                maxTime=330
                if(mainmenu1.loadGame==1):
                    remainingseconds=gameData['Timer']
                remainingseconds = maxTime - seconds 
                seconds=int((pygame.time.get_ticks()-remainingseconds)/1000) #calculate how many seconds have elapsed
                board.timer_seconds(remainingseconds) 
                gameData['Timer']=remainingseconds
                if(remainingseconds == 0):
                    board.display_seconds_window()
                
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        flag=False

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        mouse_pos=pygame.mouse.get_pos()
                        #print(mouse_pos)
                        if BUTTON.collidepoint(mouse_pos) and requireRoll == True:
                            roll=dice.roll_dice()
                            # print(roll)
                            remaining_steps = roll
                            dice.display_roll(roll)
                            endOfTurn = False
                            requireRoll = False
                            whoFlag=0
                            backSingle=0
                            restartPlayer=0
                            board.clear_upgrade_menu()
                            board.clear_who_menu()
                            upgradeClicked=0
                            pygame.display.flip()

                        if saveBUTTON.collidepoint(mouse_pos):
                            print('player clicked save button!')
                            #dump gameData into .json file and exit to main menu
                            with open('game_data.json','w') as store_file:
                                json.dump(gameData,store_file)
                            board.draw_save_game()
                            newgame.screen.fill((0,0,0))
                            board.save=1
                            loadGameFlag=1
                            flag=False

                        
                        if BUTTON_UP.collidepoint(mouse_pos):
                            
                            #Display Buyable Upgrade Rects
                            mouse_pos=pygame.mouse.get_pos()
                            print("player: "+str(playersList[playerTurn].player_number)+" clicked upgrade")
                            board.create_upgrade_first()
                            board.create_upgrade_second()
                            board.create_upgrade_third()
                            upgradeClicked=1
                        
                        if BUTTON_UP1.collidepoint(mouse_pos) and upgradeClicked==1:
                            #Move themselves forward
                            print("upgrade1 clicked")
                            if(playersList[playerTurn].player_points>0):
                                playersList[playerTurn].update_position(playersList[playerTurn].column+1,playersList[playerTurn].row,square_width,square_height,line_width)
                                playersList[playerTurn].player_points-=1
                            else:
                                #display on screen not enough funds soon
                                print("Not enough points")
                                board.insufficient_funds()

                        if BUTTON_UP2.collidepoint(mouse_pos) and upgradeClicked==1:
                            #Move A player back one
                            #create a function that asks which player, will need for option 3 aswell
                            print("upgrade2 clicked")
                            if(playersList[playerTurn].player_points>0):
                                board.upgrade_who(playersList[playerTurn].player_number)
                                backSingle=1
                                #move the player that was clicked
                                #playersList[playerTurn].player_points-=1
                                whoFlag=1
                            else:
                                print("Not enough points")
                                board.insufficient_funds()

                        if BUTTON_UP3.collidepoint(mouse_pos) and upgradeClicked==1:
                            #Move a player back to the beginning
                            print("upgrade3 clicked")
                            if(playersList[playerTurn].player_points>2):
                                board.upgrade_who(playersList[playerTurn].player_number)
                                restartPlayer=1
                                #move the player to start that was clicked
                                #playersList[playerTurn].player_points-=3
                                whoFlag=1
                            else:
                                print("Not enough points")
                                board.insufficient_funds()
                        #Checking which player the boost is being used on
                        #And if its move back 1 or back to the beginning
                        if BUTTON_WHO1.collidepoint(mouse_pos) and upgradeClicked==1 and whoFlag==1 and playersList[playerTurn].player_points>0:
                            
                            if playersList[playerTurn].player_number==0:
                                if backSingle==1:  
                                    playersList[1].update_position(playersList[1].column-1,playersList[1].row,square_width,square_height,line_width)
                                    playersList[playerTurn].player_points-=1
                                else:
                                    playersList[1].update_position(0,playersList[1].row,square_width,square_height,line_width)
                                    playersList[playerTurn].player_points-=3
                            else:
                                if backSingle==1:
                                    playersList[0].update_position(playersList[0].column-1,playersList[0].row,square_width,square_height,line_width)
                                    playersList[playerTurn].player_points-=1
                                else:
                                    playersList[playerTurn].player_points-=3
                                    playersList[0].update_position(0,playersList[0].row,square_width,square_height,line_width)
                            

                        if BUTTON_WHO2.collidepoint(mouse_pos) and upgradeClicked==1 and whoFlag==1 and playersList[playerTurn].player_points>0:
                            if playersList[playerTurn].player_number<=1:
                                if backSingle==1:
                                    playersList[2].update_position(playersList[2].column-1,playersList[2].row,square_width,square_height,line_width)
                                    playersList[playerTurn].player_points-=1
                                else:
                                    playersList[playerTurn].player_points-=3
                                    playersList[2].update_position(0,playersList[2].row,square_width,square_height,line_width)
                            else:
                                if backSingle==1:
                                    playersList[playerTurn].player_points-=1
                                    playersList[1].update_position(playersList[1].column-1,playersList[1].row,square_width,square_height,line_width)
                                else:
                                    playersList[playerTurn].player_points-=3
                                    playersList[1].update_position(0,playersList[1].row,square_width,square_height,line_width)
                            

                        if BUTTON_WHO3.collidepoint(mouse_pos) and upgradeClicked==1 and whoFlag==1 and playersList[playerTurn].player_points>0:
                            
                            if playersList[playerTurn].player_number==3:  
                                if backSingle==1:
                                    playersList[2].update_position(playersList[2].column-1,playersList[2].row,square_width,square_height,line_width)
                                    playersList[playerTurn].player_points-=1
                                else:
                                    playersList[playerTurn].player_points-=3
                                    playersList[2].update_position(0,playersList[2].row,square_width,square_height,line_width)
                            else:
                                if backSingle==1:
                                    playersList[playerTurn].player_points-=1
                                    playersList[3].update_position(playersList[3].column-1,playersList[3].row,square_width,square_height,line_width)
                                else:
                                    playersList[playerTurn].player_points-=3
                                    playersList[3].update_position(0,playersList[3].row,square_width,square_height,line_width)
                            

                        if BUTTON_WHO4.collidepoint(mouse_pos) and upgradeClicked==1 and whoFlag==1 and playersList[playerTurn].player_points>0:
                            if backSingle==1:
                                playersList[playerTurn].player_points-=1
                                playersList[4].update_position(playersList[4].column-1,playersList[4].row,square_width,square_height,line_width)
                            else:
                                playersList[playerTurn].player_points-=3
                                playersList[4].update_position(0,playersList[4].row,square_width,square_height,line_width)
                            

                        

                        if GameRunFlag:
                            board.leaderboardPlace(playersList[0].player_points,playersList[1].player_points,playersList[2].player_points,playersList[3].player_points,playersList[4].player_points)
                            
                            if roll != 0:
                                #playerTurn = 0
                                
                                if (playerTurn == 0 or playerTurn==1 or playerTurn == 2 or playerTurn == 3): 
                                    
                                    triviacard1.clear_trivia()
                                    board.draw_turn_indicator(screen,'Player : '+str(playerTurn+1))
                                    
                
                                    mouse_pos = pygame.mouse.get_pos()
                                    column = int((mouse_pos[0] - 81) / (square_width + line_width))
                                    row = int((mouse_pos[1] - 50) / (square_height + line_width))
                                    dx = abs(column - playersList[playerTurn].column)
                                    dy = abs(row - playersList[playerTurn].row)

                                    direction = ""
                                    if column > playersList[playerTurn].column:
                                        direction = "right"
                                    elif column < playersList[playerTurn].column:
                                        direction = "left"
                                    elif row > playersList[playerTurn].row:
                                        direction = "down"
                                    elif row < playersList[playerTurn].row:
                                        direction = "up"

                                    if remaining_steps >= 0 and direction in ["right"] and dx <= 1 and dy <= 1 and endOfTurn == False:

                                        moveAccepted=playersList[playerTurn].update_position(column, row, square_width, square_height, line_width)
                                        #if mouse click was a valid position for player to move
                                        if moveAccepted==True:
                                            remaining_steps -= 1
                                            gameData['player'+str(playerTurn+1)+'_col']=playersList[playerTurn].column
                                            gameData['player'+str(playerTurn+1)+'_row']=playersList[playerTurn].row
                                        if remaining_steps == 0:
                                            endOfTurn = True
                                            requireRoll = True
                                            playerTurn= (playerTurn+1)%5
                                            board.draw_turn_indicator(screen, 'Player : '+str(playerTurn+1))
                                            gameData['Player_Turn']=playerTurn

                                    # Trivia card encountering code 
                                    if((playersList[playerTurn].column == 3 and remaining_steps > 0 and playersList[playerTurn].trivia1==0) 
                                    or (playersList[playerTurn].column == 7 and remaining_steps > 0 and playersList[playerTurn].trivia2==0) 
                                    or (playersList[playerTurn].column == 11 and remaining_steps > 0 and playersList[playerTurn].trivia3==0)):
                                        if playersList[playerTurn].column == 3:
                                            playersList[playerTurn].trivia1=1
                                        if playersList[playerTurn].column==7:
                                            playersList[playerTurn].trivia2=1
                                        if playersList[playerTurn].column==11:
                                            playersList[playerTurn].trivia3=1
                                        #accesing trivia_questions array for random question
                                        '''selected_question = random.choice(trivia_questions)
                                        selected_index = trivia_questions.index(selected_question)
                                        del trivia_questions[selected_index]'''
                                        selected_question = trivia_questions.questions_list.pop(0)
                                    
                                        points=triviacard1.trivia_card_content(False,selected_question,'none', start_ticks)
                                        
                                        playersList[playerTurn].player_points+=points
                                        gameData['player'+str(playerTurn+1)+'_points']=playersList[playerTurn].player_points
                                    chanceEncounter(playersList[playerTurn], chance_card_list, screen, playerTurn+1)
                                    
                                    #win condition for the players   
                                    if (playersList[playerTurn].column >= 14):
                                        board.display_winner_window("Player : "+ str(playersList[playerTurn].player_number + 1))
                                        GameRunFlag = False

                                #if it is the AIs move
                                if(playerTurn==4):
                                        
                                    start_ticks=pygame.time.get_ticks() #gets the current time in milliseconds 
                                
                                    #dice roll and turn indicator for AI
                                    roll=dice.roll_dice()
                                    dice.display_roll(roll)
                                    pygame.display.flip()
                                    board.draw_turn_indicator(screen,"AI turn")
                                        #print(roll)
                                    
                                    #AI movement 
                                    triviaFlag=playersList[4].move(roll, square_width, square_height, line_width,tcAI1,tcAI2,tcAI3)
                                    
                                    #AI buying upgrades
                                    if playersList[4].difficulty=='easy' and playersList[4].player_points>2:
                                        #easy = AI waits for 3 points to purchase upgrade
                                        #finds player furthest to the cure
                                        player=max(playersList[0].column,playersList[1].column,playersList[2].column,playersList[3].column)
                                        playerIndex=player-1
                                        playersList[playerIndex].update_position(playersList[playerIndex].column-1,playersList[playerIndex].row,square_width,square_height,line_width)
                                    elif playersList[4].difficulty=='medium' and playersList[4].player_points>0:
                                        #medium = AI buys move forward 50% of time
                                        random_num=random.randint(0,10)
                                        if random_num > 4:
                                            playersList[4].player_points-=1
                                            triviaFlag2=playersList[4].move(1, square_width, square_height, line_width,tcAI1,tcAI2,tcAI3)
                                    elif playersList[4].difficulty=='hard' and playersList[4].player_points>0:
                                        #hard = AI buys move forwards each time + answers all correctly
                                        playersList[4].player_points-=1
                                        triviaFlag2=playersList[4].move(1, square_width, square_height, line_width,tcAI1,tcAI2,tcAI3)
                                    time.sleep(1)
                                    if triviaFlag==1 or triviaFlag2==1:
                                        #selected_question = random.choice(trivia_questions)
                                        selected_question = trivia_questions.questions_list.pop(0)
                                        points=triviacard1.trivia_card_content(True,selected_question,playersList[4].difficulty,start_ticks)
                                        playersList[4].player_points+=points
                                    
                                    
                                    playerTurn=0
                                    board.draw_turn_indicator(screen,'Player : 1')
                                    pygame.display.flip()

                                    chanceEncounter(playersList[4], chance_card_list, screen, 5)

                                    #win condition
                                    if (playersList[4].column > 14):
                                        board.display_winner_window("AI")
                                        GameRunFlag = False

                                        
            
                #object rendering on screen
                board.draw_squares()
                board.create_upgrade_button()
                board.place_trivia_cards() 
                dice.create_button()
                board.draw_exit_box()
                all_sprites.draw(screen)
                #pygame.time.delay(15)
                pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()