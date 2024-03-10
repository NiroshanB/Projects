import pygame
#pygame.font.init()
#font = pygame.font.Font("freesansbold.ttf", 18)
class Button(): 
    def __init__(self, image, x_pos, y_pos, button_text, font):
        self.image = image
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.font = font
        self.button_text = button_text
        self.text = self.font.render(self.button_text, True, (0,0,0))
        #self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.rect = self.image.get_rect(center = (self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))
    
    def update(self, screen):
        if self.image is not None: 
            screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    '''
    def update_text(self, newText):
        self.text = newText   
        self.render = font.render(self.text, True, 'black')
        self.text_width = self.render.get_width()
        self.text_height = self.render.get_height()
        self.box = pygame.Surface((self.text_width, self.text_height)) 
        self.rect = self.render.get_rect(topleft = self.rect.topleft)
    '''

    def set_text(self, button_text):
        self.button_text = button_text
        self.text = self.font.render(self.button_text, True, (0, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
      



    def user_click(self, mouse_pos):
        x_pos = mouse_pos[0]
        y_pos = mouse_pos[1]
        if x_pos in range(self.rect.left, self.rect.right) and y_pos in range(self.rect.top, self.rect.bottom):
            return True
        else:
            return False


button_image = pygame.image.load("button-image.png")
#button_image = pygame.transform.scale(button_image, (25, 25))

