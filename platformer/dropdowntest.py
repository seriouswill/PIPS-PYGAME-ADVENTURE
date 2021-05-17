import pygame, sys
import random
import new_pygame

pygame.init()
screen_width = 500
screen_height = 480
win = pygame.display.set_mode((screen_width, screen_height))

run = True

# colours
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
BLUE = (0,0,255)

# fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 40)
WORD_FONT = pygame.font.SysFont("comicsans", 30)
TITLE_FONT = pygame.font.SysFont("comicsans", 70)
text = TITLE_FONT.render("BERKPOCALYPSE", 1, BLACK)
choose_text = WORD_FONT.render("Choose your character!", 1, RED)

class OptionBox():

    def __init__(self, x, y, w, h, color, highlight_color, font, option_list, selected = 0):
        self.color = color
        self.highlight_color = highlight_color
        self.rect = pygame.Rect(x, y, w, h)
        self.font = font
        self.option_list = option_list
        self.selected = selected
        self.draw_menu = False
        self.menu_active = False
        self.active_option = -1

    def draw(self, surf):
        pygame.draw.rect(surf, self.highlight_color if self.menu_active else self.color, self.rect)
        pygame.draw.rect(surf, (0, 0, 0), self.rect, 2)
        msg = self.font.render(self.option_list[self.selected], 1, (0, 0, 0))
        surf.blit(msg, msg.get_rect(center = self.rect.center))

        if self.draw_menu:
            for i, text in enumerate(self.option_list):
                rect = self.rect.copy()
                rect.y += (i+1) * self.rect.height
                pygame.draw.rect(surf, self.highlight_color if i == self.active_option else self.color, rect)
                msg = self.font.render(text, 1, (0, 0, 0))
                surf.blit(msg, msg.get_rect(center = rect.center))
            outer_rect = (self.rect.x, self.rect.y + self.rect.height, self.rect.width, self.rect.height * len(self.option_list))
            pygame.draw.rect(surf, (0, 0, 0), outer_rect, 2)

    def update(self, event_list):
        mpos = pygame.mouse.get_pos()
        self.menu_active = self.rect.collidepoint(mpos)
        
        self.active_option = -1
        for i in range(len(self.option_list)):
            rect = self.rect.copy()
            rect.y += (i+1) * self.rect.height
            if rect.collidepoint(mpos):
                self.active_option = i
                break

        if not self.menu_active and self.active_option == -1:
            self.draw_menu = False

        for event in event_list:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.menu_active:
                    self.draw_menu = not self.draw_menu
                elif self.draw_menu and self.active_option >= 0:
                    self.selected = self.active_option
                    self.draw_menu = False
                    return self.active_option
        return -1

pygame.init()
clock = pygame.time.Clock()
window = pygame.display.set_mode((640, 480))

list1 = OptionBox(
    40, 40, 160, 40, (150, 150, 150), (100, 200, 255), pygame.font.SysFont(None, 30), 
    ["SAMMATRON", "PIPSTER", "PARTICK O'CRINKLE"])



while run:
    clock.tick(60)
    event_list = pygame.event.get()
    
    for event in event_list:
        if event.type == pygame.QUIT:
            run = False
    no_char_text = LETTER_FONT.render("I haven't coded that yet!", 1, BLUE)

    selected_option = list1.update(event_list)

    if event.type == pygame.MOUSEBUTTONDOWN:
        if selected_option == 1:
            new_pygame.run_game()
        else:
            win.blit(no_char_text, (screen_width/2 - text.get_width()/2, 220))
            pygame.display.update()
    

    window.fill((255, 255, 255))
    win.blit(text, (screen_width/2 - text.get_width()/2, 240))
    win.blit(choose_text, (screen_width/2 - text.get_width()/2, 300))
    list1.draw(window)
    pygame.display.flip()
    
pygame.quit()
exit()
