import pygame

class screen:

    def __init__(self, screen_width, screen_height):
        self.screen_width = screen_width
        self.screen_height = screen_height

    def create_screen(alpha = None):
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)
        screen.set_alpha(alpha)
        
