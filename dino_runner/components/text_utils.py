from dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT
import pygame
FONT_STYLE = 'freesansbold.ttf'
black_color = (0, 0, 0)

def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 16)
    text = font.render('Points: '+ str(points), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (900, 50)
    return text, text_rect

def get_centered_message(message, width = SCREEN_WIDTH // 2 , height = SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STYLE, 32)
    text = font.render(message, True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect

def get_death_count(number):
    font = pygame.font.Font(FONT_STYLE, 16)
    text = font.render('Deaths: '+ str(number), True, black_color)
    text_rect = text.get_rect()
    text_rect.center = (900, 100)
    return text, text_rect