import pygame

size = 1.5

class Piece:
    def __init__(self, color, type, position, image):
        self.color = color
        self.type = type
        self.position = position
        self.image = pygame.image.load(f'{image}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(75,75))
        self.rect = self.image.get_rect(center=(position))

class Square:
    def __init__(self, color, position, image):
        self.color = color
        self.position = position
        self.image = pygame.image.load(f'{image}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                     (self.image.get_width() / 1.6,
                                      self.image.get_height() / 1.6))
        self.rect = self.image.get_rect(center=(position))
