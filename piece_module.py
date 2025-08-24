import pygame

size = 1.5

class Piece:
    def __init__(self, color, type, position, image):
        self.color = color
        self.type = type
        self.position = position
        self.image = pygame.image.load(f'{image}.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,
                                     (self.image.get_width() / size,
                                      self.image.get_height() / size))
        self.rect = self.image.get_rect(center=(position))

    def take_piece(self):
        pass
