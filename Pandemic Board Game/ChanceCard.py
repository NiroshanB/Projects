import random
from pygame.locals import *
import player
import pygame


def generateChanceCard(chance_card_num_each_pl):
    chance_card = []
    for player_number in range(4):#4 human players
        chance_column = []
        for i in range(2,15):#14 columns, except the first 2 column and trivia column
            if i == 3 or i == 7 or i == 11:
                continue
            chance_column.append(i)
        chance_row = []
        for i in range(4):#4 rows
            chance_row.append(player_number*4+i)
        random.shuffle(chance_column)
        random.shuffle(chance_row)
        for i in range(chance_card_num_each_pl):#4 in default
            if i >= 4:#if each row has more than 1 chance card
                chance_card.append([chance_column[i],random.choice(chance_row)])
            else:
                chance_card.append([chance_column[i],chance_row[i]])
    for i in range(chance_card_num_each_pl*3):#AI chance card
        chance_card.append([random.randint(1,15),random.randint(16,19)])
    #print(chance_card)
    return chance_card


def chanceEncounter(target_player, chance_card_list, screen, player_num):
    player_pos = [target_player.column,target_player.row]
    if player_pos in chance_card_list:#display chance card encounter pop up
        #print("Chance card encounter!")
        good_chance = positiveChance()
        if good_chance == True:
            encounterPopUp(screen, "You Earned 1 Point!", player_num)
            target_player.player_points += 1
        else:
            encounterPopUp(screen, "But You Lost 1 Point", player_num)
            if target_player.player_points >= 1:
                target_player.player_points -= 1
        chance_card_list.remove(player_pos)
        #print(chance_card_list)



def encounterPopUp(screen, pop_up_message, player_num):
    pop_up_window = pygame.Surface((150,100))
    pop_up_window.fill((215, 147, 224))
    pop_up_rect = pop_up_window.get_rect(midtop=(700,490))
    
    pop_up_font = pygame.font.Font('freesansbold.ttf', 12)
    pop_up_font_large = pygame.font.Font('freesansbold.ttf', 18)

    player_message = 'Player ' + str(player_num)
    player_message_surf = pop_up_font_large.render(player_message, True, 'Black')
    player_message_rect = player_message_surf.get_rect(midtop=(700,503))

    pop_up_title_surf = pop_up_font.render('Encounter Chance Card!', True, 'Black')
    pop_up_title_rect = pop_up_title_surf.get_rect(midtop=(700,535))

    pop_up_message_surf = pop_up_font.render(pop_up_message, True, 'Black')
    pop_up_message_rect = pop_up_message_surf.get_rect(midtop=(700,565))

    screen.blit(pop_up_window,pop_up_rect)
    screen.blit(player_message_surf,player_message_rect)
    screen.blit(pop_up_title_surf,pop_up_title_rect)
    screen.blit(pop_up_message_surf,pop_up_message_rect)


def positiveChance():
    chance = random.random()
    if chance > 0.7:
        return False
    else:
        return True