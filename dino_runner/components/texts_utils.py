import pygame
from dino_runner.utils.constants import FONT_STYLE, BLACK_COLOR, SCREEN_HEIGHT, SCREEN_WIDTH


def get_score_element(points):
    font = pygame.font.Font(FONT_STYLE, 20)

    text = font.render('Points: ' + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1000,50)
    return (text, text_rect)


def get_centered_message(message, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2):
    font = pygame.font.Font(FONT_STYLE, 30)

    text = font.render(message, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return text, text_rect
