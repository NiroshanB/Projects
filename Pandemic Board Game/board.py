import pygame
import random
import time
from pygame.locals import *
import sys
import os
from Button import *


class Board():
    def __init__(self, resolution, map_size, line_width):
        self.resolution = resolution
        self.map_size = map_size
        self.line_width = line_width
        self.screen = pygame.display.set_mode(self.resolution)
        self.observer_list = []
        self.exit_image = {}
        self.save = 0
        self.BLACK = (0, 0, 0)
        self.PINK = (255, 192, 203)
        self.NAVY_BLUE = (0, 0, 128)
        self.PURPLE = (173,42,238)
    def evaluate_dimensions(self):
        return (25, 25)

    def convert_column_to_x(self, column, square_width):
        x = self.line_width * (column + 1) + square_width * column
        return x

    def convert_row_to_y(self, row, square_height):
        y = self.line_width * (row + 1) + square_height * row
        return y

    def clear_upgrade_menu(self):
        color = self.BLACK
        diceButton = Rect(30, 30, 150, 230)
        diceButton.move_ip(595, 340)
        pygame.draw.rect(self.screen, color, diceButton)

    def clear_who_menu(self):
        color = self.BLACK
        whoMenu = Rect(30, 30, 150, 115)
        whoMenu.move_ip(595, 465)
        pygame.draw.rect(self.screen, color, whoMenu)

    def insufficient_funds(self):
        color = (255, 0, 0)
        diceButton = Rect(30, 30, 150, 40)
        diceButton.move_ip(595, 465)
        pygame.draw.rect(self.screen, color, diceButton)
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render('Not Enough Points!', True, self.NAVY_BLUE)
        textRect = text.get_rect()
        textRect.center = (700, 515)
        self.screen.blit(text, textRect)

    def upgrade_who(self, player_num):
        player_numbers = [1, 2, 3, 4, 5]
        player_numbers.pop(player_num)
        color = (255, 0, 0)
        diceButton = Rect(30, 30, 150, 115)
        diceButton.move_ip(595, 465)
        pygame.draw.rect(self.screen, color, diceButton)
        font = pygame.font.Font('freesansbold.ttf', 15)
        font2 = pygame.font.Font('freesansbold.ttf', 14)
        text = font.render('Which Player?', True, self.NAVY_BLUE)
        textRect = text.get_rect()
        textRect.center = (700, 510)
        player1 = font2.render('Player ' + str(player_numbers[0]), True, self.NAVY_BLUE)
        player1Rect = player1.get_rect()
        player1Rect.center = (700, 532)
        player2 = font2.render('Player ' + str(player_numbers[1]), True, self.NAVY_BLUE)
        player2Rect = player2.get_rect()
        player2Rect.center = (700, 552)
        player3 = font2.render('Player ' + str(player_numbers[2]), True, self.NAVY_BLUE)
        player3Rect = player3.get_rect()
        player3Rect.center = (700, 572)
        player4 = font2.render('Player ' + str(player_numbers[3]), True, self.NAVY_BLUE)
        player4Rect = player4.get_rect()
        player4Rect.center = (700, 592)
        self.screen.blit(text, textRect)
        self.screen.blit(player1, player1Rect)
        self.screen.blit(player2, player2Rect)
        self.screen.blit(player3, player3Rect)
        self.screen.blit(player4, player4Rect)

    def create_upgrade_button(self):
        color = (255, 0, 0)
        diceButton = Rect(30, 30, 150, 50)
        diceButton.move_ip(595, 280)
        pygame.draw.rect(self.screen, color, diceButton)
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('Buy Upgrades', True, self.NAVY_BLUE)
        textRect = text.get_rect()
        textRect.center = (700, 335)
        self.screen.blit(text, textRect)

    def create_upgrade_first(self):
        color = (255, 0, 0)
        diceButton = Rect(30, 30, 150, 30)
        diceButton.move_ip(595, 340)
        pygame.draw.rect(self.screen, color, diceButton)
        font = pygame.font.Font('freesansbold.ttf', 13)
        text = font.render('1:Move Self Forward 1', True, self.NAVY_BLUE)
        textRect = text.get_rect()
        textRect.center = (700, 387)
        self.screen.blit(text, textRect)

    def create_upgrade_second(self):
        color = (255, 0, 0)
        diceButton = Rect(30, 30, 150, 30)
        diceButton.move_ip(595, 380)
        pygame.draw.rect(self.screen, color, diceButton)
        font = pygame.font.Font('freesansbold.ttf', 13)
        text = font.render('1:Move Player Back 1', True, self.NAVY_BLUE)
        textRect = text.get_rect()
        textRect.center = (697, 425)
        self.screen.blit(text, textRect)

    def create_upgrade_third(self):
        color = (255, 0, 0)
        diceButton = Rect(30, 30, 150, 30)
        diceButton.move_ip(595, 420)
        pygame.draw.rect(self.screen, color, diceButton)
        font = pygame.font.Font('freesansbold.ttf', 13)
        text = font.render('3:Move Player to Start', True, self.NAVY_BLUE)
        textRect = text.get_rect()
        textRect.center = (700, 465)
        self.screen.blit(text, textRect)

    def leaderboardPlace(self, p1, p2, p3, p4, p5):
        color = (215, 147, 224)
        leaderBoard = Rect(30, 30, 200, 145)
        leaderBoard.move_ip(500, 605)
        pygame.draw.rect(self.screen, color, leaderBoard)
        font = pygame.font.Font('freesansbold.ttf', 20)
        title = font.render('Player Points', True, self.BLACK)
        font2 = pygame.font.Font('freesansbold.ttf', 15)
        title_rect = title.get_rect(center=(630, 655))
        player1 = font2.render('Player 1 : ' + str(p1), True, self.BLACK)
        player1_rect = player1.get_rect(center=(585, 680))
        player2 = font2.render('Player 2 : ' + str(p2), True, self.BLACK)
        player2_rect = player2.get_rect(center=(585, 700))
        player3 = font2.render('Player 3 : ' + str(p3), True, self.BLACK)
        player3_rect = player3.get_rect(center=(585, 720))
        player4 = font2.render('Player 4 : ' + str(p4), True, self.BLACK)
        player4_rect = player4.get_rect(center=(585, 740))
        player5 = font2.render('Player 5 : ' + str(p5), True, self.BLACK)
        player5_rect = player5.get_rect(center=(585, 760))
        self.screen.blit(title, title_rect)
        self.screen.blit(player1, player1_rect)
        self.screen.blit(player2, player2_rect)
        self.screen.blit(player3, player3_rect)
        self.screen.blit(player4, player4_rect)
        self.screen.blit(player5, player5_rect)

    def place_trivia_cards(self):
        y_val = 67
        x_val = 177
        font = pygame.font.Font('freesansbold.ttf', 20)
        text = font.render('T', True, self.BLACK)
        for y in range(3):
            for x in range(20):
                textRect = text.get_rect()
                textRect.center = (x_val, y_val)
                self.screen.blit(text, textRect)
                y_val += 28
            x_val += 112
            y_val = 67

    def start_timer(self):
        print('doesnt work gets stuck in loop')
        clock = pygame.time.Clock()
        counter = 40
        font = pygame.font.Font('freesansbold.ttf', 15)
        text = font.render(str(counter), True, (255, 0, 0))
        timer_event = pygame.USEREVENT + 1
        pygame.time.set_timer(timer_event, 1000)
        run = True
        while run:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == timer_event:
                    counter -= 1
                    text = font.render(str(counter), True, (255, 0, 0))
                    if counter == 0:
                        pygame.time.set_timer(timer_event, 0)
            self.clear_timer_number()
            text_rect = text.get_rect()
            text_rect.move_ip(0, 260)
            self.screen.blit(text, text_rect)
            pygame.display.flip()

    def draw_squares(self):
        square_width, square_height = self.evaluate_dimensions()
        color = (255, 0, 0)
        color2 = (0, 255, 0)
        rect1 = Rect(30, 26, 100, 559)
        rect1.move_ip(470, 26)
        pygame.draw.rect(self.screen, color2, rect1)
        rect2 = Rect(30, 26, 100, 559)
        rect2.move_ip(-50, 26)
        pygame.draw.rect(self.screen, color, rect2)
        color3 = (255, 204, 153)
        color4 = (255, 153, 51)
        color5 = (255, 102, 102)
        line_color = self.BLACK
        for row in range(self.map_size[0]):
            for column in range(self.map_size[1]):
                if column == 3 or column == 7 or column == 11:
                    color = self.PURPLE
                else:
                    if column % 2 == 1:
                        if row % 2 == 1:
                            color = color5
                        elif row % 2 == 0:
                            color = color3
                    elif column % 2 == 0:
                        if row % 2 == 1:
                            color = color3
                        elif row % 2 == 0:
                            color = color4
                x = self.convert_column_to_x(column, square_width)
                y = self.convert_row_to_y(row, square_height)
                geometry = (x + 78, y + 50, square_width, square_height)
                pygame.draw.rect(self.screen, color, geometry)
                pygame.draw.line(self.screen, line_color, (80, 164), (499, 164), 7)
                pygame.draw.line(self.screen, line_color, (80, 275), (499, 275), 7)
                pygame.draw.line(self.screen, line_color, (80, 386), (499, 386), 7)
                pygame.draw.line(self.screen, line_color, (80, 499), (499, 499), 7)

    def display_winner_window(self, winner):
        window_width = 400
        window_height = 200
        window_x = (800 - window_width) // 2
        window_y = (800 - window_height) // 2

        window_surface = pygame.Surface((window_width, window_height))
        window_surface.fill(self.PINK)

        font = pygame.font.Font("freesansbold.ttf", 36)
        text = font.render(f"{winner} has won!", True, self.BLACK)
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        window_surface.blit(text, text_rect)

        additional_font = pygame.font.Font("freesansbold.ttf", 15)
        additional_text = additional_font.render("press ESC to exit", True, (255, 0, 0))
        additional_text_rect = additional_text.get_rect(center=(window_width // 2, window_height // 2 + 40))
        window_surface.blit(additional_text, additional_text_rect)

        self.screen.blit(window_surface, (window_x, window_y))
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

    def save_exit_image(self):
        self.exit_image[1] = pygame.image.load("x.png").convert()

    def draw_exit_box(self):
        image1 = pygame.transform.scale(self.exit_image[1], (32, 32))
        self.screen.blit(image1, (742, 5))

    def draw_save_game(self):
        rect_width = 200
        rect_height = 50
        rect_x = 500
        rect_y = 0
        rect_surface = pygame.Surface((rect_width, rect_height))
        rect_surface.fill(self.PINK)
        pygame.draw.rect(rect_surface, self.BLACK, (0, 0, rect_width, rect_height), 2)
        font = pygame.font.Font("freesansbold.ttf", 24)
        text = font.render("Game Saving", True, self.BLACK)
        text_rect = text.get_rect(center=(rect_width // 2, rect_height // 2))

        rect_surface.blit(text, text_rect)
        self.screen.blit(rect_surface, (rect_x, rect_y))
        pygame.display.flip()
        time.sleep(2)

    def draw_timer_box(self):
        rect_width = 200
        rect_height = 50
        rect_x = 260
        rect_y = 0
        rect_surface = pygame.Surface((rect_width, rect_height))
        rect_surface.fill(self.PINK)
        pygame.draw.rect(rect_surface, self.BLACK, (0, 0, rect_width, rect_height), 2)
        font = pygame.font.Font("freesansbold.ttf", 24)
        text = font.render("Timer : ", True, self.BLACK)
        text_rect = text.get_rect(center=(rect_width // 2 - 30, rect_height // 2))

        rect_surface.blit(text, text_rect)
        self.screen.blit(rect_surface, (rect_x, rect_y))

    def clear_timer_number(self):
        rect_width = 50
        rect_height = 45
        rect_x = 370
        rect_y = 2
        rect_surface = pygame.Surface((rect_width, rect_height))
        pygame.draw.rect(rect_surface, self.PINK, (0, 0, rect_width, rect_height))
        self.screen.blit(rect_surface, (rect_x, rect_y))

    def timer_seconds(self, seconds):
        rect_width = 50
        rect_height = 45
        rect_x = 370
        rect_y = 2
        rect_surface = pygame.Surface((rect_width, rect_height))
        pygame.draw.rect(rect_surface, self.PINK, (0, 0, rect_width, rect_height))

        font = pygame.font.SysFont(None, 36)

        text = str(seconds)
        text_surface = font.render(text, True, self.BLACK)

        text_x = (rect_width - text_surface.get_width()) // 2
        text_y = (rect_height - text_surface.get_height()) // 2

        self.screen.blit(rect_surface, (rect_x, rect_y))
        self.screen.blit(text_surface, (rect_x + text_x, rect_y + text_y))

    def display_seconds_window(self):
        window_width = 400
        window_height = 200
        window_x = (800 - window_width) // 2
        window_y = (800 - window_height) // 2

        window_surface = pygame.Surface((window_width, window_height))
        window_surface.fill(self.PINK)

        font = pygame.font.Font("freesansbold.ttf", 36)
        text = font.render("Virus has won!", True, self.BLACK)
        text_rect = text.get_rect(center=(window_width // 2, window_height // 2))
        window_surface.blit(text, text_rect)

        additional_font = pygame.font.Font("freesansbold.ttf", 15)
        additional_text = additional_font.render("", True, (255, 0, 0))
        additional_text_rect = additional_text.get_rect(center=(window_width // 2, window_height // 2 + 40))
        window_surface.blit(additional_text, additional_text_rect)

        self.screen.blit(window_surface, (window_x, window_y))
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

    def turn_indicator_decorator(func):
        def wrapper(self, screen, turn):
            rect_width = 200
            rect_height = 50
            rect_x = 10
            rect_y = 0

            rect_surface = pygame.Surface((rect_width, rect_height))
            rect_surface.fill(self.PINK)
            pygame.draw.rect(rect_surface, self.BLACK, (0, 0, rect_width, rect_height), 2)

            font = pygame.font.Font("freesansbold.ttf", 24)
            text = font.render(f"Turn: {turn}", True, self.BLACK)
            text_rect = text.get_rect(center=(rect_width // 2, rect_height // 2))

            rect_surface.blit(text, text_rect)

            self.screen.blit(rect_surface, (rect_x, rect_y))

            func(screen, turn)

        return wrapper

    @turn_indicator_decorator
    def draw_turn_indicator(screen, playr):
        pass

    def attach(self, observer):
        if observer not in self.observer_list:
            self.observer_list.append(observer)

    def detach(self, observer):
        try:
            self.observer_list.remove(observer)
        except ValueError:
            pass

    def turn_setter(self, player_turn):
        self.turn = player_turn
        self.notify(self.turn)

    def notify(self, player_turn):
        for observer in self.observer_list:
            observer.update(player_turn)